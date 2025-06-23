def saudacao_personalizada(nome, idioma):
    if idioma == 'inglês':
        print(f'Hello,{nome}')
    elif idioma == 'português':
        print(f'Olá,{nome}')
    elif idioma == 'francês':
        print(f'Bonjur,{nome}')
    else:
        print(f'Hello,{nome}')
saudacao_personalizada(str(input("Digite nome: ")), str(input('Digite seu idioma: ')))