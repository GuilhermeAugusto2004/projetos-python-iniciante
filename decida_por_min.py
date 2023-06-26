import random

import PySimpleGUI as sg


class Decidapormim:
    def __init__(self):
        self.resposta = [
            "Com certeza vc deve fazer isso",
            "Nao sei, vc quem sabe",
            "Nao faz isso",
            "Acho que ta na hora certa",
        ]

    def Iniciar(self):
        layout = [
            [sg.Text("FAÇA SUA PERGUNTA:")],
            [sg.Input()],
            [sg.Output(size=(20, 10))],
            [sg.Button("Decida por min")],
        ]

        self.janela = sg.Window("decida por min", layout=layout)
        self.eventos, self.valores = self.janela.Read()
        if self.eventos == "Decida por min":
            print(random.choice(self.resposta))
            self.janela.close()

        input("faça sua pergunta: ")
        print(random.choice(self.resposta))


decida = Decidapormim()
decida.Iniciar
