import math
dinero=float(input("Introduzca la cantidad a ingresar (€):"))
while dinero<0:
    dinero = int(input("Introduzca la cantidad a ingresar (la cantidad a ingresar debe ser positiva):"))
print("---------------------------------------------------------------------------")

interes=float(input("Introduzca el tipo de interés (%):"))
while interes<0:
    interes=float(input("Introduzca el tipo de interés (La cantidad a ingresar debe ser positiva):"))
print("---------------------------------------------------------------------------")

años=int(input("Introduzca los años:"))
while años<0:
    años=int(input("Introduzca los años (los años de depósito deben especificarse con un número positivo):"))
print("---------------------------------------------------------------------------")

total1=(1+(interes/100))
total2=pow(total1,años)
total3=dinero*total2

print("Ingreso:",f'{dinero:.2f}',"€")
print("Interés:",interes,"%")
print("Años:",años)
print("Total:",f'{total3:.2f}',"€")
