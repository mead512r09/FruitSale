from plotly.graph_objs import Bar, Layout
from plotly import offline
from pyodbc_data import *


def santa_oranges():
    total_santa_oranges = 0
    total_santa_oranges2 = 0
    total_santa_oranges3 = 0


    for row in cursor:
        if row[10] is not None:
            total_santa_oranges += int(row[10])
    print(total_santa_oranges)

    for row in cursor1:
        if row[10] is not None:
            total_santa_oranges2 += int(row[10])
    print(total_santa_oranges2)

    for row in cursor2:
        if row[10] is not None:
            total_santa_oranges3 += int(row[10])
    print(total_santa_oranges3)

    years_of_santa_oranges = []
    years_of_santa_oranges.append(total_santa_oranges)
    years_of_santa_oranges.append(total_santa_oranges2)
    years_of_santa_oranges.append(total_santa_oranges3)

    y_values = years_of_santa_oranges
    x_values = [2017, 2018, 2019]
    data = [Bar(x=x_values, y=y_values)]

    x_axis_config = {'title': 'Years', 'dtick': 1}
    y_axis_config = {'title': 'Santa Oranges'}
    my_layout = Layout(title='Amount of Santa Oranges sold in 3 years',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='santa_oranges.html')
