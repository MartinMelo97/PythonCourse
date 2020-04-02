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

print('Ingresa dos numeros a sumar')
numero_1 = float(input('Ingresa el primer valor: '))

numero_2 = float(input('Ingresa el segundo valor: '))

total = numero_1 + numero_2

print('El total de la suma es de:', '{:0.2f}'.format(total))