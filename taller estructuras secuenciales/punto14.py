lan=int(input("ingrese el valor de la lectura anterior:"))
lac=int(input("ingrese el valor de la lectura actual:"))
kl=int(input("ingrese el costo del kilovatio:"))
total= (lac-lan)*kl
total1= (lan-lac)*kl
if lac > lan:
    print("el monto a pagar por consumo es:",total)
elif lac < lan:
    print("el monto a pagar por consumo es:",total1)
