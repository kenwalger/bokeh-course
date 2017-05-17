import numpy as np
import pandas as pd
import requests

from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import ColumnDataSource, figure

output_file("world-map.html")
url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

r = requests.get(url)
json_data = r.json()


def get_coordinates(features):
    depth = lambda L: isinstance(L, list) and max(map(depth, L))+1
    country_id = []
    longitudes = []
    latitudes = []

    for feature in json_data['features']:
        coordinates = feature['geometry']['coordinates']
        number_dimensions = depth(coordinates)
        # one border
        if number_dimensions == 3:
            country_id.append(feature['id'])
            points = np.array(coordinates[0], 'f')
            longitudes.append(points[:, 0])
            latitudes.append(points[:, 1])
        # several borders
        else:
            for shape in coordinates:
                country_id.append(feature['id'])
                points = np.array(shape[0], 'f')
                longitudes.append(points[:, 0])
                latitudes.append(points[:, 1])
    return country_id, longitudes, latitudes

country_id, lats, longs = get_coordinates(json_data['features'])

print("Country Count: {}\nLat Count: {}\nLong Count:{}\n".format(len(
    country_id), len(lats), len(longs)))

# country_name = [country_id for country in country_id]

world_map_plot = figure(plot_width=900, plot_height=600, title="World Map",
                        tools=TOOLS, x_range=(-180, 180), y_range=(-90, 90))

world_map_plot.patches(lats, longs, fill_color="#F1EEF6", fill_alpha=0.7,
                       line_width=2)

# hover = world_map_plot.select_one(HoverTool)
# hover.point_policy = "follow_mouse"
# hover.tooltips = [
#     ("Country", "@country_name")
# ]

# show(world_map_plot)
