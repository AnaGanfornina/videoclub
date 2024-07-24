import sqlite3, csv

def rows_to_dictlist(filas,nombres_columna):
    registros = []
    for fila in filas:
        registro = {}
  
        for i, nombre in enumerate(nombres_columna):
            registro [nombre] = fila [i]  #Así se crea un diccionario
        registros.append(registro)

    return registros



#Abrir la conexion

con = sqlite3.connect ("data/peliculas.sqlite")
#crear cursor

cur = con.cursor()

# Uso el cursos con sql en forma de cadena

cur.execute("select id, nombre, url_foto, url_web from directores where url_foto is NOT NULL")

colums_description = cur.description


nombres_columna = []
for columna in columns_description:
    nombres_columna.append (columna [0])

lista = list (map (lambda item: item[0], columns_description))

# Proceso la respuesta si la hubiera (un select)

rows = cur.fetchall()

#hacer una función que me transforme la lista de tuplas resul, en una lista   
#de diccionarios como las que devuelve el dict reader
resultado  = rows_to_dictlist(rows,nombres_columna)

print (resultado)

#cerrar la conexión siempre
con. close ()

"""
#Ejercicio clase__________________________

#Abrir la conexion

con = sqlite3.connect ("data/peliculas.sqlite")
#crear cursor

cur = con.cursor()

# Uso el cursos con sql en forma de cadena

cur.execute("select id, nombre, url_foto, url_web from directores")

result = cur.fetchall()
description = ["id","nombre", "url_fot0¡o","url_web"]
lista = []
for item in result:
    registro = {}
  
    for i, clave in enumerate(description):
        description [clave] = item [i]  #Así se crea un diccionario
    lista.append(registro)
return lista

"""