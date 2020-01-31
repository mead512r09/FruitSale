from pyodbc_data import *

total_smallgrapefruit2019 = 0

for row in cursor2:
    if row[7]:
        total_smallgrapefruit2019 += int(row[7])


total_smallgrapefruit2017 = 0

for row in cursor:
    if row[7]:
        total_smallgrapefruit2017+= int(row[7])


total_smallgrapefruit2018 = 0

for row in cursor1:
    if row[7]:
        total_smallgrapefruit2018 += int(row[7])

