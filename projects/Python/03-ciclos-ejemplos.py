# Operaciones con elemntos de una lista: Elementos cudrados. - For
# Interacción con el usuario - While
# Contar hacia atrás - While
# Sumar números hasta un límite - While
# Sumar números hasta un límite - For


# listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for numero in listaNumeros:
#     print("El cuadrado del número: ", numero, " es: ", numero ** 2)

# respuesta = True

# while ( respuesta ):
#     pregunta = input("¿Desea continuar con el programa: S/N")

#     if ( pregunta == "n"):
#         respuesta = False
#     if ( pregunta != "n" and pregunta != "s"):
#         print("Respuesta incorrecta. Por favor Intente de nuevo")

# while ( True ):
#     pregunta = input("¿Desea continuar con el programa: S/N")
    
#     if ( pregunta == "n"):
#         break

limite = int(input("Por favor. Digite el límite del ejercicio: "))
acumulador = 0

while ( acumulador < limite):
    nuevoNumero = int(input("Por favor digite un número: "))

    acumulador += nuevoNumero

print("El límite es: ", limite)
print("El acumulador fue: ", acumulador)