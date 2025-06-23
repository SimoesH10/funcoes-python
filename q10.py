def contador_letras(texto):
    maiusculas = 0
    minusculas = 0
    
    for caractere in texto:
        if caractere.isupper():
            maiusculas += 1
        elif caractere.islower():
            minusculas += 1
            
    return maiusculas, minusculas

entrada = input("Digite uma frase: ")
maiusculas, minusculas = contador_letras(entrada)
print(f"Maiúsculas: {maiusculas}")
print(f"Minúsculas: {minusculas}")
