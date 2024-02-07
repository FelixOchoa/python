
## Bucle FOR
frutas = ["manzana", "pera", "mango", "Guineo maduro"]

# for fruta in frutas:
#      print(fruta)

# for i in range(6):
#    print(i)

#for i in range(1, 6):
#     print(i)

# for indice, fruta in enumerate(frutas):
#     #  if ( fruta == "mango"):
#     #      print("El mango está rico")
#     #      break
#     print(indice, fruta)

#     if ( fruta == "pera"):
#         print("La pera está rica")

#     if ( fruta == "manzana"):
#         print("La manzana está rica")

# ## Bucle WHILE
# contador = 0

# while (contador <= 5):
#     if(contador != 0):
#         print("Este es el paso número", contador)
#     contador += 1

## Bucle WHILE con ELSE
# contador = 0

# while (contador < 5):

#     if( contador == 7):
#         print("Se encontró el número 3")
#         break
#     contador += 1
# else:
#     print("No se encontró el número")

# contador = 0

# switch = True

# while switch:
#     print("Este es el paso número", contador)
#     contador += 1
#     if contador == 200000:
#         print("Se hizo algo")
#         switch = False

        

# contador = 1
# listaNumeros = []

# while (contador < 10):
#     numero = int(input("Introduce un número: "))
#     listaNumeros.append(numero)
#     contador += 1

# print(listaNumeros)


intentos = 1
listaContraseñas = ["felix", "calamar", "alfredo", "gutierrez"]
contraseñaEncontrada = False

while (intentos <= 3):
    print("Intento número", intentos)
    contraseñaDigitada = input("Introduce la contraseña: ")

    for contraseña in listaContraseñas:
        if contraseñaDigitada == contraseña:
            print("¡Contraseña correcta!")
            contraseñaEncontrada = True
            break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        intentos += 1

    if(contraseñaEncontrada == True):
        break
    
else:
    print("Has agotado tus intentos. Bloqueando el acceso.")
