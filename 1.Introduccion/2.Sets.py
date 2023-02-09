set_countries = {'col', 'mex', 'bol', 'bol'} # los sets no admiten elementos duplicados, estos se eliminan al imprimirlos
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12} # los sets no tienen un orden definido, cada vez que se imprime este cambia.
print(set_types)

set_from_string = set('hola') # los set se pueden crear a partir de strings
print(set_from_string)

set_from_list = set([5, 4, 6, 8, 8, 1]) # los sets se pueden crear a partir de listas.
print(set_from_list)  
print(type(set_from_list))

set_from_tuple = set(('abc', 'cbv', 'as', 'abc')) # los sets se pueden crear a partir de tuplas.
print(set_from_tuple)

numbers = [1,2,3,1,2,3,4] 
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers) # Puedes transformar un set a una lista y asi tener los numeros unicos.
print(unique_numbers)
