a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))
d=int(input("D: "))
mi=a*1000
ce=b*100
de=c*10
u=d
N=mi+ce+de+u
print("su numero es: ",N)
if (c>=5):
  mi=a*1000
  ce=b*100
  N=mi+(ce+100)
  print("el valor redondeado es: " ,N)
else:
  mi=a*1000
  ce=b*100
  N=mi+ce
  print("el valor redondeado es: " ,N)
