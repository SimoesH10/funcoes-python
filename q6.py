def funcao_idade(idade):
    if idade > 0 and idade <=150:
        print(f'sua idade é: {idade}. É valida!')
    else:
        print('Retorne uma idade valida!')

funcao_idade(int(input('Digite sua idade: ')))