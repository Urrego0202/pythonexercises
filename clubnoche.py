"""Pedir edad y documento.

Reglas:

Edad ≥ 18 → puede entrar solo si tiene documento.
Si la edad < 18 → "Entrada denegada"
Si tiene 18 o más pero no tiene documento → "Debe presentar documento"""
#------------------------------------------------------------------------------

edad = int(input("Ingresa tu edad: "))
documento = input("Tienes documento (si/no): ").lower()

if edad >= 18:
    if documento == "si":
        print("Puedes entrar al club")
    else:
        print("Debe presentar documento")
else:
    print("Entrada denegada")