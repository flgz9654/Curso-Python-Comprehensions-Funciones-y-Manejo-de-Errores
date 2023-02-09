
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union de Sets

set_c = set_a.union(set_b) # Metodo que permite unir sets en uno nuevo
print(set_c)

print(set_a | set_b) # Con el operador Pipe | se puede realizar la union de 2 sets.

# Interseccion de Sets

set_c = set_a.intersection(set_b) # Metodo que muestra la interseccion entre 2 sets, retorna el elemento en comun.
print(set_c)
print(set_a & set_b)

# Diferencia de Sets

set_c = set_a.difference(set_b) # Metodo que muestra los elementos diferentess de un set y otro.
print(set_c) 
print(set_a - set_b)

# Diferencia Simetrica

set_c = set_a.symmetric_difference(set_b) # Metodo que muestra los elementos que no tienen en comun ambos sets.
print(set_c)
print(set_a ^ set_b)
