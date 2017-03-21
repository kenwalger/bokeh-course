import pandas as pd

from bokeh.io import output_file, show
from bokeh.models import CategoricalColorMapper
from bokeh.plotting import ColumnDataSource, figure

file = 'country-pops.csv'
output_file('pop-life-expect.html')

countries = pd.read_csv(file, nrows=25)

country_data = ColumnDataSource(countries)

color_mapper = CategoricalColorMapper(factors=['Asia', 'Africa', 'Antarctica',
                                               'Australia', 'Central America',
                                               'Europe', 'North America',
                                               'Oceania', 'South America'],
                                      palette=['#00FF00', '#FFD343', 'darkgray',
                                               'brown', 'cyan', 'orange',
                                               'red', '#0000FF', 'purple'])


plot = figure(x_axis_label='Population', y_axis_label='Life Expectancy')

plot.diamond(x='Population', y='Life expectancy', source=country_data, size=10,
             color=dict(field='Continent', transform=color_mapper),
             legend='Continent')

plot.legend.location = 'bottom_right'
plot.legend.background_fill_color = 'lightgray'

show(plot)
