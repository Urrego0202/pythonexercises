"""16. Gasolinera “LoopFuel” - Control de litros vendidos
Como operador, quiero usar un while que sume litros hasta superar 100.
Cada vez que se venda una cantidad, verificar:
Si el total aún es menor que 100 → mostrar “Sigue vendiendo”.
Si llega o supera 100 → mostrar “Meta diaria alcanzada”."""


total_litros = 0

while total_litros < 100:
    litros_vendidos = int(input("Ingresa la cantidad de litros vendidos: "))
    total_litros += litros_vendidos
    if total_litros >= 100:
        print(f"Meta diaria alcanzada: {total_litros}")
    else:
        print("Sigue vendiendo")
    