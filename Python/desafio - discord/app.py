# Primeiro desafio, retonar a soma de dois numeros.
# def sum(a, b):
#     return a + b


# Segundo desafio, retornar a idade de anos para dias.
# def calAge(idade):
#     return idade * 365


# def points(dois, tres):
#     dois *= 2
#     tres *= 3
#     return dois + tres


def countTrue(lista):
    j = 0
    for i in lista:
        if i:
            j += 1
    return j


print(countTrue(lista=[True, False, False, True, False, True]))