lan=int(input("ingrese el valor de la lectura anterior:"))
lac=int(input("ingrese el valor de la lectura actual:"))
total=abs(lac-lan)
if (total>=0 and total<=100):
    c=(total)*4600
    print("el monto a pagar por consumo es:",c)
elif (total>=101 and total<=300):
 
    c=(total)*80000
    print("el monto a pagar por consumo es:",c)
elif (total>=301 and total<=500):
    
    c=(total)*100000
    print("el monto a pagar por consumo es:",c)
elif (total>500):
    
    c=(total)*120000
    print("el monto a pagar por consumo es:",c)


