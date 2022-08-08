pri=int(input("Ingrese el precio que paga por el producto: "))
prv=int(input("Ingrese el precio de venta al publico del producto: "))
total=(prv-pri)
d=(total/prv)*100
print("El porcentaje de descuento es:",d)