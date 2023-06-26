import random

import PySimpleGUI as sg


class chutenumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text("Seu chute", size=(35, 0))],
            [sg.Input(size=(18, 0), key="Valor chute")],
            [sg.Button("Chutar! ")],
            [sg.Output(size=(20, 10))],
        ]

        self.janela = sg.Window("CHUTE UM NUMERO!", layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                self.evento, self.valores = self.janela.Read()

                if self.evento == "Chutar!":
                    self.valor_chute = self.valores["Valorchute"]
                    while self.tentar_novamente:
                        if int(self.valor_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo!")
                            break
                        elif int(self.valor_chute) < self.valor_aleatorio:
                            print("Chute um valor mais alto!")
                            break
                        if int(self.valor_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print("parabens")
                            break
        except Exception:
            print("FAVOR DIGITAR UM NUMERO!")
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =
        random.randint(self.valor_minimo, self.valor_maximo)


chute = chutenumero()
chute.Iniciar()
