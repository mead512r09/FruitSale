from plotly.graph_objs import Bar, Layout
from plotly import offline
from pyodbc_data import *


def small_oranges():
    total_small_oranges = 0
    total_small_oranges2 = 0
    total_small_oranges3 = 0

    for row in cursor:
        if row[11] is not None:
            total_small_oranges += int(row[11])
    print(total_small_oranges)

    for row in cursor1:
        if row[11] is not None:
            total_small_oranges2 += int(row[11])
    print(total_small_oranges2)

    for row in cursor2:
        if row[11] is not None:
            total_small_oranges3 += int(row[11])
    print(total_small_oranges3)

    years_of_smalloranges = []
    years_of_smalloranges.append(total_small_oranges)
    years_of_smalloranges.append(total_small_oranges2)
    years_of_smalloranges.append(total_small_oranges3)

    y_values = years_of_smalloranges
    x_values = [2017, 2018, 2019]
    data = [Bar(x=x_values, y=y_values)]

    x_axis_config = {'title': 'Years', 'dtick': 1}
    y_axis_config = {'title': 'Amount of Small Oranges'}
    my_layout = Layout(title='Amount of Small Oranges sold in 3 years',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='small_oranges.html')
