class Client:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: Create | Read | Update | Delete | Sair")
            if command == "sair":
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Erro. Tente Novamente.")


class Professor(Client):
    def __init__(self, crud):
        super().__init__()
        self.crud = crud
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)

    def create(self):
        name = input("Nome: ")
        ano = input("Ano de nascimento: ")
        cpf = input("CPF: ")
        self.crud.create(name, int(ano), cpf)
        print(f"Professor {name} criado!")

    def read(self):
        name = input("Nome: ")
        result = self.crud.read(name)
        for i in result:
            print("Nome: ", i["t.name"])
            print("Ano de nascimento: ", i["t.ano_nasc"])
            print("Cpf: ", i["t.cpf"])

    def update(self):
        name = input("Nome: ")
        novoCpf = input("Novo CPF: ")
        self.crud.update(name, novoCpf)

    def delete(self):
        name = input("Nome do professor a ser deletado: ")
        self.crud.delete(name)