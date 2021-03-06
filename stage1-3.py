import numpy as np
import pandas as pd

from bokeh.charts import Bar
from bokeh.io import output_file, show
from bokeh.plotting import ColumnDataSource, figure

file = 'country-pops.csv'
output_file('stage1-3.html')

countries = pd.read_csv(file, nrows=5)
countries_array = np.array(countries.head)

print(countries_array)

bar_chart = Bar(countries,
                'Country_English',
                values='Population',
                title="Population",
                legend=False)

country_data = ColumnDataSource(countries)

plot = figure(x_axis_label='Population', y_axis_label='Life Expectancy')

plot.circle(x='Population', y='Life_expectancy', source=country_data, size=15)

show(plot)
