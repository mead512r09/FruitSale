from plotly.graph_objs import Bar, Layout
from plotly import offline
from pyodbc_data import *


def red_apples():
    total_RedApples = 0
    for row in cursor:
        if row[12] is not None:
            total_RedApples += int(row[12])
    print(total_RedApples)

    total_RedApples1 = 0
    for row in cursor1:
        if row[12] != None:
            total_RedApples1 += int(row[12])
    print(total_RedApples1)

    total_RedApples2 = 0
    for row in cursor2:
        if row[12] != None:
            total_RedApples2 += int(row[12])
    print(total_RedApples2)

    all_years_RedApples = []
    all_years_RedApples.append(total_RedApples)
    all_years_RedApples.append(total_RedApples1)
    all_years_RedApples.append(total_RedApples2)

    y_values = all_years_RedApples

    x_values = [2017, 2018, 2019]
    data = [Bar(x=x_values, y=y_values,
                text=y_values,
                textposition='auto', )]

    x_axis_config = {'title': 'The Years', 'dtick': 1}
    y_axis_config = {'title': 'amount of Red Apples'}
    my_layout = Layout(title='The amount of Red Apples sold in the three years', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='Red_Apples.html')

