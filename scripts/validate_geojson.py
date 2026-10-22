"""Structural GeoJSON checks; no dependencies and no geometry mutation."""
import json
import math
from pathlib import Path
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def position(value):
    require(isinstance(value, list) and len(value) in (2, 3), 'position must have 2 or 3 coordinates')
    require(all(type(n) in (int, float) and math.isfinite(n) for n in value), 'coordinates must be finite numbers')
    require(-180 <= value[0] <= 180 and -90 <= value[1] <= 90, 'longitude/latitude out of range')


def sequence(value, minimum, check):
    require(isinstance(value, list) and len(value) >= minimum, f'expected at least {minimum} members')
    for item in value:
        check(item)


def ring(value):
    sequence(value, 4, position)
    require(value[0] == value[-1], 'polygon ring is not closed')
    require(len({tuple(p[:2]) for p in value[:-1]}) >= 3, 'polygon ring needs 3 distinct vertices')


def geometry(value):
    require(isinstance(value, dict), 'geometry must be an object')
    require('crs' not in value, 'legacy crs is not supported')
    kind = value.get('type')
    if kind == 'GeometryCollection':
        sequence(value.get('geometries'), 1, geometry)
        return
    checks = {
        'Point': position,
        'MultiPoint': lambda c: sequence(c, 1, position),
        'LineString': lambda c: sequence(c, 2, position),
        'MultiLineString': lambda c: sequence(c, 1, lambda line: sequence(line, 2, position)),
        'Polygon': lambda c: sequence(c, 1, ring),
        'MultiPolygon': lambda c: sequence(c, 1, lambda polygon: sequence(polygon, 1, ring)),
    }
    require(isinstance(kind, str) and kind in checks, 'unsupported geometry type')
    checks[kind](value.get('coordinates'))


def validate(document, seen=None):
    if seen is None:
        seen = set()
    require(isinstance(document, dict) and document.get('type') == 'FeatureCollection', 'expected FeatureCollection')
    require('crs' not in document, 'legacy crs is not supported')
    features = document.get('features')
    require(isinstance(features, list), 'features must be an array')
    for index, feature in enumerate(features):
        try:
            require(isinstance(feature, dict) and feature.get('type') == 'Feature', 'expected Feature')
            require('crs' not in feature, 'legacy crs is not supported')
            properties = feature.get('properties')
            require(isinstance(properties, dict), 'properties must be an object')
            for key in ('id', 'name', 'source'):
                require(isinstance(properties.get(key), str) and properties[key].strip(), f'properties.{key} must be a nonempty string')
            feature_id = properties['id']
            require(feature_id not in seen, f'duplicate feature ID: {feature_id}')
            geometry(feature.get('geometry'))
            seen.add(feature_id)
        except ValueError as error:
            raise ValueError(f'feature {index}: {error}') from error
    return len(features)


def reject_constant(value):
    raise ValueError(f'invalid JSON number: {value}')


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def main():
    root = Path(__file__).resolve().parents[1]
    paths = sorted((root / 'data').glob('*.geojson'))
    require(bool(paths), 'no data/*.geojson files found')
    seen = set()
    for path in paths:
        try:
            document = json.loads(path.read_text(encoding='utf-8'), parse_constant=reject_constant, object_pairs_hook=unique_keys)
            count = validate(document, seen)
        except (ValueError, OSError, RecursionError) as error:
            raise ValueError(f'{path.name}: {error}') from error
        print(f'{path.name}: valid ({count} features)')


if __name__ == '__main__':
    try:
        main()
    except ValueError as error:
        print(f'Validation failed: {error}', file=sys.stderr)
        sys.exit(1)
