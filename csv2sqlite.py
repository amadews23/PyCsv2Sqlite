# Pequenyo script para insertar columnas de un csv a una tabla
#
#
import csv, sqlite3
conn = sqlite3.connect("ant.db")
curs = conn.cursor()
#Delimiter in csv file (,)
reader = csv.reader(open('Clients.csv', 'r'), delimiter=',')
for row in reader:

	to_db = [unicode(row[0],"utf8"), unicode(row[1], "utf8")]
	curs.execute("INSERT INTO clientes (nombre, apellidos) VALUES (?, ?);", to_db)
	conn.commit()
