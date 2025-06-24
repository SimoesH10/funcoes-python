def split_custom(texto, caractere):
    resultado = []
    atual = ""
    for i in texto:
        if i == caractere:
            resultado.append(atual)
            atual = ""
        else:
            atual += i
    resultado.append(atual)
    return resultado

texto = input("Digite um texto: ")
caractere = input("Digite um caractere: ")

print(split_custom(texto, caractere))