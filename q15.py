def startwith_custom(texto, prefixo):
    return texto[:len(prefixo)] == prefixo

texto = input("Digite o texto: ")
prefixo = input("Digite um prefixo: ")

print(startwith_custom(texto, prefixo))