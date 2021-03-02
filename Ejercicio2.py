# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:24:41 2021

@author: Jbeltrant
"""

# TALLER ALGORITMO CONDICIONALES
# EJERCICIO 1
Num_Camisas = float(input("Digite el número camisas: "))
Valor_Camisa = float(input("Digite el valor de la camisa: "))
Valor_Parcial = Num_Camisas * Valor_Camisa
Primer_Descuento = (Num_Camisas * Valor_Camisa) * 0.3
Costo_Desceunto1 = Valor_Parcial - Primer_Descuento
Segundo_Descuento = (Num_Camisas * Valor_Camisa) * 0.1
Costo_Desceunto2 = Valor_Parcial - Segundo_Descuento
print("Valor a pagar: ")
if (Num_Camisas >= 3):
    print(Costo_Desceunto1)
else:
    print(Costo_Desceunto2)

# EJERCICIO 2
Num_Azar = float(input("Digite el número obtenido: "))
Valor_Compra = float(input("Digite el valor de la compra: "))
Primer_Descuento = Valor_Compra * 0.15
Costo_Desceunto1 = Valor_Compra - Primer_Descuento
Segundo_Descuento = Valor_Compra * 0.20
Costo_Desceunto2 = Valor_Compra - Segundo_Descuento
print("Valor a pagar: ")
if (Num_Azar >= 74):
    print(Costo_Desceunto2)
else:
    print(Costo_Desceunto1)

# EJERCICIO 3
Valor_Monto = float(input("Digite el valor del monto asegurar: "))
Primer_porcentaje = Valor_Monto * 0.03
Costo_Valor1 = Valor_Monto + Primer_porcentaje
Segundo_porcentaje = Valor_Monto * 0.02
Costo_Valor2 = Valor_Monto + Segundo_porcentaje
print("Valor a pagar: ")
if (Valor_Monto < 50000):
    print(Costo_Valor1)
else:
    print(Costo_Valor2)

# EJERCICIO 4
Num_Puntos = float(input("Digite el número de puntos de contaminación: "))
Valor_Ganancia = float(input("Digite el valor de ganancias de esta semana: "))
Total_Conteo = Num_Puntos / 5
Con_Multa = Valor_Ganancia * 0.5
Total_1 = Valor_Ganancia - Con_Multa
Sin_Multa = Valor_Ganancia * 0
Total_2 = 0
if (Num_Puntos > 170):
    print("Multa a pagar: ")
    print(Total_1)
else:
    print("Multa a pagar: ")
    print(Total_2)

# EJERCICIO 5
Valor_comercial = float(input("Digite el valor del automóvil o terreno: "))
Porcentaje1 = float(input("Digite el % devaluado del automovil en 3 años: "))
Porcentaje2 = float(input("Digite el % Avaluado del terreno en 3 años: "))
Valor_Devaluo = Porcentaje1 / 100
Valor_Avaluo = Porcentaje2 / 100
Valor_Devaluo1 = Valor_comercial * Valor_Devaluo
Valor_Avaluo1 = Valor_comercial * Valor_Avaluo
Valor_Total_Avaluo = Valor_Avaluo1 / 2
if (Valor_Devaluo1 > Valor_Total_Avaluo):
    print("Debe comprar el auotomóvil")
else:
    print("Debe comprar el terreno")

# EJERCICIO 6
Cantidad = float(input("Digite la cantidad de computadoras compradas: "))
Valor = Cantidad * 11000
Descuento1 = Valor * 0.10
Valor_Descuento1 = Valor - Descuento1
Descuento2 = Valor * 0.20
Valor_Descuento2 = Valor - Descuento2
Descuento3 = Valor * 0.40
Valor_Descuento3 = Valor - Descuento3
if (Cantidad < 5):
    print("Valor a pagar con descuento del 10% es: ")
    print(Valor_Descuento1)
elif (Cantidad > 10):
    print("Valor a pagar con descuento del 20% es: ")
    print(Valor_Descuento2)
else:
    print("Valor a pagar con descuento del 40% es: ")
    print(Valor_Descuento3)

# EJERCICIO 7
Valor = int(input('Digite el precio del aparato a comprar  : '))
Marca = input('Digite la marca del aparato: ')
if Valor >= 2000 and Marca.lower() == 'nosy':
    Total_Descuento = Valor - (Valor * 0.10) - (Valor * 0.05)
    Total_IVA = Total_Descuento + (Total_Descuento * 0.16)
    print(f' Total: {Total_IVA}')
elif Valor >= 2000:
    Total_Descuento = Valor - (Valor * 0.10)
    Total_IVA = Total_Descuento + (Total_Descuento * 0.16)
    print(f' Total: {Total_IVA}')
elif Marca.lower() == 'nosy':
    Total_Descuento = Valor - (Valor * 0.05)
    Total_IVA = Total_Descuento + (Total_Descuento * 0.16)
    print(f' Total: {Total_IVA}')
else:
    print(f' Total: {Valor}')

# EJERCICIO 8
Valor_Compra = float(input('Digite el monto total de la compra : '))
if Valor_Compra > 500000:
    Dinero_Propio = Valor_Compra * 0.55
    Prestamo_Banco = Valor_Compra * 0.30
    Prestamo_Fabricante = Valor_Compra * 0.15
    Intereses = Prestamo_Fabricante * 0.20
    print(f' Cantidad a invertir: {Dinero_Propio}')
    print(f' Valor del prestamo del banco: {Prestamo_Banco}')
    print(f' Valor del credito al fabricante: {Prestamo_Fabricante}')
    print(f' Intereses causados: {Intereses}')
elif Valor_Compra <= 500000:
    Dinero_Propio = Valor_Compra*0.70
    Prestamo_Fabricante = Valor_Compra * 0.30
    Intereses = Prestamo_Fabricante * 0.20
    print(f' Cantidad a invertir: {Dinero_Propio}')
    print(f' Valor del credito al fabricante: {Prestamo_Fabricante}')
    print(f' Intereses causados: {Intereses}')

# EJERCICIO 9
Recoletar_n1 = float(input('Digite el primer número : '))
Recoletar_n2 = float(input('Digite el segundo número : '))
if Recoletar_n1 == Recoletar_n2:
    Resultado1 = Recoletar_n1 * Recoletar_n2
    print(f' Total: {Resultado1}')
elif Recoletar_n1 > Recoletar_n2:
    Resultado2 = Recoletar_n1 - Recoletar_n2
    print(f' Total: {Resultado2}')
elif Recoletar_n1 < Recoletar_n2:
    Resultado3 = Recoletar_n1 + Recoletar_n2
    print(f' Total: {Resultado3}')

# EJERCICIO 10
Recoletar_n1 = float(input('Digite el primer número : '))
Recoletar_n2 = float(input('Digite el segundo número : '))
Recoletar_n3 = float(input('Digite el tercer número : '))
if Recoletar_n1 > Recoletar_n2 and Recoletar_n1 > Recoletar_n3:
    print(f'El mayor numero es el : {Recoletar_n1}')
elif Recoletar_n2 > Recoletar_n1 and Recoletar_n2 > Recoletar_n3:
    print(f'El mayor numero es el : {Recoletar_n2}')
elif Recoletar_n3 > Recoletar_n1 and Recoletar_n3 > Recoletar_n2:
    print(f'El mayor numero es el : {Recoletar_n3}')

# JABT
