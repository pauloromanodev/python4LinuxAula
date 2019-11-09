from functools import reduce

#list comprehension

#lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = []

#nova_lista = [x * x for x in lista if x % 2 == 0]

for x in range(1,10):
    lista += [x]

nova_lista = [x + 2 for x in lista]

print(nova_lista)

quadrado = lambda x: x*x

print(quadrado(2))

print(type(quadrado))
