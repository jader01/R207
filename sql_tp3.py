import sqlite3 as sql
import json

con = sql.connect("computer.sqlite") #lien vers la vse de doné
cur = con.cursor()

cur.execute("SELECT nompc, refcomp FROM machine, composant WHERE EXISTS (SELECT refcomp FROM assemble WHERE assemble.refcomp=Composant.refcomp AND machine.numpc=assemble.numpc)")
#au dessus ^ la req sql a excuter
res = cur.fetchall()


# Obtenir les noms des colonnes
column_names = [description[0] for description in cur.description] #pour recup le nom des colones 

print("<!Doctype html>") #debut du code html

print("<style>table{border-collapse:collapse;}td{text-align:center;border:1px solid black;}th{text-align:center;border:1px solid black;}</style>")
# ^ tout le style du tableau

print("<center>") #pour centrer le tableau
print("<table>") #creation tableau

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
