from neo4j import GraphDatabase

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def criar(self, tx):
        query = "CREATE (p:Pessoa {nome: $nome, idade: $idade, sexo: $sexo}) RETURN p"
        result = tx.run(query, nome=self.nome, idade=self.idade, sexo=self.sexo)
        return result.single()[0]

    @staticmethod
    def buscar(tx, nome):
        query = "MATCH (p:Pessoa {nome: $nome}) RETURN p.nome as nome, p.idade as idade, p.sexo as sexo"
        result = tx.run(query, nome=nome)
        record = result.single()
        if record is not None:
            return Pessoa(record["nome"], record["idade"], record["sexo"])
        return None

    def atualizar(self, tx):
        query = "MATCH (p:Pessoa {nome: $nome}) SET p.idade = $idade, p.sexo = $sexo RETURN p"
        result = tx.run(query, nome=self.nome, idade=self.idade, sexo=self.sexo)
        return result.single()[0]

    def excluir(self, tx):
        query = "MATCH (p:Pessoa {nome: $nome}) DETACH DELETE p"
        tx.run(query, nome=self.nome)

    def criar_relacao_conta_bancaria(self, tx, numero_conta):
        query = "MATCH (p:Pessoa {nome: $nome}), (c:ContaBancaria {numero_conta: $numero_conta}) " \
                "CREATE (p)-[r:TEM_CONTA]->(c) RETURN r"
        result = tx.run(query, nome=self.nome, numero_conta=numero_conta)
        return result.single()[0]


class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def criar(self, tx):
        query = "CREATE (c:ContaBancaria {numero_conta: $numero_conta, nome_titular: $nome_titular, saldo: $saldo}) " \
                "RETURN c"
        result = tx.run(query, numero_conta=self.numero_conta, nome_titular=self.nome_titular, saldo=self.saldo)
        return result.single()[0]

    @staticmethod
    def buscar(tx, numero_conta):
        query = "MATCH (c:ContaBancaria {numero_conta: $numero_conta}) RETURN c.numero_conta as numero_conta, " \
                "c.nome_titular as nome_titular, c.saldo as saldo"
        result = tx.run(query, numero_conta=numero_conta)
        record = result.single()
        if record is not None:
            return ContaBancaria(record["numero_conta"], record["nome_titular"], record["saldo"])
        return None

    def atualizar(self, tx):
        query = "MATCH (c:ContaBancaria {numero_conta: $numero_conta}) SET c.nome_titular = $nome_titular, " \
                "c.saldo = $saldo RETURN c"
        result = tx.run(query, numero_conta=self.numero_conta, nome_titular=self.nome_titular, saldo=self.saldo)
        return result.single()[0]

    def excluir(self, tx):
        query = "MATCH (c:ContaBancaria {numero_conta: $numero_conta}) DETACH DELETE c"
        tx.run(query, numero_conta=self.numero_conta)


def menu():
    print("=== MENU ===")
    print("1. Criar Pessoa")
    print("2. Buscar Pessoa")
    print("3. Atualizar Pessoa")
    print("4. Excluir Pessoa")
    print("5. Criar Conta Bancária")
    print("6. Buscar Conta Bancária")
    print("7. Atualizar Conta Bancária")
    print("8. Excluir Conta Bancária")
    print("9. Criar relação entre Pessoa e Conta Bancária")
    print("10. Sair")


def main():
    uri = "bolt://54.84.92.177:7687"
    username = "neo4j"
    password = "merchants-annex-odors"
    driver = GraphDatabase.driver(uri, auth=(username, password))

    while True:
        menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Nome da Pessoa: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            pessoa = Pessoa(nome, idade, sexo)

            with driver.session() as session:
                session.execute_write(pessoa.criar)
                print("Pessoa criada com sucesso!")

        elif opcao == "2":
            nome = input("Nome da Pessoa: ")

            with driver.session() as session:
                pessoa = session.execute_read(Pessoa.buscar, nome)
                if pessoa is not None:
                    print(f"Nome: {pessoa.nome}")
                    print(f"Idade: {pessoa.idade}")
                    print(f"Sexo: {pessoa.sexo}")
                else:
                    print("Pessoa não encontrada.")

        elif opcao == "3":
            nome = input("Nome da Pessoa: ")
            idade = input("Nova idade: ")
            sexo = input("Novo sexo: ")
            pessoa = Pessoa(nome, idade, sexo)

            with driver.session() as session:
                session.execute_write(pessoa.atualizar)
                print("Pessoa atualizada com sucesso!")

        elif opcao == "4":
            nome = input("Nome da Pessoa: ")
            pessoa = Pessoa(nome, None, None)

            with driver.session() as session:
                session.execute_write(pessoa.excluir)
                print("Pessoa excluída com sucesso!")

        elif opcao == "5":
            numero_conta = input("Número da Conta: ")
            nome_titular = input("Nome do Titular: ")
            saldo = input("Saldo: ")
            conta = ContaBancaria(numero_conta, nome_titular, saldo)

            with driver.session() as session:
                session.execute_write(conta.criar)
                print("Conta bancária criada com sucesso!")

        elif opcao == "6":
            numero_conta = input("Número da Conta: ")

            with driver.session() as session:
                conta = session.execute_read(ContaBancaria.buscar, numero_conta)
                if conta is not None:
                    print(f"Número da Conta: {conta.numero_conta}")
                    print(f"Nome do Titular: {conta.nome_titular}")
                    print(f"Saldo: {conta.saldo}")
                else:
                    print("Conta bancária não encontrada.")

        elif opcao == "7":
            numero_conta = input("Número da Conta: ")
            nome_titular = input("Novo nome do Titular: ")
            saldo = input("Novo saldo: ")
            conta = ContaBancaria(numero_conta, nome_titular, saldo)

            with driver.session() as session:
                session.execute_write(conta.atualizar)
                print("Conta bancária atualizada com sucesso!")

        elif opcao == "8":
            numero_conta = input("Número da Conta: ")
            conta = ContaBancaria(numero_conta, None, None)

            with driver.session() as session:
                session.execute_write(conta.excluir)
                print("Conta bancária excluída com sucesso!")

        elif opcao == "9":
            nome_pessoa = input("Nome da Pessoa: ")
            numero_conta = input("Número da Conta: ")

            with driver.session() as session:
                pessoa = session.execute_read(Pessoa.buscar, nome_pessoa)
                conta = session.execute_read(ContaBancaria.buscar, numero_conta)
                if pessoa is not None and conta is not None:
                    session.execute_write(pessoa.criar_relacao_conta_bancaria, numero_conta)
                    print("Relação criada com sucesso!")
                else:
                    print("Pessoa ou conta bancária não encontrada.")

        elif opcao == "10":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

    driver.close()


if __name__ == "__main__":
    main()
