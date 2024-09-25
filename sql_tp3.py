##################################################################################
#                                    import librairie
################################################################################

import sqlite3 as sql
import json

####################################################################################
#                            création connexion basse de donée +
#                            associser a variable résultat requête
##############################################################################

con = sql.connect("computer.sqlite") #lien vers la bdd
cur = con.cursor()

cur.execute("SELECT nompc, refcomp FROM machine, composant WHERE EXISTS (SELECT refcomp FROM assemble WHERE assemble.refcomp=Composant.refcomp AND machine.numpc=assemble.numpc)")
#au dessus ^ la req sql a excuter
res = cur.fetchall()


##########################################################################################
#                         récupération donner pour génération html après
###########################################################################################

# Obtenir les noms des colonnes
column_names = [description[0] for description in cur.description] #pour recup le nom des colones 


##########################################################################################
#                                   génération code html
########################################################################################

print("<!Doctype html>") #debut du code html

print("<html>")
print("<head>")

print("<title> sql en python </title>")

print("<style>table{border-collapse:collapse;}td{text-align:center;border:1px solid black;}th{text-align:center;border:1px solid black;}</style>")
# ^ tout le style du tableau

print("</head>")

print("<body>")
print("<center>") #pour centrer le tableau
print("<table>") #creation tableau

# Générer automatiquement les balises th en fonction des noms de colonnes
print("<tr>") #titre en haut du tableau en gras (nom de colonne)
for col_name in column_names: #printe toutes les colones
    #print("")
    print("<th>", col_name, "</th>") #on affiche le nom des collones 
print("</tr>")

for row in res: #pour tout paramètre dans le résultat de la requete 
    print("<tr>")
    for column in row:
        if column is None: #si pas de colone on met un - 
            print("<td>-</td>")
        else:
            print('<td>' + str(column) + "</td> </font>") #sinon on print l'intérieur de la collone
    print("</tr>")

print("</table>")
print("</center>")
print("</body>")
print("</html>")

con.close()
