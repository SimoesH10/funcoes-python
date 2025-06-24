def max_custom(lista):

    maior_valor = lista[0]
    for i in lista[1:]:
        if i > maior_valor:
            maior_valor = i
    return maior_valor
    
print(max_custom([1,2,3,4,5]))