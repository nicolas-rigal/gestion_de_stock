import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nicolas',
    database = 'boutique'
    )


cursor = bd.cursor()

req = 'SELECT produit.nom, catégorie.nom AS catégorie_nom FROM produit INNER JOIN catégorie ON produit.id_catégorie = catégorie.id'
cursor.execute(req)
datas = cursor.fetchall()
print(datas)
cursor.close()