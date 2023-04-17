class Motorista:
    def __init__(self,nota:float,corridas:[]):
        self.nota = nota
        self.corridas = corridas

class Passageiro:
    def __init__(self,nome:str,documento:str):
        self.nome = nome
        self.documento = documento

    def getinfos(self):
        return ("nome: ",self.nome)+("\ndocumento: ",self.documento)

class Corrida:
    def __init__(self,nota:float,distancia:float,valor:float,passageiro:Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro
