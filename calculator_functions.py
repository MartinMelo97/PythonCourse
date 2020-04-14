def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multiplicacion(num1, num2):
  return num1 * num2

def division(num1, num2):
  return num1 / num2

def division_exacta(num1, num2):
  return num1 // num2

def elevar_cuadrado(num1):
  return num1 ** 2

def print_values(name, value):
  print(f'El resultado de la {name} es: {value}')

def get_number(num):
  return float(input(f'Dame el numero {num}: '))

def main():
  num1 = get_number(1)
  num2 = get_number(2)
  sumaa = suma(num1, num2)
  restaa = resta(num1, num2)
  multi = multiplicacion(num1, num2)
  divi = division(num1, num2)
  divi_exacta = division_exacta(num1, num2)
  num1_cuadrado = elevar_cuadrado(num1)
  num2_cuadrado = elevar_cuadrado(num2)

  print_values('suma', sumaa)
  print_values('resta', restaa)
  print_values('multiplicación', multi)
  print_values('división', divi)
  print_values('división exacta', divi_exacta)
  print_values('elevación del numero uno al cuadrado', num1_cuadrado)
  print_values('elevación del numero dos al cuadrado', num2_cuadrado)

main()
