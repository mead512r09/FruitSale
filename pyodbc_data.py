import pyodbc


pyodbc.lowercase = False
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\mini512r10\Documents\Python\fruitsale\data\2017AnthisFruit.accdb;')
conn1 = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                       r'DBQ=C:\Users\mini512r10\Documents\Python\fruitsale\data\2018AnthisFruit.accdb;')
conn2 = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                       r'DBQ=C:\Users\mini512r10\Documents\Python\fruitsale\data\2019AnthisFruit.accdb;')

cursor = conn.cursor()
cursor.execute('SELECT*FROM FruitSale')
cursor1 = conn1.cursor()
cursor1.execute('SELECT*FROM FruitSale')
cursor2 = conn2.cursor()
cursor2.execute('SELECT*FROM FruitSale')


cursor = cursor.fetchall()
cursor1 = cursor1.fetchall()
cursor2 = cursor2.fetchall()
