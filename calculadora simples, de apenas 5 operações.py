numero1= float(input(" Digite o primeiro número: "))
numero2= float(input(" Digite o segundo número: "))

print("Escolha a operaçã: ")
print("1 - soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
operacão = input("Digite o número da operacão desejada: ")

if operacão == "1":
    resultado = numero1 + numero2
    print(f"Resultado da soma: {resultado}")
elif operacão== "2:":
    resultado = numero1 - numero2
    print(f"Resultado da subtracão: {resultado}")
elif operacão == "3":
    resultado = numero1*numero2
    print(f"Resultado da multiplicação: {resultado}")
elif operacão == "4":
    resultado = numero1/numero2
    print(f"Resultado da divisão: {resultado}")
elif operacão == "5":
    resultado = numero1**numero2
    print (f"Reusltado da potência: {resultado}")
else:
    print("Não achei a operacão desejada")
