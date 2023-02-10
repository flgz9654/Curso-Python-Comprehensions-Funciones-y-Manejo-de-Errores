# List_Comprehensions

numbers = []

for element in range(1, 11):
    numbers.append(element * 2)

# print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
# print(numbers_v2)


number = []
for i in range(1, 11):
    if i % 2 == 0:
        number.append(i * 2)
# print(number)

par = [i * 2 for i in range(1, 11) if i % 2 == 0]
# print(par)

cuadrados2 = []
for i in range(5):
    cuadrados2.append(i ** 2)

cuadrados = [i ** 2 for i in range(5)]
# print(cuadrados2)

unos = [1 for i in range(5)]
# print(unos)

lista = [10, 20, 30, 40, 50]
lista2 = [i / 10 for i in lista]
# print(lista2)

frase = 'El perro de san roque no tiene rabo'
erres = [i for i in frase if i == 'r']
# print(len(erres))


# Dictionary_Comprehensions

dicc = {}
for i in range(1, 5):
    dicc[i] = (i *  2)
# print(dicc)

dicc2 = {i : i * 2 for i in range(1, 5)}
# print(dicc2)

import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
    
population2 = {country : random.randint(1, 100) for country in countries}    

# print(population2)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
people = {names : ages for (names, ages) in zip(names,ages)}

print(people)
print(list(zip(names, ages)))  

lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
print(mi_dict)

list1 = ['Francisco', 'Paula', ' Duvan', 'Jaime']
list2 = ['Programmer', 'Comunicadora', 'Ingeniero', 'Tecnico']

prof = {i : j for (i, j) in zip(list1, list2)}
print(prof)