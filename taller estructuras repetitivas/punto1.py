n=int(input("N: "))
k=int(input("K: "))
c=n+1
while (k<n):
  lista=[]
  for i in range (k,c):
    lista.sort(reverse=True)
  print(lista)
  break
else:
  print("K debe ser menor que N")