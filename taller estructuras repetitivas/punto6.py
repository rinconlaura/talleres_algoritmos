D=int(input("dividendo:"))
d=int(input("divisor:"))
c=0
while (D>=d):
    D=D-d
    c=c+1
    r=D
print("residuo:",r)
print("cociente:",c)