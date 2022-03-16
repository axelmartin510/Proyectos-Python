import sqlite3

def talla(ingreso):
    ingreso = ingreso.upper()
    while ingreso != "L" and ingreso != "M" and ingreso != "XL":
        ingreso = input("Error de campo: ")
    ingreso = ingreso.upper()
    return ingreso

def verificar(ingreso):
    while not ingreso.isdecimal():
        ingreso = input("Error de campo: ")
    ingreso = int(ingreso)
    return ingreso

conn = sqlite3.connect("articles.sqlite")
cur = conn.cursor()

selectall = "SELECT name, price, color, size FROM articles ORDER BY name ASC"

while True:

    print("""
    1 - Ver productos 
    2 - Combo completo
    3 - Combos personalizados
    4 - Cerrar programa
    """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        for x in cur.execute(selectall):
            print("\n",x[0], x[2], "talle", x[3], "$", x[1])

    if opcion == "2":
        talle = input("Seleccione su talle (M - L - XL): ")
        talle = talla(talle)

        print("Su combo es el siguiente: ")
        for row in cur.execute("SELECT name, price, color FROM articles WHERE size = ? ORDER BY name ASC" ,(talle,)):
            print(row[0], "-", row[2], "-", "$", row[1])

        precio = cur.execute("SELECT SUM(price) FROM articles WHERE size = ?" ,(talle,))
        for row in precio:
            print("\nEl precio total es: $", str(row).strip(",()"))

    if opcion == "3":
        talle = input("Seleccione su talle (M - L - XL): ")
        talle = talla(talle)

        cantidades = {}

        shorts = input("Seleccione la cantidad de shorts: ")
        shorts = verificar(shorts)
        cantidades["Short"] = shorts
        buzos = input("Seleccione la cantidad de buzos: ")
        buzos = verificar(buzos)
        cantidades["Buzo"] = buzos
        remeras = input("Seleccione la cantidad de remeras: ")
        remeras = verificar(remeras)
        cantidades["Remera"] = remeras
        jeans = input("Seleccione la cantidad de jeans: ")
        jeans = verificar(jeans)
        cantidades["Jean"] = jeans
        zapatillas = input("Seleccione la cantidad de zapatillas: ")
        zapatillas = verificar(zapatillas)
        cantidades["Zapatillas"] = zapatillas

        precio = 0
        data_acum = []

        for x in cantidades:
            query = cur.execute("SELECT price * ? FROM articles WHERE size = ? AND name = ?", (cantidades[x], talle, x,))
            data = cur.fetchone()
            precio += int(str(data[0]).strip("(),"))
        
        print("\nSu combo es el siguiente: ")
        for x in cantidades:
            cur.execute("SELECT price FROM articles WHERE size = ? AND name = ?", (talle, x,))
            print(cantidades[x], x, "de $", int(str(cur.fetchone()).strip("(),")))
        print("\nEl precio total es: $", precio)

    if opcion == "4":
        print("Gracias por utilizar el programa!")
        break

    else:
        continue
        






