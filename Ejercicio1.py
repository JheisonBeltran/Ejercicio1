# -*- coding: utf-8 -* -
"""
Created on Sun Feb 28 16:10:30 2021

@author: Jbeltrant
"""

print("Hola Jheison")
print("Hola Mundo Jheison")

# EJERCICIO 1

Primer_inversion = float(input("Digite el valor a invertir #1: "))
Segundo_inversion = float(input("Digite el valor a invertir #2: "))
Tercero_inversion = float(input("Digite el valor a invertir #3: "))
Total_inversion = Primer_inversion + Segundo_inversion + Tercero_inversion
print("Total inversion: ")
print(Total_inversion)
Total_inversion1 = Primer_inversion / Total_inversion
Total_inversion11 = Total_inversion1 * 100
print("Inversionista 1: ")
print(Total_inversion11)
Total_inversion2 = Segundo_inversion / Total_inversion
Total_inversion22 = Total_inversion2 * 100
print("Inversionista 2: ")
print(Total_inversion22)
Total_inversion3 = Tercero_inversion / Total_inversion
Total_inversion33 = Total_inversion3 * 100
print("Inversionista 3: ")
print(Total_inversion33)

# EJERCICIO 2
Pago_Basico = float(input("Digite el sueldo basico: "))
Num_Hijos = float(input("Digite el # de hijos: "))
Total_Bono = Num_Hijos * 80000
print("Bonificación del empleado: ")
print(Total_Bono)
Total_Pago = Total_Bono + Pago_Basico
print("Total valor a pagar al empleado: ")
print(Total_Pago)

# EJERCICIO 3
Pago_Basico = float(input("Digite el saldo incial: "))
Interes_1 = Pago_Basico * 0.15
Total_conInteres = Interes_1 + Pago_Basico
print("Intereses ahorrados:")
print(Interes_1)
print("Soldo más interes:")
print(Total_conInteres)

# EJERCICIO 4
Num_m4 = float(input("Digite el # de metro cuadrado: "))
Total_m4 = Num_m4 * 80000
Cuota_Inicial = Total_m4 * 0.35
Saldo_Pendiente = Total_m4 - Cuota_Inicial
Num_Cuotas = 12
Saldo_Cuotas = Saldo_Pendiente / Num_Cuotas
print("Valor total por metro cuadrado: ")
print(Total_m4)
print("Valor cuota inicial es: ")
print(Cuota_Inicial)
print("Valor penidnete a pagar es: ")
print(Saldo_Pendiente)
print("Valor por cuota es: ")
print(Saldo_Cuotas)

# EJERCICIO 5
Sueldo_Base = float(input("Digite el sueldo base: "))
Dto_Ley = Sueldo_Base * 0.01
Dto_SSocial = Sueldo_Base * 0.04
Dto_SForzoso = Sueldo_Base * 0.005
Dto_CAhorro = Sueldo_Base * 0.05
Total_Pago = Sueldo_Base - Dto_CAhorro - Dto_Ley - Dto_SForzoso - Dto_SSocial
print("Descuento Ley de politica publica: ")
print(Dto_Ley)
print("Descuento Seguro social: ")
print(Dto_SSocial)
print("Descuento Seguro forzoso: ")
print(Dto_SForzoso)
print("Descuento Caja ahorro: ")
print(Dto_CAhorro)
print("Total a pagar: ")
print(Total_Pago)

# EJERCICIO 6
Num_palabras = float(input("Digite el # de palabras: "))
Num_cm = float(input("Digite el # de cm: "))
Num_colores = float(input("Digite el # de colores: "))
Valor_palabras = Num_palabras * 20000
Valor_cm = Num_cm * 15000
Valor_colores = Num_colores * 25000
Total_Pago = Valor_palabras + Valor_cm + Valor_colores
print("Valor total por palabras: ")
print(Valor_palabras)
print("Valor total por cm: ")
print(Valor_cm)
print("Valor total por colores: ")
print(Valor_colores)
print("Total a pagar: ")
print(Total_Pago)

# EJERICIO 7
Num_años = float(input("Digite el # de años labordos: "))
Años_Trabajados = (Num_años * 120000) - 20000
Año_Trabajado = 100000
if (Num_años >= 2):
    print(Años_Trabajados)
else:
    print(Año_Trabajado)


# EJERCICIO 8
Sueldo_Base = float(input("Digite el sueldo base por hora: "))
Sueldo_BaseTotal = Sueldo_Base * 20000
Dto_CAhorro = Sueldo_BaseTotal * 0.05
Total_Pago = Sueldo_BaseTotal - Dto_CAhorro
print("Descuento Caja ahorro: ")
print(Dto_CAhorro)
print("Total a pagar: ")
print(Total_Pago)

# EJERCICIO 9
Monto_Inicial = float(input("Digite el monto inicial: "))
Monto_Final = float(input("Digite el monto final: "))
Monto_Base = Monto_Final - Monto_Inicial
Recargo = Monto_Base * 0.2
Monto_Base_Total = Monto_Base + Recargo
print("Valor de recargo: ")
print(Recargo)
print("Total a pagar: ")
print(Monto_Base_Total)

# EJERCICIO 10
Num_Foto = float(input("Digite el # de fotos a revelar: "))
Valor_Base = Num_Foto * 1500
Valor_Iva = Valor_Base * 0.16
Valor_Total = Valor_Base + Valor_Iva
print("Valor de IVA: ")
print(Valor_Iva)
print("Valor_Total: ")
print(Valor_Total)

# EJERCICIO 11
Presupuesto = float(input("Digite el monto presupuestal: "))
Ptto_Ginecología = Presupuesto * 0.4
Ptto_Traumatología = Presupuesto * 0.3
Ptto_Pediatría = Presupuesto * 0.3
print("Valor ptto Ginecología: ")
print(Ptto_Ginecología)
print("Valor ptto Traumatología: ")
print(Ptto_Traumatología)
print("Valor ptto Pediatría: ")
print(Ptto_Pediatría)

# EJERCICIO 12
Num_Peliculas = float(input("Digite el # de peliculas para alquiler: "))
Num_Días = float(input("Digite el # días: "))
Valor_Peliculas = Num_Peliculas * Num_Días
Valor_Total = (Valor_Peliculas * 1500) - 1500
print("Total a pagar: ")
print(Valor_Total)

# EJERCICIO 13
Num_Personas = float(input("Digite el # personas: "))
Num_Días = float(input("Digite el # días: "))
Valor_Viaje = (Num_Personas * Num_Días) * 25000
Valor_Iva = Valor_Viaje * 0.12
Valor_Total = Valor_Viaje + Valor_Iva
print("Total IVA: ")
print(Valor_Iva)
print("Total a pagar: ")
print(Valor_Total)

# EJERCICIO 14
Num_días = float(input("Digite el # de días en hotel: "))
Días_Estadía = (Num_días * 200000) - 100000
Día_Estadía = 100000
if (Num_días >= 2):
    print(Días_Estadía)
else:
    print(Día_Estadía)

# EJERCICIO 15
Prestamo = float(input("Digite el monto del prestamo: "))
Intereses = Prestamo * 0.24
P_Interes = Prestamo + Intereses
C_Especial = P_Interes / 2
Cuota_Especial = C_Especial / 4
Cuota_ordinarias = C_Especial / 20
print("Prestamos + Intereses es: ")
print(P_Interes)
print("Valor cuotas especiales: ")
print(Cuota_Especial)
print("Valor cuotas ordinarias: ")
print(Cuota_ordinarias)
