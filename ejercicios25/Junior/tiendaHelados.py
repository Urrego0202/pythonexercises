"""19. Tienda de helados - Registro de clientes atendidos
Como empleado, quiero usar un while que cuente clientes hasta que el número supere 15.
Si el número es múltiplo de 5, mostrar “Pausa para limpieza”.
Al final, mostrar “Turno finalizado”."""

contador = 0

while contador < 15:
    contador += 1
    if contador % 5:
        print(f"Cliente número: {contador}")
    else:
        print("Pausa para limpieza")
print("Turno finalizado")
