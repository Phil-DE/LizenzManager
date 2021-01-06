import sqlite3

#Verbindung
connection = sqlite3.connect("Lizenzen.db")
cursor = connection.cursor()

#Eingabe
Programm = input("Programm: ")
Owner = input("LizenzInhaber (Name oder PC-Name) : ")
notes = input("Notizen (Optional) : ")
if notes == "":
    notes = "/"
serialNumber = input("SerienNummer (Optional) : ")
if serialNumber == "":
    serialNumber = "/"

sql = "INSERT INTO Lizenzen VALUES(" + "NULL," + "'" + Programm + "'" + "," + "'" + Owner + "'" + "," + "'" + notes + "'" + "," + "'" + serialNumber + "')"
cursor.execute(sql)
connection.commit()

connection.close()
input("Enter drücken um dieses Programm zu schließen...")