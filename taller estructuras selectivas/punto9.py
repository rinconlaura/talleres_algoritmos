n=str(input("ingrese su nombre:"))
mc=int(input("ingrese el monto de su compra:"))
print(n)
print("el monto de la compra es:", mc)
if (mc<50000):
    print("no hay descuento")
elif (mc>=50000 and mc<=100000):
    t=mc-(mc*0.05)
    print("el descuento es del 5%")
    print("el monto a pagar es de: ",t)
elif (mc>=100000 and mc<=700000):
    t=mc-(mc*0.11)
    print("el descuento es del 11%")
    print("el monto a pagar es de: ",t)
elif (mc>=700000 and mc<=1500000):
    t=mc-(mc*0.18)
    print("el descuento es del 18%")
    print("el monto a pagar es de: ",t)
elif (mc>1500000):
    t=mc-(mc*0.25)
    print("el descuento es del 25%")
    print("el monto a pagar es de: ",t)



