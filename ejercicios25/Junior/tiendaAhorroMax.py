"""Tienda “Ahorra Más” - Caja registradora básica
Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
Si la venta supera $100,000, mostrar “Venta destacada”.
Al final, mostrar el total vendido."""

montodeventa = float(input("Ingresa el monto de venta: "))
ventatotal = 0
while montodeventa != 0:
    ventatotal  = ventatotal + montodeventa
    if montodeventa >= 100000:
        print(f"Venta destacada: {montodeventa}")
    montodeventa = float(input("Ingresa el monto de venta: "))
print(f"El total vendido fué: {ventatotal}")
#asdasd