#entradas
v1=int(input("ingrese el valor de la primera venta:"))
v2=int(input("ingrese el valor de la segunda venta:"))
v3=int(input("ingrese el valor de la tercera venta:"))
s=int(input("ingrese el valos de su sueldo:"))
#caja negra
comision=(v1+v2+v3)*0.1
total=s+comision
#salida
print("su sueldo total incluyendo la comision por ventas es: ", total)