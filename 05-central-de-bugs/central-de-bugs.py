print("=======================")
print("    CENTRAL DE BUGS    ")
print("=======================")

print("Selecione a gravidade do problema: ")
print("1 - Baixa")
print("2 - Média")
print("3 - Alta")
print("4 - Crítica")

gravidade = input("Digite uma opção de 1 a 4: ")


if gravidade == "1":
    print("Bug registrado com prioridade baixa.")
elif gravidade == "2":
    print("Bug enviado para análise.")
elif gravidade == "3":
    print("Desenvolvedor deve ser acionado.")
elif gravidade == "4":
    print("Prioridade Máxima! Bug Crítico deve ser tratado imediatamente.")
else:
    print("Você não digitou um numero de 1 a 4. Operação inválida. ")


print("=======================================")
print("Obrigada por utilizar a Central de Bugs")
print("=======================================")    