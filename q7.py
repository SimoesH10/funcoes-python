def valida_email(email):
    if ' ' in email:
        print('Seu email é inválido')
    elif email.count('@') != 1:
        print('Digite um email inválido')
    elif not email.endswith('.com'):
        print('Digite um email inválido')
    else:
        print('Email válido')

valida_email(input('Digite seu email: '))