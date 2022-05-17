from controllers.automataControllers import automataController
from tkinter import *

class home:
    def __init__(self):
        self.automataController = automataController()
    
    def init(self):
        window = Tk()
        window.title("Procesamiento de cadenas mediante Automatas")
        window.geometry('600x600')
        
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
        self.cmpLexSintactico = Text(window,width=43,height=4)
        self.cmpLexSintactico.grid(row=10,columnspan=4)
                      
        lblToken2 = Label(window, text="Token3")
        lblToken2.grid(row=12, column=0)
        self.txtLexToken = Entry(window, width=50)
        self.txtLexToken.grid(row=12, column=1)
        
        lblEstado = Label(window, text="ESTADO RESPUESTA")
        lblEstado.grid(row=14, columnspan=2)
        self.cmpLexRespuesta = Text(window,width=43,height=4)
        self.cmpLexRespuesta.grid(row=15,columnspan=4)
        
        
        window.mainloop()
        
    def clickedAutoLex(self):
        self.cmpLex.delete('1.0', END)
        cadenaOriginal = self.automataController.esValido(self.txtPregunta.get()) #retorno variables "error_palabra", "caracter_error", "estadoacp"
        self.cmpLex.insert(INSERT, "Validación de la cadena:\n" + cadenaOriginal) 
        tokens1 = self.auto_lex.tokenizado() #retorno de la cadena de id's
        self.txtLexToken.insert(INSERT, tokens1)


"""
    def clickedEntero(self):
        self.cmpResult.delete('1.0', END)
        cadenaEntero = self.automataController.esEntero(self.txtEntero.get())
        self.cmpResult.insert(INSERT, "Validación de entero:\n" + cadenaEntero)

    def clickedCorreo(self):
        self.cmpResult.delete('1.0', END)
        cadenaCorreo = self.automataController.esReserved(self.txtCorreo.get())
        self.cmpResult.insert(INSERT, "Validación de correo electrónico:\n" + cadenaCorreo)

    def clickedIdentificador(self):
        self.cmpResult.delete('1.0', END)
        cadenaIdentificador = self.automataController.esId(self.txtIdentificador.get())
        self.cmpResult.insert(INSERT, "Validación de identificador\n" + cadenaIdentificador)"""