# while
i = 0
while i < 5:
    print(i)
    i += 1

print("-" * 4)

dir(2)  # Verificar que objetos son iterables (Ej. con un entero = 2
dir(2.0)  # Float no es iterable
dir("Hola Mundo")  # String es iterable
dir({1: 2})  # diccionario es iterable

frutas = ['manzana', 'pera', 'platano', 'naranja', 'kiwi', 'arandano']

for fruta in frutas:
    print(fruta)

print(fruta)  # Imprime el ultimo valor, pq guarda ultima posicion de for

print("-" * 4)

i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

print("-" * 4)

# Objeto de tipo iterable
frutas = iter(frutas)
print(frutas)

print(next(frutas))
print(next(frutas))
print(next(frutas))
print(next(frutas))
print(next(frutas))
print(next(frutas))
# print(next(frutas)) #error, ya no quedan elementos a iterar
print("-" * 4)

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las
# correspondientes notas introducidas por el usuario.

asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lenguaje']

i = 0
notas = []
for asignatura in asignaturas:
    nota = input(f'Dime tu nota en asignatura {asignatura}: ')
    notas.append(nota)

for idx, asignatura in enumerate(asignaturas):
    print(f'En {asignatura} has sacado la nota {notas[idx]}')

print("-" * 4)

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir

asignaturas = {'Matematicas': 0, 'Fisica': 0, 'Quimica': 0, 'Historia': 0, 'Lenguaje': 0}
for asignatura in asignaturas:
    nota = input(f'Dime tu nota en asignatura {asignatura}: ')
    # asignaturas[]

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)

print("-" * 4)
