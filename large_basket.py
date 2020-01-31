from pyodbc_data import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


def large_basket():
    # Three Graphs
    total_LargeBasket = 0
    total_LargeBasket2 = 0
    total_LargeBasket3 = 0

    # Fetching data from rows for cursors 1-3
    for row in cursor:
        if row[6]:
            total_LargeBasket += int(row[6])
    print(total_LargeBasket)

    for row in cursor1:
        if row[6]:
            total_LargeBasket2 += int(row[6])
    print(total_LargeBasket2)

    for row in cursor2:
        if row[6]:
            total_LargeBasket3 += int(row[6])
    print(total_LargeBasket3)

    years_largebaskets_sold = [total_LargeBasket, total_LargeBasket2, total_LargeBasket3]

    # Making graph
    fig, ax = plt.subplots()
    y_values = years_largebaskets_sold
    x_values = 2017, 2018, 2019

    plt.plot(x_values, y_values, 'red')

    title = "Fruit sale results for 'Large Basket'\n2017-19"
    plt.title(title, fontsize=16)
    plt.xlabel("From 2017, 2018, & 2019", c='blue', fontsize=14)
    plt.ylabel("Number Sold",c='blue', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.ylim(450,500)

    plt.show()
