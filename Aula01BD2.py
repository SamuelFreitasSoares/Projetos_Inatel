class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        self.assunto = assunto
        print("O professor {self.nome} está ministrando uma aula sobre {self.assunto}")


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print("O aluno {self.nome} está presente.")


class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, aluno):
        self.alunos = aluno

    def listar_presenca(self):
        print("Presença na aula sobre {assunto}, ministrada pelo pofessor {self.professor}:")
        if self.alunos:
            for aluno in self.alunos:
                print("O aluno {aluno.nome} está presente")
        else:
            print("Os alunos não estão presentes")


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())
