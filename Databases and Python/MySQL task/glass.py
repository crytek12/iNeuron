import mysql.connector
import csv

mydb = mysql.connector.connect(
    host='localhost',
    user='abc',
    password='password'
)

mycursor = mydb.cursor()

# Creating a database called glass
mycursor.execute('CREATE DATABASE IF NOT EXISTS glass')

# Creating a table called glass_table
mycursor.execute('''CREATE TABLE IF NOT EXISTS glass.glass_table(
    `index` INT(10), 
    RI FLOAT(10, 5),
    Na FLOAT(10, 5),
    Mg FLOAT(10, 5),
    Al FLOAT(10, 5),
    Si FLOAT(10, 5),
    K FLOAT(10, 5),
    Ca FLOAT(10, 5),
    Ba FLOAT(10, 5),
    Fe FLOAT(10, 5),
    Class INT(10))
''')

with open('glass.data') as file:
    reader = csv.reader(file)
    next(reader)

    for record in reader:
        mycursor.execute(f'INSERT INTO glass.glass_table VALUES {tuple(record)}')
    mydb.commit()

# See values
mycursor.execute('SELECT * FROM glass.glass_table')

for record in mycursor:
    print(record)
