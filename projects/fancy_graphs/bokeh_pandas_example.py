# myapp.py
##This can be run using bokeh serve --show bokeh_pandas_example.py 
##This will require bokeh and pandas for python 
##

from bokeh.layouts import column, layout
from bokeh.models import Button, ColumnDataSource, HoverTool, TapTool
from bokeh.plotting import figure, curdoc
from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select, RadioGroup, DataTable, DateFormatter, TableColumn, Paragraph
import pandas

##Import the data
dat = pandas.read_csv("./prokaryotes.txt", sep='\t', low_memory=False)#, lineterminator='\n')

##get the frequency of each value in the Group column
counts = dat.groupby('Group')['Group'].count()
categories = list(dat.groupby('Group').groups.keys())
data = counts.tolist()


# Build a datatable based on the lists generated above
plot_source = ColumnDataSource(data=dict(
    x=categories,
    y=data,
))


##set up a figure. This will include the range, where the toolbar should go and what should be included in the toolbar
p = figure(x_range=categories, toolbar_location="below",tools='tap, pan,wheel_zoom,box_zoom,reset, save', toolbar_sticky=False)

##Include the data that will be plotted, along with what to do if one of the values is selected
p.vbar(x='x', top='y', source=plot_source, width=0.9,
                        selection_color="firebrick",

                       # set visual properties for non-selected glyphs
                       nonselection_fill_alpha=0.2,
                       nonselection_fill_color="blue",
                       nonselection_line_color="firebrick",
                       nonselection_line_alpha=1.0)

##add a tool that allows the name and value of a given bar (or point) to be displayed when the value is hovered over
p.add_tools(HoverTool(tooltips=[("Name", "@x"), ("Frequency", "@y")], mode='vline'))


##create a widget that is a dropdown box for selecting the column to plot the frequencies of
select = Select(title="Variable to plot frequency of:", value="Group", options=["Group", "SubGroup", "Status"])

##get a list of all of the points that will be plotted
status_list = list(dat.groupby('Group').groups.keys())

##create a widget that is a dropdown box for all of the values that a table could be filtered by based on the Group column
select_group = Select(title="Variable to show in table:", value="Group", options=status_list)


##create a text box and fill with some text
para = Paragraph(text="I'm suprised this works!",
                     width=200, height=100)

##working
def my_select_handler(attr, old,new):
    #print 'select button option ' + str(new) + ' selected.'

    counts = dat.groupby(new)[new].count()
    categories = list(dat.groupby(new).groups.keys())
    data = counts.tolist()

    plot_source.data = dict(
    x=categories,
    y=data,
)

    p.x_range.factors = categories
    p.vbar(x='x', top='y', source=plot_source, width=0.9,
                        selection_color="firebrick",

                       # set visual properties for non-selected glyphs
                       nonselection_fill_alpha=0.2,
                       nonselection_fill_color="blue",
                       nonselection_line_color="firebrick",
                       nonselection_line_alpha=1.0)
    p.add_tools(HoverTool(tooltips=[("Name", "@x"),("Frequency", "@y")], mode='vline'))
    select_group.options = categories
    select_group.value = categories[0]



def my_select_group_handler(attr, old,new):
    subset = dat.loc[dat[select.value].isin([new])]
    tmp = dict(subset[['Group', '#Organism/Name', 'Status', 'Release Date']])
    data_table.source.data.update(tmp)


##when the select dropdown is changed call the handler function for it and update the 'value' variable
select.on_change('value',my_select_handler)

##when the select_group dropdown is changed call the handler function for it and update the 'value' variable
select_group.on_change('value',my_select_group_handler)


##filter the data by the Group column for Proteobacteria
subset = dat.loc[dat['Group'].isin(['Proteobacteria'])]

##Build into a dict and the a datatable
data = dict(subset[['Group', '#Organism/Name', 'Status', 'Release Date']][0:100])
source = ColumnDataSource(data)

##Plot these columns of data in the table
columns = [
        TableColumn(field="Group", title="Group"),
        TableColumn(field="#Organism/Name", title="Organism/Name"),
        TableColumn(field="Status", title="Status"),
        TableColumn(field="Release Date", title="Release Date"),

]

##this is the data table that will be written to the screen
data_table = DataTable(source=source, columns=columns, width=400, height=280)


##set up the layout in a matrix format
l = layout([
  [widgetbox(select, select_group),column(p, data_table)],
  [para],
])

# put the button and plot in a layout and add to the document
curdoc().add_root(l)
