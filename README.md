# MapPLZ-Python

[MapPLZ](http://mapplz.com) is a framework to make mapping quick and easy in
your favorite language.

<img src="https://raw.githubusercontent.com/mapmeld/mapplz-python/master/logo.jpg" width="140"/>

## Getting started

MapPLZ consumes many many types of geodata. It can process data for a script or dump
it into a database.

Adding some data:

```
from mapplz import MapPLZ

mapstore = MapPLZ()

# add points
mapstore.add(40, -70);
mapstore.add([40, -70);
mapstore.add({ "lat": 40, "lng": -70 })
mapstore.add(lat=40, lng=-70)

# add lines
mapstore.add([[40, -70], [33, -110]])

# add polygons
mapstore.add([[[40, -70], [33, -110], [22, -90], [40, -70]]]);

# GeoJSON objects or strings
mapstore.add({ "type": "Feature", "geometry": { "type": "Point", "coordinates": [-70, 40] } });
mapstore.add('{ "type": "Feature", "geometry": { "type": "Point", "coordinates": [-70, 40] } }');

# add properties
mapstore.add({ "lat": 40, "lng": -70, "color": "blue" })
mapstore.add(40, -70, { "color": "blue" })
mapstore.add(lat=40, lng=-70, color="blue")

# update properties
pt = mapstore.add(40, -70)
pt["properties"]["color"] == "blue"

# also: WKT, CSV strings, and MapPLZ code
mapstore.add('POINT(-70 40)')
mapstore.add('color,geo\nred,\'{"type":"Feature","geometry":{"type":"Point","coordinates":[-70,40]}}\'')

mapcode = """
map
  marker
    [40, -70]
  plz
plz
"""
mapstore.add(mapcode)
```

Each feature is returned as a MapItem, which has easily-accessible data

```
pt = mapstore.add(40, -70)
pt.lat() == 40
pt["lat"] == 40
pt.toGeoJson() == '{ "type": "Feature", "geometry": { "type": "Point", "coordinates": [-70, 40] }}'
pt.delete()

line = mapstore.add([[40, -70], [50, 20]], { "color": "red" })
line["type"] == line.type() == "line"
line["path"] == line.path() == [[40, -70], [50, 20]]
line["properties"]["color"] == "red"
line.properties()["color"] == "red"
line.delete()
```

## Queries

You don't need a database to query data with MapPLZ, but when you link
Postgres/PostGIS or MongoDB, MapPLZ simplifies geodata management and queries:

```
# count all, return integer
count = mapstore.count()

# query all, return [ MapItem ]
mapstore.query()

# five nearest - can also send GeoJSON, { "lat": 40, "lng": -70 }, or MapItem
nearest = mapstore.near([lat, lng], 5)

# all points within this polygon
# can also send GeoJSON, { path: [[[]]] }, or MapItem
inside = mapstore.within([[[40, -70], [50, -80], [30, -80], [40, -70]]])
```

## Install

Simply run ```pip install mapplz```

If you are building from source, make sure to install dependencies by running ```pip install -r requirements.txt```

## License

Free BSD License
