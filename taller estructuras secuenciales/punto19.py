x=int(input("ingrese el precio por el cual compro las naranjas: "))
y=int(input("ingrese la cantidad de docenas compradas: "))
k=int(input("ingrese el precio de venta de las naranjas: "))
inversion=(x*y)/12
pgan=(k-inversion)*(100/inversion)
print("El porcentaje de ganancia es:",pgan)