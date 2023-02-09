set_countries = {'col', 'mex', 'bol', 'bol'} 

size = len(set_countries) # Realiza el conteo de los elementos de manera unica.
print(size)

print('col' in set_countries) # Se puede preguntar si un elemento esta en el set
print('pe' in set_countries) # Se puede preguntar si un elemento esta en el set

# Add element

set_countries.add('pe') # Con este metodo se puede agregar elementos al set set.add(<elem>)
print(set_countries)

# Update element

set_countries.update({'arg', 'ecua', 'pe'}) # Este metodo permite actualizar el set y sumarle uno adicional.
print(set_countries)


# Remove element

set_countries.remove('col') # Este metodo permite eliminar elementos
print(set_countries)
set_countries.remove('arg') # Si el elemento no esta genera un KeyError.
print(set_countries)

set_countries.discard('ar') # Este metodo elimnina elementos, si no esta no genera error.
print(set_countries)

set_countries.add('arg')
print(set_countries)

set_countries.pop() # Este metodo elimina un elemento aleatorio del set.
print(set_countries)

set_countries.clear() # Este metodo elimina todos los elementos y deja el set vacio.
print(set_countries)


