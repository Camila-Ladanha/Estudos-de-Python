"""Calculadora com while"""

while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input ("Digite o segundo número: ")
    operador = input ("Digite ( + - / *): ")

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
    except:
        print("Você digitou um número Inváldio")
        continue

    if operador == "+":
        print(num_1 + num_2)

    elif operador == "-": 
        print(num_1 - num_2)

    elif operador == "*":
        print(num_1 * num_2)

    elif operador == "/":
        print(num_1 / num_2)

        if num_2 == 0:
            print("Não é possível dividir por zero.")
            continue
        print(num_1 / num_2)

    else: 
        print("Você digitou o operador Inválido")
        continue
    while True:
        sair = input("Deseja sair? [S]im ou [N]ão: ").lower()
        
        if sair == "s":
            programa_encerra = True
            break
        elif sair == "n":
            programa_encerra = False
            break
        else: 
            print("Digite apenas S ou N.")

    print("fim do programa")
    break