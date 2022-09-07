usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
 }
User = input("ingrese el usuario: ")    
Pass = input("ingrese la contraseña: ") 
intentos = 3

while(User not in usuarios.keys() or Pass != usuarios[User]["password"]):
    intentos = intentos - 1
    print(f"Acceso fallido; le quedan {intentos} intentos")

    User = input("ingrese el usuario: ") 
    Pass = input("ingrese la contraseña: ")

    if intentos == 0:
        print("Acceso fallido; sin intentos")
        break 

if User in usuarios.keys() and Pass == usuarios[User]["password"]:
  if (User=="iperurena"):
    print("Iñaki Perurena")
  if (User=="fmuguruza"):
    print("Fermin Muguruza")
  if (User=="aolaizola"):
    print("Aimar Olaizola")