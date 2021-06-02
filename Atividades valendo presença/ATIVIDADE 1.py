listapoo = [10,20,15,30,25]
# primeira questão. Pilha.
listapoo.insert(0, int(input ('digite um numero para adicionar ao topo da pilha: ' )))
print(listapoo)
listapoo.pop(0)
print(listapoo)

# segunda questão. fila
listapoo.append(int(input('digite um número ')))
print(listapoo)
listapoo.pop(0)
print(listapoo)

#terceira questão. lista encadeada
listapoo.insert(int(input('digite em qual indice você quer adcionar ')), int(input('digite um numero para adicionar no indice indicado ')))
print(listapoo)
listapoo.pop(int(input('digite em qual indice você quer retirar  ')))
print(listapoo)