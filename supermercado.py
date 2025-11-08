"""Cada producto cuesta $2.000.

Reglas:

30 unidades → 15% descuento

10 unidades → 5% descuento

Si el total después del descuento es < $50.000 → agregar $5.000 de envío
Calcular total final."""
#------------------------------------------------------------------------
print("MERCADO AHORROMAX")

unidades = int(input("Ingresa las unidades que llevas: "))
producto = 2000
descuento30unidades = 0.85
descuento10unidades = 0.95
total = producto * unidades


if unidades >= 30:
    descuento = total * descuento30unidades
elif unidades >= 10:
    descuento = total * descuento10unidades
else:
    descuento = 0
    
if descuento < 50000:
    envio = 5000
    print("El total con envio de $5000 es de:",descuento)
else:
    envio = 0
    total_final = descuento + envio
    print("El total a pagar sin costo de envio es de:",total_final)
         
    
