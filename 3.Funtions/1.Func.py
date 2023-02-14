print('Hola, mundo')

def my_print(text):
    print(text * 2)
    
my_print('Este es mi texto ')
my_print('Hola ')

a = 10
b = 90

c = a + b

def suma(a, b):
    my_print(a + b)
    
suma(45, 55)
suma(10, 4)


# _return_

def sum_whith_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum
    
result = sum_whith_range(1, 10)
print(result)

result_2 = sum_whith_range(result, result + 10)
print(result_2)

# Return and Args:

def find_volume(leng=1, width=1, depth=1):
    return leng * width * depth, width, 'Hola'

result, width, text = find_volume(width=10)
print(result)
print(width)
print(text)
