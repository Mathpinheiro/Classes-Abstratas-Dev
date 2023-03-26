from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self,valor):
        pass
    def reduzir_claridade(self,valor):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f'Aumentando a claridade em {valor} pontos')
    def reduzir_claridade(self, valor):
        print(f'Reduzindo a claridade em {valor} pontos') 
    pass

monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(5)