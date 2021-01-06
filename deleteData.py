import sqlite3

connection = sqlite3.connect("Lizenzen.db")
cursor = connection.cursor()


id = input("Datensatz ID: ")
sql = "DELETE FROM Lizenzen WHERE ID = "+id
cursor.execute(sql)
connection.commit()

connection.close()
input("Bitte Enter drücken um dieses Programm zu schließen...")