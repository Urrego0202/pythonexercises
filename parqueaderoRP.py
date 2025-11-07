"""Tarifa:

0 a 5 horas: $2.000 x hora
5 horas: $2.000 x hora + multa fija de $5.000

Validar horas:

No permitir números negativos.
Mostrar valor total."""

hora = 2000
horas = int(input("Ingresa las horas que estuviste en el parqueadero: "))

if horas <= 0:
    print("Valor invalido")
elif 1 <= horas <= 4:
    totalhr = hora * horas
    print("El valor a pagar es:",totalhr)
else:
    totalhr = hora * horas + 5000
    print("El valor a pagar + multa fija ($5000) es:",totalhr)