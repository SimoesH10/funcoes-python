def maior_numero(a, b, c):
    if a > b and a > c:
        print(f'A é o maior {a}')
    elif b > a and b > c:
        print(f'B é o maior {b}')
    else:
        print(f'C é o maior {c}')
maior_numero(int(input('Número de A: ')), int(input('Número de B: ')), int(input('Número de C: ')))