"""18. Academia de inglés - Repetición de palabras
Como estudiante, quiero ingresar una palabra y usar un for para repetirla 5 veces.
Si el contador es impar, mostrar la palabra en minúsculas.
Si es par, mostrarla en mayúsculas."""

palabrastudent = str(input("Ingresa la palabra: "))

for contador in range(1,6):
    contador += 1
    if contador % 2 == 0:
        print(palabrastudent.upper())
    else:
        print(palabrastudent.lower())