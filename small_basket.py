from pyodbc_data import *
import plotly.graph_objects as go
from plotly import offline


def small_basket():
    total_smallbasket = 0
    total_smallbasket1 = 0
    total_smallbasket2 = 0

    for row in cursor:
        if row[5]:
            total_smallbasket += (row[5])

    for row in cursor1:
        if row[5]:
            total_smallbasket1 += (row[5])

    for row in cursor2:
        if row[5]:
            total_smallbasket2 += (row[5])

    fig = go.Figure(data=[go.Scatter(
        x=[2017, 2018, 2019], y=[total_smallbasket, total_smallbasket1, total_smallbasket2],
        mode='markers',
        marker_size=[40, 45, 40])
    ])

    fig.show()

    print(total_smallbasket)
    print(total_smallbasket1)
    print(total_smallbasket2)
