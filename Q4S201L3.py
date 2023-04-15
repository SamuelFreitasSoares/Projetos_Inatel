class Televisao:
    def __init__(self, modelo):
        self.__modelo = modelo
        self.__volume = 0
        self.__canal = ""

    def aumentar_volume(self, quantidade):
        self.__volume += quantidade

    def diminuir_volume(self, quantidade):
        self.__volume -= quantidade

    def trocar_canal(self, canal):
        self.__canal = canal

    def imprimir_info(self):
        print("Modelo:", self.__modelo)
        print("Volume:", self.__volume)
        print("Canal:", self.__canal)


class SmartTV(Televisao):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.__internet = False

    def conectar_internet(self):
        self.__internet = True

    def imprimir_info(self):
        super().imprimir_info()
        print("Internet:", "Conectado" if self.__internet else "Desconectado")


# Criando um objeto da classe Televisao
tv1 = Televisao("TV A")
tv1.aumentar_volume(70)
tv1.diminuir_volume(27)
tv1.trocar_canal("Canal #1")
tv1.imprimir_info()

# Criando um objeto da classe SmartTV
tv2 = SmartTV("Smart TV B")
tv2.aumentar_volume(70)
tv2.diminuir_volume(27)
tv2.trocar_canal("Canal #1")
tv2.conectar_internet()
tv2.imprimir_info()
