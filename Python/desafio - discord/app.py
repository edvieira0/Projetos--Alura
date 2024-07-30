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


# def countTrue(lista):
#     j = 0
#     for i in lista:
#         if i:
#             j += 1
#     return j

# def countTrue(lst):
#   return len([value for value in lst if value])


def fibonaccin(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a + b

print(fibonaccin(10))