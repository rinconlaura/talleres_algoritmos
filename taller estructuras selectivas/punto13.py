from datetime import date
today=date.today()
añoa=today.year
mesa=today.month
diaa=today.day


fn =(input ("ingrese año mes y dia de su nacimiento: " ))
(añon,mesn,dian)=fn.split(" ")
añon=int(añon)
mesn=int(mesn)
dian=int(dian)
edad=0
if(mesn==mesa):
    if(dian>=diaa):
        edad=(añoa-añon)-1
    else:
        edad=(añoa-añon)
elif (mesn<mesa):
    edad=(añoa-añon)
else:
    edad=(añoa-añon)-1

signo=""

if (dian>=21 and mesn==1) or (dian<=19 and mesn==2):
    signo="acurio"
if (dian>=20 and mesn==2) or (dian<=20 and mesn==3):
    signo="piscis"
if (dian>=21 and mesn==3) or (dian<=20 and mesn==4):
    signo="aries"
if (dian>=21 and mesn==4) or (dian<=21 and mesn==5):
    signo="tauro"
if (dian>=22 and mesn==5) or (dian<=21 and mesn==6):
    signo="geminis"
if (dian>=22 and mesn==6) or (dian<=22 and mesn==7):
    signo="cancer"
if (dian>=23 and mesn==7) or (dian<=23 and mesn==8):
    signo="leo"
if (dian>=24 and mesn==8) or (dian<=22 and mesn==9):
    signo="virgo"
if (dian>=23 and mesn==9) or (dian<=22 and mesn==10):
    signo="libra"
if (dian>=23 and mesn==10) or (dian<=21 and mesn==11):
    signo="escorpio"
if (dian>=22 and mesn==11) or (dian<=21 and mesn==12):
    signo="sagitario"
if (dian>=22 and mesn==12) or (dian<=20 and mesn==1):
    signo="capricornio"

print(signo)
print(edad)

