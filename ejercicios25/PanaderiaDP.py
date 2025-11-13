"""1. Panadería de Don Pancho — Descuentos por cantidades
La panadería de Don Pancho vende pan a $300 cada uno.

Reglas:

Si compra más de 20 panes → 10% descuento
Si compra más de 50 panes → 20% descuento
Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
Calcular y mostrar el total."""

print("Bienvenido a la panadería de Don Pancho")

pan = 300
cantidad = int(input("Ingresa la cantidad de panes a comprar: "))

if cantidad >= 20:
    print("El costo total con un descuento de 10% es de: ",(pan * cantidad) * 0.9)
elif cantidad >= 50:
    print("El costo total con un descuento de 20% es de: ",(pan * cantidad), * 0.20)
elif cantidad <= 0:
    print("Cantidad invalida")
else:
    print("El costo total es de: ", (pan * cantidad))
