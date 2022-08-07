#entradas
p1=int(input("ingrese la nota del primer parcial:"))
p2=int(input("ingrese la nota del segundo parcial:"))
p3=int(input("ingrese la nota del tercer parcial:"))
ex=int(input("ingrese la nota del examen final:"))
tr=int(input("ingrese la nota del trabajo final:"))
#caja negra
pa=(p1+p2+p3)/3
total=((pa*0.55)+(ex*0.30)+(tr*0.15))
#salida
print("su nota final es: ", total)