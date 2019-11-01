import mysql.connector
from mysql.connector import errorcode
import csv

try:
    cnx = mysql.connector.connect(
        user="root",
        password="gyTwce<U:23c",
        host="localhost",
        database="OrchLib"
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error: {}".format(err))
        cnx.close()

cursor = cnx.cursor()


with open('formatted_library.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        vals = [row[i].replace("\"", "") for i in range(1, len(row))]
        vals.append(row[0])
        text = "INSERT INTO regular (Composer, Arranger, Title, Type, Grade, PML, Piano, History, Comments, Location) VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\",\"{9}\")"
        # print(vals)
        command = text.format(*vals)
        try:
            cursor.execute(command)
        except:
            print(command)
            print("Cursor error! Abort!")
            break
    cnx.commit()

    cursor.close()
    cnx.close()
