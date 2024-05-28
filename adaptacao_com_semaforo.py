'''semáforo que controla o acesso a uma seção crítica'''
import threading
import time
import emoji
import random
import math

class Gerenciador():
    def __init__(self, controle=0, maximo=4):
        self.controle = controle  # Contador de controle para alternar entre os semáforos
        self.maximo = maximo  # Máximo valor do contador de controle
        self.semaforo = threading.Semaphore(1)  # Semáforo para controlar o acesso à seção crítica

    def incrementarControle(self):
        self.controle = (self.controle + 1) % self.maximo  # Incrementa e reinicia o controle
        if self.controle == 0:
            print("\n")  # Nova linha após cada ciclo completo

class Semaforo(threading.Thread):
    def __init__(self, gerenciador, nome):
        super().__init__()
        self.gerenciador = gerenciador  # Referência ao gerenciador
        self.nome = nome  # Nome do semáforo
        self.deveExecutar = True  # Flag para controlar a execução da thread

    def run(self):
        while self.deveExecutar:
            self.gerenciador.semaforo.acquire()  # Adquire o semáforo antes de entrar na seção crítica
            try:
                rand = math.floor(random.random() * 3)
                if rand == 0:
                    cor = ':red_circle:'
                elif rand == 1:
                    cor = ':yellow_circle:'
                else:
                    cor = ':green_circle:'
                print(f"{self.nome} : {emoji.emojize(cor)}")
                self.gerenciador.incrementarControle()
            finally:
                self.gerenciador.semaforo.release()  # Libera o semáforo após sair da seção crítica
            time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente

    def parar(self):
        self.deveExecutar = False  # Define a flag para parar a execução da thread

if __name__ == "__main__":
    gerenciador = Gerenciador()
    semaforoNorte = Semaforo(gerenciador, "Norte")
    semaforoSul = Semaforo(gerenciador, "Sul")
    semaforoLeste = Semaforo(gerenciador, "Leste")
    semaforoOeste = Semaforo(gerenciador, "Oeste")

    semaforoNorte.start()
    time.sleep(0.1)
    semaforoSul.start()
    time.sleep(0.1)
    semaforoLeste.start()
    time.sleep(0.1)
    semaforoOeste.start()
    time.sleep(0.1)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        semaforoNorte.parar()
        semaforoSul.parar()
        semaforoLeste.parar()
        semaforoOeste.parar()
        print("Fim da simulação.")
