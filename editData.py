import sqlite3

connection = sqlite3.connect("Lizenzen.db")
cursor = connection.cursor()

id = input("ID: ")
id = int(id)
status = False
column = ""
while status == False:
    print("########## Verfügbare Datensätze ##########")
    print("Programm / LizenzInhaber / Notizen / SerienNummer")
    column = input("Welcher Datensatz soll geändert werden: ")
    if column == "Programm":
        status = True
        break
    if column == "LizenzInhaber":
        status = True
        break
    if column == "Notizen":
        status = True
        break
    if column == "LizenzNummer":
        status = True
        break
    if status == True:
        print("Falsche Eingabe! Bitte überprüfe deine Eingabe...")
updateData = input("Neuer Eintrag: ")
sql = "UPDATE Lizenzen SET " + column + " = " + "'" + updateData + "'" + " WHERE ID = "+str(id)
cursor.execute(sql)
connection.commit()
connection.close()
