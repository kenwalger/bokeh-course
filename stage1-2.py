from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file('test.html')

plot = figure(plot_width=600, plot_height=800, tools='pan,box_zoom,reset')
plot.square(x=[1, 2, 4, 8, 10], y=[6, 2, 18, 4, 9], size=20)

show(plot)
