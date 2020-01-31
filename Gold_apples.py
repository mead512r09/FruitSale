from plotly.graph_objs import Bar, Layout
from plotly import offline
from pyodbc_data import *


def gold_apples():
    total_GoldApples = 0
    for row in cursor:
        if row[13] is not None:
            total_GoldApples += int(row[13])
    print(total_GoldApples)

    total_GoldApples1 = 0
    for row in cursor1:
        if row[13] != None:
            total_GoldApples1 += int(row[13])
    print(total_GoldApples1)

    total_GoldApples2 = 0
    for row in cursor2:
        if row[13] != None:
            total_GoldApples2 += int(row[13])
    print(total_GoldApples2)

    all_years_GoldApples = []
    all_years_GoldApples.append(total_GoldApples)
    all_years_GoldApples.append(total_GoldApples1)
    all_years_GoldApples.append(total_GoldApples2)

    y_values = all_years_GoldApples

    x_values = [2017, 2018, 2019]
    data = [Bar(x=x_values, y=y_values,
                text=y_values,
                textposition='auto', )]

    x_axis_config = {'title': 'The Years', 'dtick': 1}
    y_axis_config = {'title': 'amount of Gold Apples'}
    my_layout = Layout(title='The amount of Gold Apples sold in the three years', xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='Gold_Apples.html')

