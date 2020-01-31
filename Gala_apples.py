from plotly.graph_objs import Bar, Layout
from plotly import offline
from pyodbc_data import *


def gala_apples():
    total_GalaApples = 0
    for row in cursor:
        if row[15] is not None:
            total_GalaApples += int(row[15])
    print(total_GalaApples)

    total_GalaApples1 = 0
    for row in cursor1:
        if row[15] != None:
            total_GalaApples1 += int(row[15])
    print(total_GalaApples1)

    total_GalaApples2 = 0
    for row in cursor2:
        if row[15] != None:
            total_GalaApples2 += int(row[15])
    print(total_GalaApples2)

    all_years_GalaApples = []
    all_years_GalaApples.append(total_GalaApples)
    all_years_GalaApples.append(total_GalaApples1)
    all_years_GalaApples.append(total_GalaApples2)

    y_values = all_years_GalaApples

    x_values = [2017, 2018, 2019]
    data = [Bar(x=x_values, y=y_values,
                text=y_values,
                textposition='auto', )]

    x_axis_config = {'title': 'The Years', 'dtick': 1}
    y_axis_config = {'title': 'amount of Gala Apples'}
    my_layout = Layout(title='The amount of Gala Apples sold in the three years', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='Gala_Apples.html')

