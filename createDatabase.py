import os
import sys
import sqlite3

#Datenbank vorhanden
if os.path.exists("Lizenzen.db"):
    print("Datenbank ist vorhanden!")
    sys.exit(0)

#Datenbank erstellen und Verbindung herstellen
connection = sqlite3.connect("Lizenzen.db")

#Cursor erzeugen
cursor = connection.cursor()

#Tabelle erzeugen
sql = "Create TABLE Lizenzen(" \
    "ID INTEGER primary key autoincrement, " \
    "Programm TEXT," \
    "LizenzInhaber TEXT," \
    "Notizen TEXT," \
    "Seriennummer TEXT)"
cursor.execute(sql)

connection.close()
print("Datenbank wurde erstellt!")
input("Bitte Enter drücken um dieses Programm zu schließen...")