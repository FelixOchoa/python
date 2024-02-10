
## sumar 2 numeros

# def sumaNumeros(n1: int, n2: int):
#     return n1 + n2

# listaVacia = []
# controlador = True

# while(controlador):
#     listaVacia.append(
#         sumaNumeros(
#         int(input("Digite el primer número a sumar: ")),
#         int(input("Digite el segundo número a sumar: "))
#     )
#     )

#     for i in listaVacia:
#         if ( i == 50):
#             controlador = False
#             break


# print(listaVacia)

def sumaListas(lista: list):
    acumulador = 0

    for i in lista:
        acumulador += i

    return acumulador

def multiplicarListas(lista: list):
    acumulador = 1

    for i in lista:
        acumulador *= i
        
    return acumulador
