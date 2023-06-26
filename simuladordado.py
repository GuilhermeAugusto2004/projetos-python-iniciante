import random

import PySimpleGUI as sg


class SimuladorDado:
    def __init__(self):
        self.valorminimo = 1
        self.valormaximo = 6
        self.layout = [
            [sg.Text('BEM VINDO')],
            [sg.Button('sim'), sg.Button('nao')],
        ]

    def iniciar(self):
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.valordado()
            elif self.eventos == 'nao' or self.eventos == 'n':
                print('OBRIGADO')
            else:
                print('favor digitar sim ou nao')
        except:
            print('erro ao receber resposta')

    def valordado(self):
        print(random.randint(self.valorminimo, self.valormaximo))
        quit()


simulador = SimuladorDado()
simulador.iniciar()
