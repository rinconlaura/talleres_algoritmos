s=int(input("ingrese el valor del sueldo base: "))
da=int(input("ingrese el valor de las ventas del deparamento a:"))
db=int(input("ingrese el valor de las ventas del deparamento b:"))
dc=int(input("ingrese el valor de las ventas del deparamento c:"))
vt=(da+db+dc)
print("el valos de las ventas totales es de: ", vt)
va=vt*0.33

if(da>va):
    t=(s*0.20)+s
    print("el valor del sueldo de los vendedores del departamento a es de: ",t)
else:
    print("el valor del sueldo de los vendedores del departamento a es: ",s )       
if(db>va):
    t=(s*0.20)+s
    print("el valor del sueldo de los vendedores del departamento b es de: ",t)
else:
    print("el valor del sueldo de los vendedores del departamento b es: ",s )   
if(dc>va):
    t=(s*0.20)+s
    print("el valor del sueldo de los vendedores del departamento c es de: ",t)
else:
    print("el valor del sueldo de los vendedores del departamento c es: ",s )   
