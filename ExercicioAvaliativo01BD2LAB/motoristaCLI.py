from motoristaDAO import *
class MotoristaCLI:
    def __init__(self, database: Database):
        self.motorista_dao = MotoristaDAO(database)

    def menu(self):
        while True:
            print("\n1 - Criar motorista")
            print("2 - Ler motorista")
            print("3 - Atualizar motorista")
            print("4 - Deletar motorista")
            print("5 - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.criar_motorista()
            elif opcao == "2":
                self.ler_motorista()
            elif opcao == "3":
                self.atualizar_motorista()
            elif opcao == "4":
                self.delete_motorista()
            elif opcao == "5":
                break
            else:
                print("Opção inválida")

    def criar_motorista(self):
        nota = input("Digite a nota do motorista: ")
        nome_passageiro = input("Digite o nome do passageiro: ")
        documento_passageiro = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        corridas = []
        while True:
            nota_corrida = input("Digite a nota da corrida: ")
            distancia_corrida = float(input("Digite a distância percorrida na corrida: "))
            valor_corrida = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, vars(passageiro))
            corridas.append(corrida)
            opcao = input("Deseja adicionar mais uma corrida? (S/N) ")
            if opcao.lower() != "s":
                break
        motorista = Motorista(nota, corridas)
        self.motorista_dao.create(motorista)

    def ler_motorista(self):
        _id = input("Digite o ID do motorista que deseja ler: ")
        motorista = self.motorista_dao.read(_id)
        print(motorista)

    def atualizar_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_dao.read(id)

        if motorista:
            corridas_new = []
            notaNova = input("Nova nota do motorista: ")
            nome = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)
            qntCorridas = int(input("Entre com o numero de corridas"))
            for k in range(qntCorridas):
                nota = float(input(f"{k + 1} - Entre com a nota: "))
                distancia = float(input(f"{k + 1} - Entre com a distancia: "))
                valor = float(input(f"{k + 1} - Entre com o valor: "))
                corrida = Corrida(nota, distancia, valor, passageiro.to_dict())
                corridas_new.append(vars(corrida))
            self.motorista_dao.update(id, notaNova, corridas_new)

    def delete_motorista(self):
        motorista_id = input("Entre com o ID do motorista a ser excluido: ")
        self.motorista_dao.delete(motorista_id)