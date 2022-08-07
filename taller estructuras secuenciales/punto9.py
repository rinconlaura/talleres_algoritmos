#entradas
horas=int(input("ingrese la cantidad de horas trabajadas:"))
pagoh=int(input("ingrese el precio de la hora:"))


#caja negra
s=(horas*pagoh)
sn=s*0.2
total=s-sn
#salida
print("su sueldo neto es: ", total)