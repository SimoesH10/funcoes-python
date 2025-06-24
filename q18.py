def strip_custom(texto, caracteres):
    inicio = 0
    fim = len(texto)
    while inicio < fim and texto[inicio] in caracteres:
        inicio += 1
    while fim > inicio and texto[fim - 1] in caracteres:
        fim -= 1
    return texto[inicio:fim]