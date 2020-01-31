from pyodbc_data import *

total_largegrapefruit2019 = 0

for row in cursor2:
    if row[8]:
        total_largegrapefruit2019 += int(row[8])


total_largegrapefruit2017 = 0

for row in cursor:
    if row[8]:
        total_largegrapefruit2017+= int(row[8])


total_largegrapefruit2018 = 0

for row in cursor1:
    if row[8]:
        total_largegrapefruit2018 += int(row[8])

