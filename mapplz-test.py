# mapplz-test.py
# base testing class for MapPLZ-Python
# FreeBSD license - by Nick Doiron (@mapmeld)

import unittest
import subprocess
import json
from mapplz import MapPLZ


class TestPEP8(unittest.TestCase):
    def test_mapitem_py(self):
        cmds = ['pep8', '--first', 'mapitem.py', 'mapplz.py', 'mapplz-test.py']
        linter = subprocess.Popen(cmds, stdout=subprocess.PIPE)
        output, err = linter.communicate()
        if output != "":
            print(output)
        self.assertTrue(output == '')


class TestWithoutDB(unittest.TestCase):
    def setUp(self):
        self.mapstore = MapPLZ()

    def test_add_pt_lat_lng(self):
        pt = self.mapstore.add(40, -70)
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt.type(), "point")
        self.assertEqual(pt["lat"], 40)
        self.assertEqual(pt["lng"], -70)

    def test_add_pt_lat_lng_prop(self):
        pt = self.mapstore.add(40, -70, "key")
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["property"], "key")
        self.assertEqual(pt.properties()["property"], "key")

    def test_add_pt_lat_lng_props(self):
        pt = self.mapstore.add(40, -70, {"color": "red"})
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["color"], "red")

    def test_add_pt_lat_lng_propstr(self):
        pt = self.mapstore.add(40, -70, '{"color": "red"}')
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["color"], "red")

    def test_add_json_latlng(self):
        pt = self.mapstore.add({"lat": 40, "lng": -70, "color": "red"})
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["color"], "red")

    def test_add_pt_latlng(self):
        pt = self.mapstore.add([40, -70])
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)

    def test_add_pt_latlngprop(self):
        pt = self.mapstore.add([40, -70, 'key'])
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["property"], "key")

    def test_add_pt_latlngprops(self):
        pt = self.mapstore.add([40, -70, {"color": "red"}])
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["color"], "red")

    def test_add_pt_latlngpropstr(self):
        pt = self.mapstore.add([40, -70, '{"color": "red"}'])
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["color"], "red")

    def test_add_pt_latlng_dict(self):
        pt = self.mapstore.add({"lat": 40, "lng": -70})
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)

    def test_add_pt_by_geojson_dict(self):
        gj = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-70, 40]
            }
        }
        pt = self.mapstore.add(gj)
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)

    def test_add_pt_by_geojson_string(self):
        gj = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-70, 40]
            }
        }
        pt = self.mapstore.add(json.dumps(gj))
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)

    def test_add_pt_latlng_kwargs(self):
        pt = self.mapstore.add(lat=40, lng=-70)
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)

    def test_add_pt_latlng_props_kwargs(self):
        pt = self.mapstore.add(lat=40, lng=-70, color="red")
        self.assertEqual(pt.lat(), 40)
        self.assertEqual(pt.lng(), -70)
        self.assertEqual(pt["properties"]["color"], "red")

    def test_add_line(self):
        line = self.mapstore.add([[40, -70], [22, -110]])
        self.assertEqual(line.path()[0][0], 40)
        self.assertEqual(line.path()[0][1], -70)
        self.assertEqual(line["path"][0][0], 40)
        self.assertEqual(line["path"][0][1], -70)
        self.assertEqual(line.type(), 'line')

    def test_add_latlng_line(self):
        linepts = [{"lat": 40, "lng": -70}, {"lat": 22, "lng": -110}]
        line = self.mapstore.add(linepts)
        self.assertEqual(line.type(), 'line')

    def test_add_path_line(self):
        linepts = {"path": [[40, -70], [22, -110]], "color": "red"}
        line = self.mapstore.add(linepts)
        self.assertEqual(line.type(), 'line')
        self.assertEqual(line["properties"]["color"], "red")

if __name__ == "__main__":
    unittest.main()
