import sqlite3 as sql
import json

con = sql.connect("computer.sqlite") #lien vers la vse de doné
cur = con.cursor()

cur.execute("SELECT nompc FROM machine WHERE EXISTS (SELECT numpc FROM assemble WHERE EXISTS (SELECT DISTINCT refcomp FROM cartevideo WHERE ramvideo>=8 AND cartevideo.refcomp=assemble.refcomp AND machine.numpc=assemble.numPC))")
#au dessus ^ la req sql a excuter
res = cur.fetchall()


# Obtenir les noms des colonnes
column_names = [description[0] for description in cur.description] #pour recup le nom des colones 

print("<!Doctype html>") #debut du code html

print("<html>")
print("<head>")

print("<style>table{border-collapse:collapse;}td{text-align:center;border:1px solid black;}th{text-align:center;border:1px solid black;}</style>")
# ^ tout le style du tableau

print("</head>")

print("<center>") #pour centrer le tableau
print("<table>") #creation tableau

# Générer automatiquement les balises th en fonction des noms de colonnes
print("<tr>") #titre en haut du tableau en gras (nom de colonne)
for col_name in column_names: #proute toutes les colones
    #print("")
    print("<th>", col_name, "</th>") #on affiche le nom des collones 
print("</tr>")

for row in res: #pour tout paramètre dans le résultat de la requete 
    print("<tr>")
    for column in row:
        if column is None: #si pas de colone on met un - 
            print("<td>-</td>")
        else:
            print('<td>' + str(column) + "</td> </font>") #sinon 
    print("</tr>")

print("</table>")
print("</center>")
print("</html>")

con.close()
