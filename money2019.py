from pyodbc_data import *

total_money2019 = 0
for row in cursor2:
    if row[14]:
        total_money2019 += int(row[14])


total_money2017 = 0
for row in cursor:
    if row[14]:
        total_money2017 += int(row[14])


total_money2018 = 0
for row in cursor1:
    if row[14]:
        total_money2018 += int(row[14])

