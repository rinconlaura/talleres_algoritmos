p=int(input("P: "))
q=int(input("Q: "))
t=((p**3)+(q**4)-(2*(p**2)))
print(t)
if (t>680):
    print("P y Q satisfacen la expresión P^3 + Q^4 - 2*P^2 > 680")
else:
    print("P y Q no Satisfacen la expresión P^3 + Q^4 - 2*P^2 > 680")
