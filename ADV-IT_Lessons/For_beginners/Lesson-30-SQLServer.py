#Библиотека
import pypyodbc

#Подключение к БД

mySQLServer = "MANOWAR\SQLEXPRESS"
myDatabase = "northwind"
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')

marker = connection.cursor()

#Текст запроса
mySQLQuery = ("""
                SELECT CompanyName, ContactName, Country 
                FROM dbo.Customers
                WHERE Country = 'Canada'
                """)

#Запуск
marker.execute(mySQLQuery)

#Вывод
results = marker.fetchall()

#Вывод на экран
for row in results:
    companyname = row[0]
    contactname = row[1]
    countryname = row[2] 

    print ("Welcome: " + str(companyname) + " User: " + str(contactname) + " From: " + str(countryname))

#Обязательно закрыть соединение к базе
connection.close()