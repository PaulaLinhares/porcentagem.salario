salario = float(input("Digite aqui o seu salário:"))
if salario >= 1.250:
    novo = salario + (salario * 10/100)
else:
    novo = salario + (salario * 15/100)
print("Seu novo salário com aumento agora é: R${:.2f}".format(novo))
