from __future__ import print_function

import requests
import numpy as np

import bokeh
print(bokeh.__version__)

from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource, HoverTool
from bokeh.plotting import figure

url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'

r = requests.get(url)
geo_json_data = r.json()

print(geo_json_data)


def get_coordinates(features):
    depth = lambda L: isinstance(L, list) and max(map(depth, L))+1
    country_id = []
    xs = []
    ys = []
    for feature in geo_json_data['features']:
        coords = feature['geometry']['coordinates']
        nbdims = depth(coords)
        country_id.append(feature['id'])
        # one border
        if nbdims == 3:
            pts = np.array(coords[0], 'f')
            xs.append(pts[:, 0])
            ys.append(pts[:, 1])
        # several borders
        else:
            for shape in coords:
                pts = np.array(shape[0], 'f')
                xs.append(pts[:, 0])
                ys.append(pts[:, 1])
    return country_id, xs, ys

country_id, xs, ys = get_coordinates(geo_json_data['features'])

country_name = [country_id for country in country_id]

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(plot_width=900, plot_height=600, title="World Map",
           tools=TOOLS, x_range=(-180, 180), y_range=(-90, 90))

p.patches(xs, ys, fill_color="#F1EEF6", fill_alpha=0.7, line_width=2)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Country", "@country_name")
]

output_file("test.html")
show(p)
