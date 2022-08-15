from cmath import sqrt
import math
a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))

d=((b**2)-(4*a*c))
if(d==0):
  x1=(-b/(2*a))
  x2=(-b/(2*a))
  print(" X1 es: " ,x1)
  print(" X1 es: " ,x2)
if(d>0):
    x2=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
    x3=(-b-sqrt((b**2)-(4*a*c)))/(2*a)
    print(" X2 es: ", x2)
    print(" X3 es: ", x3)
if(d<0):
    print("No tiene solucion en los reales")
else:
    print("Error")