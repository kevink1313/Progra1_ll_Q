# Como funcionan las estructuras de control
saludo = False

if saludo:
    print("hola mundo")
else:
    print("no hay saludos")

respuesta = "lagarto"
if respuesta != "lagarto":
    print("me gusta el Lagarto asado")
else:
    print("No me gusta")

edad = 15
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

nota = 30

if nota < 60:
    print("El estudiante se quedó")
elif nota <  70:
    print("El alumno se fue a penales")
else:
    print("El alumno paso el año")

print("//////////////////")

# Vamos a realizar ejemplos de bucles 
# variables de control

num1 = 1
num1 += 1
print(num1)


# Bucle mientras o while
Control = True

while Control == True:
    print(num1)
    num1 += 1
    if num1 == 101:
        Control = False



Contador = 0
num2 = 1
online = True
while Contador < 100 and online:
    print(num2)
    num2 += 1
    Contador += 1

# Bucle o ciclo For
print("/////////////////")

for i in range(4):
    print(i)
print("////////////////")

for c in range(5):
    print("Feliz Cumpleaños Yureymi")
asdasds
