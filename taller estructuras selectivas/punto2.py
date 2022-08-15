sb=int(input("ingrese su sueldo base"))
t1=(sb*0.15)+sb
t2=(sb*0.12)+sb
if (sb<900000):
    print("Su sueldo final es de: ", t1)
else:
    print("Su sueldo final es de ", t2)

