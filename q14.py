def min_custom(lista):
    menor_valor = lista[0]
    for i in lista[1:]:
        if i < menor_valor:
            menor_valor = i
        return menor_valor
    
print(min_custom([1,2,3,4,5]))