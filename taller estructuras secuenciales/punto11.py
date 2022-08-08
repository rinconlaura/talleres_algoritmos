nom=str(input("ingrese su nombre:"))
hn=int(input("ingrese la cantidad de horas normales trabajadas:"))
hx=int(input("ingrese la cantidad de horas extra trabajadas:"))
ph=int(input("ingrese el valor del pago por hora normal trabajada:"))
s=ph*hn
ht=(ph*hx)*0.25
pt=s+ht
pf=s*0.05
poh=s*0.02
ca=s*0.07
d=pf+poh+ca
a=250000+173000+180000
sn=pt+a-d
print("las asignaciones totales son:",a)
print("las deducciones totales son:",d)
print("el sueldo neto es:",sn)