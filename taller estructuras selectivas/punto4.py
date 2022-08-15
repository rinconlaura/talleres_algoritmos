mc=int(input("ingrese el monto de la compra: "))
if (mc>5000000):
    ip=mc*0.55
    pb=mc*0.30
    cf=mc*0.15
    i=cf*0.20
    print(" la inversión de los fondos de la empresa es de: ", ip)
    print(" El Prestamo del banco es de: ",pb)
    print("El valor del credito es de: ",cf)
    print(" El monto a pagar por Intereses del fabricante es de: ", i)
elif (mc<=5000000):
    ip=mc*0.70
    cf=mc*0.30
    i=cf*0.20
    print(" la inversión de los fondos de la empresa es de: ", ip)
    print("El valor del credito es de: ",cf)
    print(" El monto a pagar por Intereses del fabricante es de: ", i)
  