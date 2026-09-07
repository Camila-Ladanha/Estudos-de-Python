distancia = 530
consumo = 13
preco_combustivel = 6.97
pessoas = 2

litros = distancia / consumo
custo_total = litros * preco_combustivel
custo_por_pessoa = custo_total / pessoas

print(f"Você precisa de {litros:.2f} litros")
print(f"A viagem custa R$ {custo_total:.2f}")
print(f"Cada pessoa vai pagar R$ {custo_por_pessoa:.2f}")
