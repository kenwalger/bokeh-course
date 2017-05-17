import pandas as pd

from bokeh.io import output_file, show
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.plotting import ColumnDataSource, figure

input_file = 'country-pops.csv'
output_file('pop-life.html')

countries = pd.read_csv(input_file)

country_data = ColumnDataSource(countries)

color_mapper = CategoricalColorMapper(factors=['Asia', 'Africa', 'Antarctica',
                                               'Australia', 'Central America',
                                               'Europe', 'North America',
                                               'Oceania', 'South America'],
                                      palette=['#00FF00', '#FFD343', 'darkgray',
                                               'brown', 'cyan', 'crimson',
                                               'red', '#0000FF', 'purple'])

plot = figure(x_axis_label='Population',
              y_axis_label='Life Expectancy',
              title='Population vs. Life Expectancy',
              tools="pan,wheel_zoom,box_zoom,reset,hover,save")

plot.diamond(x='Population', y='Life_expectancy', source=country_data,
             size=10, color=dict(field='Continent', transform=color_mapper),
             legend='Continent')

plot.legend.location = 'bottom_right'
plot.legend.background_fill_color = 'lightgray'

hover = plot.select_one(HoverTool)
hover.tooltips = [('Country Name English', '@Country_English'),
                  ('Population', '@Population'),
                  ('Life Expectancy (years)', '@Life_expectancy'),
                  ]

show(plot)
