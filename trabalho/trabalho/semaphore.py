'''Código com FCFS e RR'''
import threading
import time
import random
from collections import deque

class Tarefa(threading.Thread):
    def __init__(self, idTarefa, tempoExecucao):
        super().__init__()
        self.idTarefa = idTarefa  # Identificador da tarefa
        self.tempoExecucao = tempoExecucao  # Tempo de execução da tarefa
        self.tempoInicio = None  # Tempo de início da tarefa
        self.tempoFim = None  # Tempo de término da tarefa

    def run(self):
        self.tempoInicio = time.time()  # Marca o tempo de início da tarefa
        print(f"Tarefa {self.idTarefa} começou em {self.tempoInicio:.2f}")
        time.sleep(self.tempoExecucao)  # Simula o tempo de execução da tarefa
        self.tempoFim = time.time()  # Marca o tempo de término da tarefa
        print(f"Tarefa {self.idTarefa} terminou em {self.tempoFim:.2f}")

def escalonamentoFcfs(tarefas):
    for tarefa in tarefas:
        tarefa.start()  # Inicia a execução da tarefa
        tarefa.join()  # Aguarda a conclusão da tarefa

def escalonamentoRoundRobin(tarefas, quantumTempo):
    fila = deque(tarefas)  # Fila de tarefas para o Round Robin
    while fila:
        tarefa = fila.popleft()  # Remove a primeira tarefa da fila
        tarefa.tempoInicio = time.time()  # Marca o tempo de início da tarefa
        if tarefa.tempoExecucao > quantumTempo:
            time.sleep(quantumTempo)  # Executa a tarefa pelo tempo do quantum
            tarefa.tempoExecucao -= quantumTempo  # Reduz o tempo de execução restante
            fila.append(tarefa)  # Re-enfileira a tarefa se não terminou
        else:
            time.sleep(tarefa.tempoExecucao)  # Executa a tarefa pelo tempo restante
            tarefa.tempoFim = time.time()  # Marca o tempo de término da tarefa
            print(f"Tarefa {tarefa.idTarefa} terminou em {tarefa.tempoFim:.2f}")

def calcularTempoEsperaMedio(tarefas):
    tempoEsperaTotal = 0
    for tarefa in tarefas:
        tempoEspera = tarefa.tempoInicio - tempoInicioGlobal  # Calcula o tempo de espera da tarefa
        tempoEsperaTotal += tempoEspera
    return tempoEsperaTotal / len(tarefas)  # Retorna o tempo de espera médio

if __name__ == "__main__":
    numTarefas = 5
    tarefasFcfs = [Tarefa(i, random.randint(1, 5)) for i in range(numTarefas)]
    tarefasRr = [Tarefa(i, random.randint(1, 5)) for i in range(numTarefas)]
    
    # Escalonamento FCFS
    tempoInicioGlobal = time.time()
    escalonamentoFcfs(tarefasFcfs)
    tempoEsperaMedioFcfs = calcularTempoEsperaMedio(tarefasFcfs)
    print(f"Tempo de espera médio (FCFS): {tempoEsperaMedioFcfs:.2f} segundos")

    # Escalonamento Round Robin
    quantumTempo = 2
    tempoInicioGlobal = time.time()
    escalonamentoRoundRobin(tarefasRr, quantumTempo)
    tempoEsperaMedioRr = calcularTempoEsperaMedio(tarefasRr)
    print(f"Tempo de espera médio (RR): {tempoEsperaMedioRr:.2f} segundos")
