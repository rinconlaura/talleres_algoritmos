
inversion=int(input("ingrese la cantidad invertida"))
tasa=float(input("ingrese la tasa de interes"))
total=(inversion*tasa)
saldo=inversion+total
if (total>100000):
    print("La ganancia por intereses es de: ", total)
else:
    print("la ganancia por intereses no supera los 100000")
print("en la cuenta tiene un total de: ", saldo)
