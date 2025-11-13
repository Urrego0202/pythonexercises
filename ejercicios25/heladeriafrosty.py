"""4. Heladería “Frosty” — Sabor y topping
Sabores y precios:

chocolate → $4.000
vainilla → $3.500
Opcional: topping cuesta $1.000.

Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
Si el sabor es válido, preguntar si quiere topping y calcular total."""

#-----------------------------------------------------------------------

print ("Bienvenido a Heladería Frosty")

chocolate = 4000
vainilla = 3500
topping = 1000

sabor = input("¿Qué sabor de helado desea? (chocolate/vainilla): ").lower()

if sabor != "chocolate" and sabor != "vainilla":
    print("Sabor no disponible")
else:
    if sabor == "chocolate":
        precio = chocolate
    else:
        precio = vainilla

    print("El sabor elegido fué: ",sabor)

    opcional = input("¿Desea topping? (si/no): ").lower()    

    if opcional != "si" and opcional != "no":
        print("Respuesta no valida")
    else:
        if opcional == "si":
            precio = precio + topping 
            print("El total a pagar + topping es: ",precio) 
        else:      
            print("El total a pagar es de: ",precio)