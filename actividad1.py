from datetime import datetime 

año_actual = datetime.now().year 

# SUELDOS BASE

sueldo_base_asalariado = 1000
sueldo_base_comisionado = 800
sueldo_base_por_horas = 8

#NOMBRE DEL EMPLEADO Y TIPO DE NÓMINA

nombre_empleado=input("Nombre del empleado:")
nómina=int(input("""Escoja el tipo de nómina:
1. Asalariado
2. Comisionado
3. Por horas
Tipo de empleado (1-3):"""))

asalariado=1
comisionado=2
por_horas=3

#SI EL EMPLEADO ES ASALARIADO:
if(nómina == asalariado):
    añocontratacion=int(input("Año de contratación:"))
    print("Empleado:",nombre_empleado)
    print("Salario:",sueldo_base_asalariado + 100*(año_actual-añocontratacion),"€")

#SI EL EMPLEADO ES COMISIONADO:
elif(nómina == comisionado):
    totalventas=int(input("Total de ventas:"))
    print("Empleado:",nombre_empleado)
    print("Salario:",sueldo_base_comisionado +10*totalventas,"€")

#SI EL EMPLEADO TRABAJA POR HORAS:
elif(nómina == por_horas):
    horas=float(input("Horas trabajadas:"))
    print("Empleado:",nombre_empleado)
    print("Salario:",sueldo_base_por_horas*horas,"€")





