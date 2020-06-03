#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pywhatkit as kit

#Função que executa alguma coisa
def funcao_botao():
    n1 = str(caixa_1.get())
    kit.playonyt(n1)
    messagebox.showinfo('Encontramos a sua música!', 'Divirta-se curtindo a sua música! ')

#Iniciando uma janela
janela = Tk()

#Colocando um texto dentro da janela
label_1 = Label(janela, text='Digite a música que você está procurando', font = 'Arial 9')
label_1.place(x=30,y=10)

#Criando um botão de função
botao_1 = Button(janela, width = 25, text ='Tocar!', command =funcao_botao, background = 'white')
botao_1.place(x=50,y=80)

#Criando uma caixa de entrada de dados
caixa_1 = Entry(janela, background='white', width = 30, font='Arial 8')
caixa_1.place(x=50, y=50)

#Criando uma janela 800x600
janela.geometry('350x200+0+0')

#Criando um loop para manter a janela aberta
janela.title("PlayTube v1.0")
janela.mainloop()