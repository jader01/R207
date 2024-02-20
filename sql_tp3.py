import sqlite3 as sql
import json

con = sql.connect("computer.sqlite")
cur = con.cursor()

cur.execute("SELECT nompc, refcomp FROM machine, composant WHERE EXISTS (SELECT refcomp FROM assemble WHERE assemble.refcomp=Composant.refcomp AND machine.numpc=assemble.numpc)")
res = cur.fetchall()

# Obtenir les noms des colonnes
column_names = [description[0] for description in cur.description]

print("<!Doctype html>")

print("<style>table{border-collapse:collapse;}td{text-align:center;border:1px solid black;}th{text-align:center;border:1px solid black;}</style>")

print("<center>")
print("<table>")

# Générer automatiquement les balises th en fonction des noms de colonnes
print("<tr>")
for col_name in column_names:
    print("")
    print("<th>", col_name, "</th>")
print("</tr>")

for row in res:
    print("<tr>")
    for column in row:
        if column is None:
            print("<td>-</td>")
        else:
            print("<td>" + str(column) + "</td>")
    print("</tr>")

print("</table>")
print("</center>")

con.close()
