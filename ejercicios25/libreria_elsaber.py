"""Libro cuesta $25.000.

Si es estudiante → 15% descuento
Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
Validar:

Si no es estudiante, el cupón no aplica.
Si ingresa cupón incorrecto, ignorarlo.
Mostrar total."""
#---------------------------------------------------------------
print("LIBRERÍA EL SABER")

libro = 25000
esestudiante = input("Eres estudiante (si/no): ").lower()

if esestudiante == "si":
    precio = libro * 0.85
    cupon = input("Ingresa el cupón (En caso de no tener, presiona la tecla ENTER): ")
    if cupon == "LIBRO10":
        precio = precio * 0.9
        print("El costo total con descuento de cupón: ")
    else:
        print("Cupón no valido")
else:
    precio = libro
print("El valor del libro es: ",precio)
    
    
