t=float(input("ingrese su temperatura :"))

if(t>85 and t<=100):
  print("el deporte apropiado para practicar es natacion")
elif(t>71 and t<=85):
  print("el deporte apropiado para practicar es Tenis")
elif(t>33 and t<=70):
  print("el deporte apropiado para practicar es golf")
elif(t>11 and t<=32):
  print("el deporte apropiado para practicar es Esqui")
elif(t<=10):
  print("el deporte apropiado para practicar es Marcha")
else:
  print("la temperatura no se adapta a ningun deporte")