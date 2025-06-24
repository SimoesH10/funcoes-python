def replace_custom(texto, antigo, novo):
    return texto.replace(antigo, novo)

texto = input("Digite o texto original: ")
antigo = input("Digite o texto a ser substituído: ")
novo = input("Digite o novo texto: ")

print(replace_custom(texto, antigo, novo))