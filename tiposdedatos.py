nombre = 'Arturo'

# print('Hola, ' + nombre)

# tipos de datos
entero = 15
flotantes = 5.32151
string = 'Texto'
booleano = True

# + - * ** / // %
# operadores aritmeticos
suma = 4 + 5 # 9
resta = 5 - 4
multiplicacion = 5 * 4
potencia = 5 ** 2
division = 10 / 2
division_exacta = 5 // 2
modulo = 10 % 2
# print('El valor de tu suma es:', suma)

print('Ingresa los numeros con los que se realizaran las operaciones')
numero_1 = float(input('Ingresa el primer valor: '))

numero_2 = float(input('Ingresa el segundo valor: '))

# Suma
total = numero_1 + numero_2

print('El total de la suma es de:', '{:0.2f}'.format(total))

# Resta

total = numero_1 - numero_2

print('El total de la resta es de:', '{:0.2f}'.format(total))

# multiplicacion

total = numero_1 * numero_2

print('El total de la multiplicacion es de:', '{:0.2f}'.format(total))

# Potencia

total = numero_1 ** numero_2

print('El total de la potencia es de:', '{:0.2f}'.format(total))

# Division

total = numero_1 / numero_2

print('El total de la division (con decimales) es de:', '{:0.2f}'.format(total))

# Division exacta

total = numero_1 // numero_2

print('El total de la division (sin decimales) es de:', total)

# Modulo

total = numero_1 % numero_2

print('El residuo de la division es de:', '{:0.2f}'.format(total))