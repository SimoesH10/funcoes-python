def calcular_pagamneto(horas_trabalhadas, taxa_hora, pagamento_total):
    pagamento_total = horas_trabalhadas * taxa_hora
    return pagamento_total

resultado = calcular_pagamneto(float(input("Digite as horas trabalhadas: ")),float(input("Digite a taxa por hora: ")),0)

print(f"Pagamento total: R$ {resultado:.2f}")