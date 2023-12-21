# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Michael", "Castillo"]

print(type(my_list))
print(type(my_other_list))


#_________________________________________________________________________
# Acceso a elementos y búsqueda
print(my_other_list[0]) #35
print(my_other_list[1]) #1.77
print(my_other_list[-1]) #Castillo
print(my_other_list[-4]) #35
# print(my_other_list[-5]) #Error, no hay esa cantidad de elementos en la lista.
# print(my_other_list[4]) IndexError
print(my_list.count(30))
print(my_other_list.index("Michael"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("Athenas") #Inserta al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") #Se dice la posición y se inserta
print(my_other_list)

my_other_list[1] = "Azul" #Se sobreescribe lo que hay en la posición
print(my_other_list)

my_other_list.remove("Azul") #Remueva la palabra que coincide
print(my_other_list)

my_list.remove(30) # Remueve el primer valor encontrado
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))