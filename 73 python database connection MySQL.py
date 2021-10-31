'''
on cmd
    pip3 install mysql-connector
'''

import mysql.connector

#mydb = mysql.connector.connect(host="localhost", user="root", passwd="Abhay@321")
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Abhay@321", database="eadda")

mycursor = mydb.cursor()

#mycursor.execute("show databases")
mycursor.execute("select * from student")

for i in mycursor:
    print(i)

