"""Synthetic fixtures test structural errors; these are never published map data."""
import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_geojson import validate, unique_keys, reject_constant


def collection(geometry=None):
    return {'type': 'FeatureCollection', 'features': [{
        'type': 'Feature',
        'properties': {'id': 'test-only', 'name': 'Synthetic test', 'source': 'unit test'},
        'geometry': geometry or {'type': 'Point', 'coordinates': [0, 0]},
    }]}


class ValidationTests(unittest.TestCase):
    def test_empty_placeholder(self):
        self.assertEqual(validate({'type': 'FeatureCollection', 'features': []}), 0)

    def test_all_geometry_types(self):
        ring = [[0, 0], [2, 0], [0, 2], [0, 0]]
        geometries = [
            {'type': 'Point', 'coordinates': [0, 0, 10]},
            {'type': 'MultiPoint', 'coordinates': [[0, 0]]},
            {'type': 'LineString', 'coordinates': [[0, 0], [1, 1]]},
            {'type': 'MultiLineString', 'coordinates': [[[0, 0], [1, 1]]]},
            {'type': 'Polygon', 'coordinates': [ring]},
            {'type': 'MultiPolygon', 'coordinates': [[ring]]},
            {'type': 'GeometryCollection', 'geometries': [{'type': 'Point', 'coordinates': [0, 0]}]},
        ]
        for geometry in geometries:
            with self.subTest(geometry=geometry):
                self.assertEqual(validate(collection(geometry)), 1)

    def test_bad_coordinates(self):
        for coordinates in ([49, -123], [181, 0], [True, 0], [0, float('nan')], [0], ['0', 0]):
            with self.subTest(coordinates=coordinates), self.assertRaises(ValueError):
                validate(collection({'type': 'Point', 'coordinates': coordinates}))

    def test_bad_rings(self):
        for ring in ([[0, 0], [1, 0], [1, 1], [0, 1]], [[0, 0]] * 4):
            with self.assertRaises(ValueError):
                validate(collection({'type': 'Polygon', 'coordinates': [ring]}))

    def test_missing_properties_and_null_geometry(self):
        for key in ('id', 'name', 'source'):
            data = collection()
            del data['features'][0]['properties'][key]
            with self.assertRaises(ValueError):
                validate(data)
        data = collection()
        data['features'][0]['geometry'] = None
        with self.assertRaises(ValueError):
            validate(data)

    def test_duplicate_id_across_layers(self):
        seen = set()
        validate(collection(), seen)
        with self.assertRaisesRegex(ValueError, 'duplicate feature ID'):
            validate(collection(), seen)

    def test_preserves_unknown_metadata(self):
        data = collection()
        data['features'][0]['properties']['original_metadata'] = {'anything': [1, 2]}
        before = copy.deepcopy(data)
        validate(data)
        self.assertEqual(data, before)

    def test_strict_json(self):
        for text in ('{"a": 1, "a": 2}', '{"a": NaN}'):
            with self.assertRaises(ValueError):
                json.loads(text, object_pairs_hook=unique_keys, parse_constant=reject_constant)

    def test_legacy_crs(self):
        data = collection()
        data['crs'] = {'type': 'name'}
        with self.assertRaises(ValueError):
            validate(data)


if __name__ == '__main__':
    unittest.main()
