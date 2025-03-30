#Crear conjuntos en Python
# Usando el constructor set() para crear el primer conjunto:
group_a = set(['Ana', 'Marcos', 'Carlos', 'Mario'])
# Usando la sintaxis literal con llaves para crear los otros dos conjuntos:
group_b = {'Ana', 'Pedro', 'Carlos', 'Antonio'}
group_c = {'Ana', 'Antonio', 'Marcos', 'Pepe'}
# Imprimir los conjuntos originales:
print("Grupo A:", group_a)
print("Grupo B:", group_b)
print("Grupo C:", group_c)
# Unión de conjuntos: combina todos los elementos sin duplicados
all_students = group_a.union(group_b).union(group_c)
print("\nTodos los estudiantes (unión):", all_students)
# Intersección entre dos conjuntos:
a_and_b = group_a.intersection(group_b)
a_and_c = group_a.intersection(group_c)
b_and_c = group_b.intersection(group_c)

print("\nEstudiantes en ambos group_a y group_b:", a_and_b)
print("Estudiantes en ambos group_a y group_c:", a_and_c)
print("Estudiantes en ambos group_b y group_c:", b_and_c)

# Intersección de los tres conjuntos: elemento(s) común(es) a todos
common_all = group_a.intersection(group_b).intersection(group_c)
print("\nEstudiante(s) común(es) a todos los grupos:", common_all)

# Unir todos los estudiantes en un solo conjunto, eliminando duplicados
all_students = group_a.union(group_b).union(group_c)

# Recorrer cada estudiante para determinar en qué grupos se encuentra
for student in all_students:
    groups_in = []
    # Se utiliza zip para asociar las letras 'A', 'B', 'C' a cada grupo
    for letter, group in zip('ABC', [group_a, group_b, group_c]):
        if student in group:
            groups_in.append(letter)
    # Unir las letras con un guion (-) para formar la cadena de grupos
    groups_str = '-'.join(groups_in)
    # Si el estudiante pertenece a más de un grupo, se agrega la 's' en "grupo(s)"
    plural = 's' if len(groups_in) > 1 else ''
    print(f'{student} en grupo{plural}: {groups_str}')

    #Operaciones de álgebra de conjuntos en Python
    # Definición de los conjuntos
group_a = {'Ana', 'Marcos', 'Carlos', 'Mario'}
group_b = {'Ana', 'Pedro', 'Carlos', 'Antonio'}

# Unión: combina todos los elementos de ambos conjuntos, sin duplicados
union_ab = group_a.union(group_b)
print("group_a.union(group_b):", union_ab)
# Ejemplo de salida: {'Ana', 'Antonio', 'Pedro', 'Carlos', 'Marcos', 'Mario'}

# Diferencia: elementos que están en group_a pero no en group_b
difference_ab = group_a.difference(group_b)
print("group_a.difference(group_b):", difference_ab)
# Ejemplo de salida: {'Marcos', 'Mario'}

# Intersección: elementos comunes en ambos conjuntos
intersection_ab = group_a.intersection(group_b)
print("group_a.intersection(group_b):", intersection_ab)
# Ejemplo de salida: {'Ana', 'Carlos'}

# isdisjoint: verifica si los conjuntos no tienen elementos en común
print("group_a.isdisjoint(group_b):", group_a.isdisjoint(group_b))
# Ejemplo de salida: False, ya que comparten elementos

# isdisjoint con otro conjunto que no comparte elementos
print("group_a.isdisjoint({1, 2}):", group_a.isdisjoint({1, 2}))
# Ejemplo de salida: True

# issubset: verifica si group_a es subconjunto de group_b
print("group_a.issubset(group_b):", group_a.issubset(group_b))
# Ejemplo de salida: False

# issubset: verifica si group_a es subconjunto de {'Marcos'}
print("group_a.issubset({'Marcos'}):", group_a.issubset({'Marcos'}))
# Ejemplo de salida: False

# Un conjunto siempre es subconjunto de sí mismo
print("group_a.issubset(group_a):", group_a.issubset(group_a))
# Ejemplo de salida: True

# issuperset: verifica si group_a es superconjunto de sí mismo
print("group_a.issuperset(group_a):", group_a.issuperset(group_a))
# Ejemplo de salida: True

# issuperset: verifica si group_a es superconjunto de group_b
print("group_a.issuperset(group_b):", group_a.issuperset(group_b))
# Ejemplo de salida: False

# issuperset: verifica si group_a es superconjunto de {'Marcos'}
print("group_a.issuperset({'Marcos'}):", group_a.issuperset({'Marcos'}))
# Ejemplo de salida: True

# Diferencia simétrica: elementos que están en uno u otro conjunto, pero no en ambos
sym_diff_ab = group_a.symmetric_difference(group_b)
print("group_a.symmetric_difference(group_b):", sym_diff_ab)
# Ejemplo de salida: {'Antonio', 'Pedro', 'Marcos', 'Mario'}