num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

media = (num1 + num2 + num3 + num4) / 4

if media >= 5:
    print(f"Média: {media:.2f}. Aprovado!")
else:
    print(f"Média: {media:.2f}. Reprovado.")