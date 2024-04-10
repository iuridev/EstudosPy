#uma lista porém que não tem valores repetidos e não é possivel recuperar valor

conjunto_a = set((10,55,20))

conjunto_b = {10, 40, 60}

#para exibir é nescessario converter em lista
print(list(conjunto_a.union(conjunto_b)))
print(list(conjunto_a.intersection(conjunto_b)))
print(list(conjunto_a.difference(conjunto_b)))
print(list(conjunto_a.symmetric_difference(conjunto_b)))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.issuperset(conjunto_b))

conjunto_a.add(99)
conjunto_a.clear()
conjunto_a = conjunto_b.copy()
conjunto_a.discard(10)
conjunto_a.pop()
conjunto_a.remove(60)
print(len(conjunto_a))

print(1 in conjunto_b)






