price = 100 # Global

def increment():
    price = 200 # Variable local en la funcion
    result = price + 10
    # print(price)
    return result

print(price)
price2 = increment()
print(price2)


def f(x):
    return 2*x
y = f(5)
print(y)


def di_hola():
    print("Hola")

di_hola()

def di_hola(nombre):
    print("Hola", nombre)
di_hola("Juan")

# Argumentos por posición

def resta(a, b):
    return a-b

y = resta(5, 3)
print(y)

# Argumentos por nombre
# el orden ya no importa, y se podría llamar de la siguiente forma.
x = resta(a=3, b=5)
z = resta(b=5, a=3)
print(x)
print(z)

# Argumentos por defecto
def suma(a, b, c=0):
    return a+b+c
x = suma(5,5,3)
z = suma(5,5)
print(x)
print(z)

def suma(a=3, b=5, c=0):
    return a+b+c
suma() # 8
suma(1)     # 6
suma(4,5)   # 9
suma(5,3,2) # 10

def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
suma([1,3,5,4]) # 13

def suma(*numeros):
    print(type(numeros))
    # <class 'tuple'>
    total = 0
    for n in numeros:
        total += n
    return total
suma(1, 3, 5, 4) # 13
suma(6) # 6
suma(6, 4, 10) # 20
suma(6, 4, 10, 20, 4, 6, 7) # 57