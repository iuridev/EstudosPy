lista = []

#add item na lista
lista.append(1)
lista.append("Hello World")
lista.append([10, 40, 20])
print(lista)

#copiar lista
lista_copia = lista.copy()
print(lista_copia)

#limpar a lista
lista.clear()
print(lista)

#contar quantas vezes um obj aparece na lista
lista_copia.append(1)
lista_copia.append(10)
lista_copia.append(100)
print(lista_copia.count(1))

#saber o indice de referença - primeira ocorrencia
print(lista_copia.index("Hello World"))

#retirar elemento da lista (exemplo de pilha)
print(lista_copia.pop())
print(lista_copia.pop(1))

print(lista_copia)
lista_copia.remove(1) #remove o objeto int 1
print(lista_copia)

#fazer espelhmento da lista
lista_copia.reverse()
print(lista_copia)

#ordenar a lista
lista = ["iuri", "Brasil", "futebol"]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
lista.sort(key=lambda x: len(x))
print(lista)
lista.sort(key=lambda x: len(x), reverse=True) 
print(lista)

#tamanho da lista
print(len(lista))

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])