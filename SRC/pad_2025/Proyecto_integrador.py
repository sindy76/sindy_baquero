# 1.Crear conjuntos en Python
# Usando el constructor set() para crear el primer conjunto:
group_a = set(['johana', 'Marcos', 'Andres', 'hugo', 'Pepe'])
# Usando la sintaxis literal con llaves para crear los otros dos conjuntos:
group_b = {'johana', 'carla', 'Andres', 'Antonio', 'Marcos'}
group_c = {'johana', 'Antonio', 'Marcos', 'Pepe', 'Carlos'}
print("Grupo A:", group_a)
print("Grupo B:", group_b)
print("Grupo C:", group_c)
print("***********************************************************************************")
# 2.Unión de conjuntos: combina todos los elementos sin duplicados
all_students = group_a.union(group_b).union(group_c)
for student in all_students:
    groups_in = []
for letter, group in zip('ABC', [group_a, group_b, group_c]):
        if student in group:
            groups_in.append(letter)
groups_str = '-'.join(groups_in)
plural = 's' if len(groups_in) > 1 else ''
print(f'{student} en grupo{plural}: {groups_str}') 
print("Estudiantes en todos los grupos:", all_students)
print("***********************************************************************************")

# 3.Intersección de conjuntos: encuentra los elementos comunes entre dos conjuntos
common_students = group_a.intersection(group_b)
print("Estudiantes comunes entre A y B:", common_students)
print("***********************************************************************************")

# 4. métodos disponibles para conjuntos:
#  Ejemplos de métodos disponibles para conjuntos
# 4.1 add: Añade un elemento al conjunto.
group_a_add = group_a.copy()
group_a_add.add("Sofía")
print("group_a después de add('Sofía'):", group_a_add)
print("***********************************************************************************")
# 4.2 clear: Elimina todos los elementos del conjunto.
group_b_clear = group_b.copy()
group_b_clear.clear()
print("group_b después de clear():", group_b_clear)
print("***********************************************************************************")

# 4.3 copy: Devuelve una copia del conjunto.
group_c_copy = group_c.copy()
print("Copia de group_c:", group_c_copy)
print("***********************************************************************************")

# 4.4 difference: Elementos que están en group_a pero no en group_b.
diff_ab = group_a.difference(group_b)
print("group_a.difference(group_b):", diff_ab)
print("***********************************************************************************")

# 4.5 difference_update: Actualiza una copia de group_a eliminando elementos presentes en group_b.
group_a_diff = group_a.copy()
group_a_diff.difference_update(group_b)
print("group_a después de difference_update(group_b):", group_a_diff)
print("***********************************************************************************")

# 4.6 discard: Elimina un elemento del conjunto; si no existe, no genera error.
group_b_discard = group_b.copy()
group_b_discard.discard("carla")      # 'carla' se elimina si existe.
group_b_discard.discard("NoExiste")   # No genera error si el elemento no existe.
print("group_b después de discard('carla') y discard('NoExiste'):", group_b_discard)
print("***********************************************************************************")


# 4.7 intersection: Devuelve la intersección de dos conjuntos.
intersect_ab = group_a.intersection(group_b)
print("group_a.intersection(group_b):", intersect_ab)
print("***********************************************************************************")

# 4.8 intersection_update: Actualiza una copia de group_c, dejando solo elementos comunes con group_a.
group_c_intersect = group_c.copy()
group_c_intersect.intersection_update(group_a)
print("group_c después de intersection_update(group_a):", group_c_intersect)
print("***********************************************************************************")

# 4.9 isdisjoint: Devuelve True si no hay elementos comunes.
print("group_a.isdisjoint({'X', 'Y'}):", group_a.isdisjoint({'X', 'Y'}))
print("group_a.isdisjoint(group_b):", group_a.isdisjoint(group_b))
print("group_a.isdisjoint(group_c):", group_a.isdisjoint(group_c))
print("group_b.isdisjoint(group_c):", group_b.isdisjoint(group_c))
print("***********************************************************************************")

# 4.10 issubset: Devuelve True si todos los elementos de group_c_intersect están en group_a.
print("group_c_intersect.issubset(group_a):", group_c_intersect.issubset(group_a))
print("group_a.issubset(group_c_intersect):", group_a.issubset(group_c_intersect))
print("group_b.issubset(group_a):", group_b.issubset(group_a))
print("group_b.issubset(group_c):", group_b.issubset(group_c))
print("group_c.issubset(group_b):", group_c.issubset(group_b))
print("***********************************************************************************")


# 4.11 issuperset: Devuelve True si group_a contiene todos los elementos de group_c_intersect.
print("group_a.issuperset(group_c_intersect):", group_a.issuperset(group_c_intersect))
print("group_c_intersect.issuperset(group_a):", group_c_intersect.issuperset(group_a))
print("group_b.issuperset(group_a):", group_b.issuperset(group_a))
print("group_b.issuperset(group_c):", group_b.issuperset(group_c))
print("group_c.issuperset(group_b):", group_c.issuperset(group_b))
print("***********************************************************************************")

# 4.12 pop: Devuelve y elimina un elemento arbitrario de una copia de group_a.
group_a_pop = group_a.copy()
popped_element = group_a_pop.pop()
print("Elemento removido con pop() de group_a:", popped_element)
print("group_a después de pop() (copia):", group_a_pop)
print("***********************************************************************************")

# 4.13 remove: Elimina un elemento específico; genera error si no existe.
group_a_remove = group_a.copy()
if "hugo" in group_a_remove:
    group_a_remove.remove("hugo")
print("group_a después de remove('hugo'):", group_a_remove)
print("***********************************************************************************")

# 4.14 symmetric_difference: Devuelve elementos que están en uno u otro conjunto, pero no en ambos.
sym_diff_ab = group_a.symmetric_difference(group_b)
print("group_a.symmetric_difference(group_b):", sym_diff_ab)
print("***********************************************************************************")

# 4.15 symmetric_difference_update: Actualiza una copia de group_a con la diferencia simétrica con group_b.
group_a_sym = group_a.copy()
group_a_sym.symmetric_difference_update(group_b)
print("group_a después de symmetric_difference_update(group_b):", group_a_sym)
print("***********************************************************************************")

# 4.16 union: Devuelve un conjunto con todos los elementos de ambos conjuntos (ya usado previamente).
union_ab = group_a.union(group_b)
print("group_a.union(group_b):", union_ab)
print("***********************************************************************************")

# 4.17 update: Actualiza una copia de group_a agregando los elementos de group_c.
group_a_update = group_a.copy()
group_a_update.update(group_c)
print("group_a después de update(group_c):", group_a_update)
print("***********************************************************************************")

# 5. Operaciones de álgebra de conjuntos en Python
# 5.1. Unión de conjuntos: Combina todos los elementos sin duplicados.
union_ab = group_a.union(group_b)
print("group_a.union(group_b):", union_ab)
print("************************************************************************************")
# 5.2. Diferencia: Devuelve los elementos que están en group_a pero no en group_b.
diff_ab = group_a.difference(group_b)
print("group_a.difference(group_b):", diff_ab)
print("*****************************************************************************")

# 5.3. Intersección: Devuelve los elementos comunes entre ambos conjuntos.
intersect_ab = group_a.intersection(group_b)
print("group_a.intersection(group_b):", intersect_ab)
print("*****************************************************************************")
# 5.4. isdisjoint: Devuelve True si no hay elementos en común.
print("group_a.isdisjoint(group_b):", group_a.isdisjoint(group_b))
# Comprobación de isdisjoint con otro conjunto sin elementos comunes.
print("group_a.isdisjoint({1, 2}):", group_a.isdisjoint({1, 2}))
print ("******************************************************************************")

# 5.5. issubset: Devuelve True si todos los elementos de group_a están en group_b.
print("group_a.issubset(group_b):", group_a.issubset(group_b))
print("group_a.issubset({'Marcos'}):", group_a.issubset({'Marcos'}))
print("group_a.issubset(group_a):", group_a.issubset(group_a))
print ("******************************************************************************")

# 5.6. issuperset: Devuelve True si group_a contiene todos los elementos del otro conjunto.
print("group_a.issuperset(group_a):", group_a.issuperset(group_a))
print("group_a.issuperset(group_b):", group_a.issuperset(group_b))
print("group_a.issuperset({'Marcos'}):", group_a.issuperset({'Marcos'}))
print ("******************************************************************************")

# 5.7. symmetric_difference: Devuelve los elementos que están en uno u otro conjunto, pero no en ambos.
sym_diff_ab = group_a.symmetric_difference(group_b)
print("group_a.symmetric_difference(group_b):", sym_diff_ab)
print ("******************************************************************************")


    


