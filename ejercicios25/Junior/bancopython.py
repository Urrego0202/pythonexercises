"""11. Banco “PythonBank” - Simulación de ahorro mensual
Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
Al final, mostrar el total acumulado."""

ahorromensual = 0 

for mes in range(1, 7):
    ahorro = int(input(f"Ingrese el monto ahorrado en el mes {mes}: "))
    ahorromensual += ahorro
    if ahorromensual > 1000000:
        print("¡Meta alcanzada!")
        break
        
print(f"Total acumulado: ${ahorromensual}")