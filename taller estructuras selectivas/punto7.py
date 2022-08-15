km=float(input("ingrese el valor de kilometros recorridos: "))
if (km<=300):
    print("debe cancelar el valor de 50000 COP")
elif (km>300 and km<1000):
  va=km-300
  vp=70000+(va*30000)
  print("el valor a pagar es: " , vp)
elif (km>1000):
  va=km-300
  vp=150000+(va*9000)
  print("el valor a pagar es: " ,vp)
