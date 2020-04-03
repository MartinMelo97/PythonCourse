# El usuario ingrese el precio de su producto
# Se le muestre al final el valor del IVA
# Mostrarle al usuario el total del precio original + IVA
# Valor del IVA = 0.16

print('Vamos a calcular el IVA de tu producto')

# Obteniendo el precio
precio = float(input('Ingresa el precio de tu producto: '))

# Calculando el IVA
iva = precio * 0.16

# Calculando el total
total = precio + iva

# Mostrando el IVA

print('El valor del IVA es de:', iva)
print('El precio de tu producto mas IVA es de:', total)