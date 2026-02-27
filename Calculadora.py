print("########################################")
print("        Calculadora Python             ")
print("########################################")

print("Tecle a opção desejada e aperte ENTER:")
print(" 1 - SOMA")
print(" 2 - SUBTRAÇÃO")
print(" 3 - MULTIPLICAÇÃO")
print(" 4 - DIVISÃO")
print(" 5 - POTÊNCIA")
print(" 6 - RAIZ QUADRADA")

op = int(input("Opção desejada: "))

# Raiz quadrada só precisa de um número
if op == 6:
    a = int(input("Entre com o valor de A: "))
    if a >= 0:
        print("A raiz quadrada é:", a ** 0.5)
    else:
        print("Não é possível calcular raiz quadrada de número negativo.")
else:
    a = int(input("Entre com o valor de A: "))
    b = int(input("Entre com o valor de B: "))

    if op == 1:
        print("A soma é:", a + b)
    elif op == 2:
        print("A subtração é:", a - b)
    elif op == 3:
        print("A multiplicação é:", a * b)
    elif op == 4:
        if b != 0:
            print("A divisão é:", a // b)  # Divisão inteira
        else:
            print("Erro: Divisão por zero!")
    elif op == 5:
        print("A potência é:", a ** b)
    else:
        print("Opção inválida.")

input()