# Hacer que la calculadora pueda recibir n números
# Recibir los números con un sólo input, separados por comas
# Escribe los números a jugar con ellos, separados por una coma -> 5,6,4,3,5,7
# Realizar la suma de todos los números
# Calcular el promedio de todos los números
# Calcular la multiplicación de todos los números
# Elevar cada uno de los números al cuadrado
# Calcular el factorial de cada uno de los números
# Y el factorial de la suma de todos los números
# Modularizar lo más que se pueda el código
# Y ya je

def sum_num(numeros):
    suma = 0
    for n in numeros:
        suma = suma + int(n)
    return suma

def prom_num(suma, numbers_count):
    promedio = suma/numbers_count
    return promedio

def mult_num(numeros):
    mult = 1
    for n in numeros:
        mult = mult * int(n)
    return mult

def cuadrado_n(n):
    cuad = int(n) ** 2
    return cuad

def fact_num(n):
    tope = int(n)
    fact = int(n)
    for i in range(1,tope):
        fact = fact * i
    return fact

def imp_sum(suma):
    print("El resultado de la suma es:", suma)

def imp_prom(promedio):
    print("El resultado del promedio es:", promedio)

def imp_mul(mult):
    print("El resultado de la multiplicacion es:", mult)

def imp_cuad(cuad,n):
    print(f'El resultado del cuadrado del numero {n} es: {cuad}')

def imp_fac(fact,n):
    print(f'La factorial del numero {n} es: {fact}')

def main():
    num = input('Sullivan, dame los números: ')
    numeros = num.split(',')
    suma = sum_num(numeros)
    imp_sum(suma)
    numbers_count = len(numeros)
    promedio = prom_num(suma, numbers_count)
    imp_prom(promedio)
    multiplicacion = mult_num(numeros)
    imp_mul(multiplicacion)
    for n in numeros:
        cuad = cuadrado_n(n)
        imp_cuad(cuad, n)
        fact = fact_num(n)
        imp_fac(fact, n)
    fact_suma = fact_num(suma)
    imp_fac(fact_suma, suma)

main()