import math

while True:
    print("Escolha a forma geométrica:")
    print("1 - Retângulo")
    print("2 - Triângulo")
    print("3 - Círculo")
    opcao = input("Opção: ")

    if opcao not in ["1", "2", "3"]:
        print("Opção inválida, tente novamente.")
        continue

    if opcao == "1":
        base = input("Digite a medida da base do retângulo: ")
        altura = input("Digite a medida da altura do retângulo: ")

        if not base.isnumeric() or not altura.isnumeric():
            print("As medidas devem ser números positivos, tente novamente.")
            continue

        area = int(base) * int(altura)
        print("A área do retângulo é:", area)

    elif opcao == "2":
        base = input("Digite a medida da base do triângulo: ")
        altura = input("Digite a medida da altura do triângulo: ")

        if not base.isnumeric() or not altura.isnumeric():
            print("As medidas devem ser números positivos, tente novamente.")
            continue

        area = int(base) * int(altura) / 2
        print("A área do triângulo é:", area)

    elif opcao == "3":
        raio = input("Digite a medida do raio do círculo: ")

        if not raio.isnumeric():
            print("A medida do raio deve ser um número positivo, tente novamente.")
            continue

        area = math.pi * int(raio) ** 2
        print("A área do círculo é:", area)

    break
