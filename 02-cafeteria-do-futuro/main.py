""" Cafeteria do Futuro"""
print("Bem-vindo(a) à Cafeteria do Futuro!")
print("-" * 35)

nome = input ("Digite o seu nome: ")
quantidade = int(input("Digite quantos cafés deseja: "))
preco = float(input("Digite o preço do café: "))
cartao = bool(int(input("Possui cartão fidelidade? (1 = Sim | 0 = Não):  ")))

print("Cliente: ", nome)
print("Quantidade: ", quantidade)
print("Preço do café: R$", preco)
print("Cartão fidelidade? ", cartao)

print("-" * 35)

print("O pedido já vai ser preparado, obrigada pela preferência :)")