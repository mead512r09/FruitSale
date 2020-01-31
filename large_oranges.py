from plotly.graph_objs import Bar, Layout
from plotly import offline
from pyodbc_data import *


def large_oranges():
    total_large_oranges = 0
    total_large_oranges2 = 0
    total_large_oranges3 = 0

    for row in cursor:
        if row[9] is not None:
            total_large_oranges += int(row[9])
    print(total_large_oranges)

    for row in cursor1:
        if row[9] is not None:
            total_large_oranges2 += int(row[9])
    print(total_large_oranges2)

    for row in cursor2:
        if row[9] is not None:
            total_large_oranges3 += int(row[9])
    print(total_large_oranges3)

    years_of_large_oranges = []
    years_of_large_oranges.append(total_large_oranges)
    years_of_large_oranges.append(total_large_oranges2)
    years_of_large_oranges.append(total_large_oranges3)

    y_values = years_of_large_oranges
    x_values = [2017, 2018, 2019]
    data = [Bar(x=x_values, y=y_values,
                text=y_values)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Amount of different '}
    my_layout = Layout(title='Amount of Large Oranges sold in 3 years',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='large_oranges.html')
