"""17. Panadería “Don Pancho” - Producción diaria
Como panadero, quiero usar un for del 1 al 12.
Si el número es 6, mostrar “Mitad de la producción completada”.
Si es 12, mostrar “¡Día finalizado!”."""

proddiaria = 0

for produccion in range(1, 13):
    proddiaria = produccion
    print(proddiaria)
    if proddiaria == 6:
        print("Mitad de la producción completada: ")
    elif proddiaria == 12:
        print("Dia finalizado")