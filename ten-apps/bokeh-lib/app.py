from bokeh.charts import Scatter  #, output_file, show
from bokeh.plotting import figure, output_file, show
import pandas

df = pandas.DataFrame(columns=['X', 'Y'])
df['X'] = [1, 2, 3, 4, 5]
df['Y'] = [5, 6, 4, 5, 3]

p = Scatter(df, x='X', y='Y', title='Temperature Observations', xlabel='Day of observation', ylabel='Temperature')

# output_file('scatter_charts.html')
# show(p)

p = figure(plot_width=500, plot_height=400)
p.title.text = 'Temperature Observations'
p.title.text_color = 'orange'
p.title.text_font = 'times'
p.title.text_font_style = 'italic'

p.circle([1, 2, 3, 4, 5], [5, 6, 4, 5, 3], size=[8, 12, 14, 15, 20], color='red', alpha=0.5)
# p.triangle([1, 2, 3, 4, 5], [5, 6, 4, 5, 3], size=5, color='red', alpha=0.5)
output_file('scatter_plotting.html')
show(p)