import sqlite3

outputData = open("LizenzenDatabase.txt", "w")

#Verbindung herstellen
connection = sqlite3.connect("Lizenzen.db")
cursor = connection.cursor()

#SQL Befehl
sql = "SELECT * FROM Lizenzen ORDER BY Programm, LizenzInhaber"

#SQL Befehl ausgabe
cursor.execute(sql)
outputData.write(""+30* "-" + " Lizenzen [Lizenzen.db] "+ 30*"-")
outputData.write("\nID   /   Programm   /   LizenzInhaber   /   Notizen   /   SerienNummer")
for data in cursor:
    outputData.write("\n"+str(data[0]) + "               " + str(data[1]) + "              " + str(data[2]) + "               " + str(data[3]) + "               " + str(data[4]))

#Verbindung schließen
connection.close()
input("Bitte Enter drücken um dieses Programm zu schließen...")