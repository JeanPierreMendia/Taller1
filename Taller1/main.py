
import json
import csv

with open('Taller1/data.json', 'r') as file:
    data = json.load(file)

# Apartado 1
total = {}

for cliente in data:
    total[cliente] = 0

    for compra in data[cliente]:
        total[cliente] += compra["precio"]

for cliente in total:
    print(f"{cliente}: {total[cliente]:.2f} €")

#Apartado 2
vip = ""
mayor_gasto = 0

for cliente in total:
    if total[cliente] > mayor_gasto:
        mayor_gasto = total[cliente]
        vip = cliente

print(f"Cliente VIP: {vip}")
print(f"Total gastado: {mayor_gasto:.2f} €")

# Apartado 3
cliente_mas = ""
mayor_articulos = 0

for cliente in data:
    cantidad = len(data[cliente])

    if cantidad > mayor_articulos:
        mayor_articulos = cantidad
        cliente_mas = cliente

print(f"Cliente con más artículos: {cliente_mas}")
print(f"Cantidad de artículos: {mayor_articulos}")

# Apartado 4

mas_caro = None
mas_barato = None
cliente_caro = ""
cliente_barato = ""

for cliente in data:
    for compra in data[cliente]:

        if mas_caro is None or compra["precio"] > mas_caro["precio"]:
            mas_caro = compra
            cliente_caro = cliente

        if mas_barato is None or compra["precio"] < mas_barato["precio"]:
            mas_barato = compra
            cliente_barato = cliente


print(f"Producto más caro: {mas_caro['producto']}")
print(f"Precio: {mas_caro['precio']:.2f} €")
print(f"Cliente: {cliente_caro}")

print(f"Producto más barato: {mas_barato['producto']}")
print(f"Precio: {mas_barato['precio']:.2f} €")
print(f"Cliente: {cliente_barato}")

# Apartado 5 

categorias = {}

for cliente in data:
    for compra in data[cliente]:
        categoria = compra["categoria"]
        precio = compra["precio"]

        if categoria not in categorias:
            categorias[categoria] = precio
        else:
            categorias[categoria] += precio

for categoria in categorias:
    print(f"{categoria}: {categorias[categoria]:.2f} €")

# Apartado 6

for cliente in data:
    for compra in data[cliente]:
        compra["precioIVA"] = round(compra["precio"] * 1.21, 2)

print(data)


# Apartado 7

with open('Taller1/contabilidad_a.csv', 'w', newline='', encoding='utf-8-sig') as file:
    escritor = csv.writer(file)

    escritor.writerow(["producto", "precioIVA"])

    for cliente in data:
        for compra in data[cliente]:
            escritor.writerow([compra["producto"], compra["precioIVA"]])

print("Archivo CSV creado correctamente")