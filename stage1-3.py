import numpy as np
import pandas as pd

from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure

file = 'country-pops.csv'
output_file('pop-life-expect.html')

countries = pd.read_csv(file, nrows=25)
countries_array = np.array(countries.head)

print(countries_array)


country_data = ColumnDataSource(countries)

plot = figure(x_axis_label='Population', y_axis_label='Life Expectancy')

plot.circle(x='Population', y='Life expectancy', source=country_data, size=15)

show(plot)
