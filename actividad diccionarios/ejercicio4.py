
n=1
estudiantes = {}
while(n<=10):
    nombre = input("Ingrese nombre: ")
    nota = float(input("Ingrese nota: "))
    print("\n")

    estudiantes[n] = {'nombre':nombre, 'nota':nota}
    n+=1

print("Lista de todos los estudiantes de la clase")
for n,d in estudiantes.items():
    print(f"Nombre: {d['nombre']} Nota = {d['nota']}")

print("\nEstudiantes Suspendidos")
for n,d in estudiantes.items():
    if(d['nota']<6.0):
        print(f"Nombre: {d['nombre']} Nota = {d['nota']}")

print("\nEstudiantes Aprobados")
for n,d in estudiantes.items():
    if(d['nota']>=6.0):
        print(f"Nombre: {d['nombre']} Nota = {d['nota']}")

print("\nNota promedio de la clase")
nota = 0
for n,d in estudiantes.items():
    nota += d['nota'] 
n=1
estudiantes = {}

while(n<=10):
    nombre = input("Ingrese nombre: ")
    nota = float(input("Ingrese nota: "))
    print("\n")

    estudiantes[n] = {'nombre':nombre, 'nota':nota}
    n+=1

print("Lista de todos los estudiantes de la clase")
for n,e in estudiantes.items():
    print(f"Nombre: {e['nombre']} Nota = {e['nota']}")

print("\nEstudiantes Suspendidos")
for n,e in estudiantes.items():
    if(e['nota']<6.0):
        print(f"Nombre: {e['nombre']} Nota = {e['nota']}")

print("\nEstudiantes Aprobados")
for n,e in estudiantes.items():
    if(d['nota']>=6.0):
        print(f"Nombre: {e['nombre']} Nota = {e['nota']}")

print("\n promedio de la clase")
nota = 0
for n,e in estudiantes.items():
    nota += e['nota'] 
print(nota/len(estudiantes))