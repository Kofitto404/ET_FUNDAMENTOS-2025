#modelo:    marca,    pantalla,  RAM,       disco,        GB,          procesador       video
productos = {
'8475HD': ['HP',        15.6,   '8GB',      'DD',       '1T',       'Intel Core i5',    'Nvidia GTX1050'],
'2175HD': ['lenovo',      14,   '4GB',      'SSD',      '512GB',    'Intel Core i5',    'Nvidia GTX1050'],
'JjfFHD': ['Asus',        14,   '16GB',     'SSD',      '256GB',    'Intel Core i7',   'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP',       15.6,   '8GB',      'DD',       '1T',       'Intel Core i3',    'integrada'],
'GF75HD': ['Asus',       5.6,   '8GB',      'DD',       '1T',       'Intel Core i7',    'Nvidia GTX1050'],
'123FHD': ['lenovo',      14,   '6GB',      'DD',       '1T',       'AMD Ryzen 5',      'integrada'],
'342FHD': ['lenovo',    15.6,   '8GB',      'DD',       '1T',       'AMD Ryzen 7',      'Nvidia GTX1050'],
'UWU131HD': ['Dell',    15.6,   '8GB',      'DD',       '1T',       'AMD Ryzen 3',      'Nvidia GTX1050'],
}

#modelo      precio       stock  modelo
stock = {
'8475HD':   [387990,       10, '8475HD'],
'2175HD':   [327990,        4, '2175HD'], 
'JjfFHD':   [424990,        1, 'JjfFHD'],
'fgdxFHD':  [664990,       21, 'fgdxFHD'],
'123FHD':   [290890,       32, '123FHD'],
'342FHD':   [444990,        7, '342FHD'],
'GF75HD':   [749990,        2, 'GF75HD'],
'UWU131HD': [349990,        1, 'UWU131HD'],
'FS1230HD': [249990,        0, 'FS1230HD'],
}

def stock_marca(marca):
    total = 0
    for modelo,datos in productos.items():
        if datos[0].lower()==marca.lower():
            total += stock.get(modelo,[0,0])[1]
        print(f"El stock es: {total}")

def búsqueda_precio(p_min, p_max):
    for Stocks in stock:
        if p_min <=(stock[Stocks])[0] and p_max >=(stock[Stocks])[1]:
            disp = productos.get(Stocks, [0,0]) [0]
            disp2 = stock.get(Stocks, [0,0]) [-1]
            print(f"Los equipos disponibles son:{disp}--{disp2}")            
        else:
            print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    for Stocks in stock:
        if modelo == (stock[Stocks])[-1]:
            (stock[Stocks])[0] = p
            print("Precio Actualizado")
        else:
            print(f"No se ha encontrado el modelo '{modelo}'")
        continuar = input("Desea actualizar otro precio? (s/n): ").lower()
        if continuar == "s":
            return
        elif continuar == "n":
            return
        else:
            print("Ingrese una opcion valida")

def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        opcion = input("Ingrese opción: ")

#       --- STOCK ---

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

#       --- FILTRAR POR PRECIO ---

        elif opcion == "2":
            try:
                p_min = int(input("Ingrese el minimo: "))
                p_max = int(input("Ingrese el maximo: "))
                búsqueda_precio(p_min, p_max)
            except ValueError: print("Los numeros ingresados deben ser enteros!")

#       --- ACTUALIZAR PRECIO ---
        elif opcion == "3":

            modelo = input("Ingrese modelo EXACTO ej: '8475HD' : ")
            try:
                p = int(input("Ingrese el nuevo precio: "))
            except ValueError:
                print("Ingrese un numero entero")
            actualizar_precio(modelo, p)

#       --- SALIR ---

        elif opcion == "4":
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opción válida!!")

menu()