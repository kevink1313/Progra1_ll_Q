# Ser capaz de organizar muchos datos relaciones, es parte escencial de la programación

age_1 = 4
age_2 = 40
age_3 = 53
age_4 = 13

# Listas 
tareas = ["Read" , "Workout" , "Code"]
print(tareas)

user = ["Luis" , "Kevin"]
print(user)

temperaturas = [12,14,29,25] #los numeros inician desde 0, y se cuentan hasta el infinito, en este caso el 29 seria el indice 2
print(temperaturas[2])
temperaturas[2] = 35
print(temperaturas[2])

laps = [320,315,321]
laps.insert(1,319)
eliminado = laps.pop(0)
print(laps)
print("EL ELEMENTO ELIMINADO ES," ,eliminado)


# Recorrer listas por medio de bucle

notas = [98,80,74,96,50,45]
for nota in notas:
    print(nota)


artistas = ["Roses","Franco"]
for artista in artistas:
    print(artista)

# Para averiguar el numero de elementos que tiene una lista es con la función la palabra reservada LEN()

users = ["kevin","Luis","cathy"]
user_cont = len(users)
print(user_cont)

# podemos usar la longitud de la lista para crear declaraciones condicionales basadas en la cantidad
# de elementos como el anterior

if user_cont > 0:
    print("Empieza a trabajar")

lista_compras = ["papas","pollo","arroz"]
print(lista_compras[-1])

if len(lista_compras) > 0:
    print("Tu lista de compras es la siguiente")
    for arti in lista_compras:
        print(arti)
else:
    print("No tienes nada en tu lista de compras.")

