from pyodbc_data import *


total_clementines2019 = 0
for row in cursor2:
    if row[4]:
        total_clementines2019 += int(row[4])



total_clementines2018 = 0
for row in cursor1:
    if row[4]:
        total_clementines2018 += int(row[4])



total_clementines2017 = 0
for row in cursor:
    if row[4]:
        total_clementines2017 += int(row[4])


