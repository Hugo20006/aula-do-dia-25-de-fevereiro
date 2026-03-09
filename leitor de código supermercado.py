nome1 = input("Qual o nome do primeiro amaciante ?")
nome2 = input("Qual o nome do segundo amaciante ?")
volume1= float(input(f"Qual volume do {nome1}: "))
volume2= float(input(f"Qual o volume do {nome2}: "))
preço1 = float(input(f"Qual o preço do amaciante {nome1}: "))
preço2 = float(input(f"Qual o preço do amaciante {nome2}: "))
pk1 = preço1/volume1
pk2 = preço2/volume2
if pk1<pk2:
    nome1
    print(f"O preço do amaciante {nome1} é menor,seu preço é R${preço1} e seu volume {volume1} é: ")
elif pk2<pk1:
    nome2
    print(f"O preço do amaciante {nome2} é menor e o seu preço é R${preço2} e seu volume {volume2} é: ")
else:
    print("Os 2 amaciante tem o mesmo preço e seus volumes também são iguais")



