from cgi import test
from tkinter import *

class test:
    def __init__(self):
        window = Tk()
        window.title("Procesamiento de cadenas mediante Automatas")
        window.geometry('400x400')
     
        #boton y campos de texto recibe datos
        lblPregunta = Label(window, text="Pregunta")
        lblPregunta.grid(row=1, column=0)
        self.txtPregunta = Entry(window, width=50)
        self.txtPregunta.grid(row=1, column=1)
        
        #ventana validación lexica
        lblEstado = Label(window, text="ESTADO ANÁLISIS LÉXICO")
        lblEstado.grid(row=3, columnspan=2)
        self.cmpLex = Text(window,width=43,height=4)
        self.cmpLex.grid(row=4,columnspan=4)
        
        lblToken1 = Label(window, text="Token1")
        lblToken1.grid(row=2, column=0)
        self.txtLexToken = Entry(window, width=50)
        self.txtLexToken.grid(row=2, column=1)
        
        btnAnaLex = Button(window, text="Análisis Léxico", command="self.clickedAnaLex")
        btnAnaLex.grid(row=0, columnspan=2)

        lblToken2 = Label(window, text="Token2")
        lblToken2.grid(row=8, column=0)
        self.txtLexToken = Entry(window, width=50)
        self.txtLexToken.grid(row=8, column=1)
        
        lblEstado = Label(window, text="ESTADO ANÁLISIS SINTÁCTICO")
        lblEstado.grid(row=9, columnspan=2)
        self.cmpLex = Text(window,width=43,height=4)
        self.cmpLex.grid(row=10,columnspan=4)
                      
        lblToken2 = Label(window, text="Token3")
        lblToken2.grid(row=12, column=0)
        self.txtLexToken = Entry(window, width=50)
        self.txtLexToken.grid(row=12, column=1)
        
        lblEstado = Label(window, text="ESTADO RESPUESTA")
        lblEstado.grid(row=14, columnspan=2)
        self.cmpLex = Text(window,width=43,height=4)
        self.cmpLex.grid(row=15,columnspan=4)
        
        
        window.mainloop()

"""
    #Imprime validación lexica        
    def clickedAnaLex(self):
        self.cmpLex.delete('1.0', END)
        anaCadena = self.auto_lex.esValido(self.txtPregunta.get())
        self.cmpLex.insert(INSERT, "Resultado de la evaluación de la cadena: \n" +anaCadena)
        
        #imprime token retorno true:"auto_lex.esValido"
        tokenizatedString = self.auto_lex.token(get())
        self.cmpLexToken.insert(INSERT, "Resultado de la evaluación de la cadena: \n" +tokenizatedString)
"""  

test = test()
#test.init()