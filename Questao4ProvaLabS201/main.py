class AnimalCorrida:
    def __init__(self,velocidade:int,nome:str,cor:str):
        self.nome = nome
        self.cor = cor
        self.velocidade = velocidade

class Cavalo(AnimalCorrida):
    def __init__(self,velocidade:int,nome:str,cor:str):
        super().__init__(velocidade,nome,cor)
        self.posicao = 0

    def mover(self):
        pos = self.posicao
        if (pos<200):
            self.posicao = self.posicao + self.velocidade*4
        else: print(self.nome,"terminou a corrida!")


c1 = Cavalo(10,"Juca","Preto")
c2 = Cavalo(11,"Gabriel","Leite")
c3 = Cavalo(12,"Eueu","Marrom Escuro")

c1.mover()
c1.mover()
c1.mover()
c1.mover()
c1.mover()
c1.mover()
c2.mover()
c2.mover()
c2.mover()
c2.mover()
c2.mover()
c2.mover()
c3.mover()
c3.mover()
c3.mover()
c3.mover()
c3.mover()
c3.mover()

