import mysql.connector
import csv 

# create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE glass')
mycursor.execute('''CREATE TABLE glass.glass_table (`index` INT, RI REAL, Na REAL, Mg REAL,
                                                    Al REAL, Si REAL, K REAL, Ca REAL,
                                                    Ba REAL, Fe REAL, Class INT)''')

with open('glass.csv') as file:  
  reader = csv.DictReader(file)

  for record in reader:
    mycursor.execute('INSERT INTO glass.glass_table VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                    (record['index'], record['RI'], record['Na'], record['Mg'], record['Al'], record['Si'], record['K'], 
                     record['Ca'], record['Ba'], record['Fe'], record['Class']))


mydb.commit()

mycursor.execute('SELECT * FROM glass.glass_table')

for record in mycursor:
  print(record)
