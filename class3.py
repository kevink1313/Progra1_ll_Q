# Minimo y maxímo, clasificación de listas, sumando lista, cómo unir conjunto de datos y contar número de aparaciones.
# Ademas de la utilización de instrumentos de cuerda y actualización de cadenas.

numeros = [10,45,2,89,54,1,-3]
maximo = max(numeros)
minimo = min(numeros)

print(maximo)
print(minimo)
numeros.sort()
print(max(numeros))
print(min(numeros))

nombres = ["kevin", "karla", "Celeste", "Daniel"]
nombres.sort()
print(nombres)

# Sumar listas
promedios = [85,95,65]
print(sum(promedios))
# unir listas o conjuntos de datos
ventas_sab = [50, 150,90,85]
ventas_dom = [250, 300,100,900]
print(ventas_sab + ventas_dom)

# cómo saber la moda

pregunta1 = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5]
print(pregunta1.count(4))
print(3 in pregunta1)

# instrumentos de cuerda

nuevo_usuario = "Kevin Jiménez Rojas"
usuario_lista = nuevo_usuario.split()
print(usuario_lista)


dirección = "Buenos Aires, Barrios los Angeles,60301"
nueva_dirección = dirección.replace("Buenos Aires centro", "Las lomas")
dataset_dirección = dirección.split(",")
print(dataset_dirección)
print(nueva_dirección)

