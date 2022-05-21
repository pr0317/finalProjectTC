# from controllers.automataControllers import automataController
import tkinter as tk
import os

class Home:
    def __init__(self):
        self.window = tk.Tk()
        self.btnLexicalAnalysisStatus = "normal"
        self.btnSintacticAnalysisStatus = "disabled"
        self.btnAnswerStatus = "disabled"
    #     # self.automataController = automataController()
    #     self.defaultFont = font.nametofont("TkDefaultFont")
    #     self.defaultFont.configure(family="Segoe Script", size=19, weight=font.BOLD) 
    
    def init(self): 
        
        self.window.iconbitmap(os.path.abspath('resources/favicon.ico'))
        self.window.title("Universidad Central - Ingeniería de sistemas")
        self.window.geometry('500x600')
        self.window.resizable(width=False, height=False)


        tk.Label(self.window, 
            text="Analizador de Lenguajes", 
            font=("Calibri", 14, 'bold'), 
            foreground="#FFFFFF", 
            width=500,
            background="#2980B9",
            borderwidth=0
        ).pack(ipadx=0, ipady=8)


        self.mainFrame = tk.Frame(self.window)
        self.mainFrame.pack(pady=20, padx=20, ipady=30)
        self.mainFrame.config(bg="#FFFFFF", bd=0)


        tk.Label(self.mainFrame, 
            text="Por favor ingrese una pregunta", 
            font=("Calibri", 13, 'bold'), 
            foreground="#333333", 
            background="#FFFFFF",
            width=500,
            borderwidth=0
        ).pack(pady=(9,0))


        self.question = tk.Text(self.mainFrame, 
            font=("Calibri", 13),
            bg="#FEFEFE",
            foreground="#333333",
            bd=1,
            width=30,
            height=1,
            padx=8,
            pady=6
        )
        self.question.pack(pady=(10,0))


        self.btnLexicalAnalysis = tk.Button(self.mainFrame, 
            text="Análisis Léxico",
            bd=0,
            fg="#FFFFFF",
            padx=5,
            bg="#3498DB",
            font=("Calibri", 13),
            state=self.btnLexicalAnalysisStatus
        )
        self.btnLexicalAnalysis.pack()
        self.btnLexicalAnalysis.place(x=40, y=95)


        self.btnSintacticAnalysis = tk.Button(self.mainFrame, 
            text="Análisis Sintáctico",
            bd=0,
            fg="#FFFFFF",
            padx=5,
            bg="#1ABC9C",
            font=("Calibri", 13),
            state=self.btnSintacticAnalysisStatus
        )
        self.btnSintacticAnalysis.pack()
        self.btnSintacticAnalysis.place(x=162, y=95)


        self.btnAnswer = tk.Button(self.mainFrame, 
            text="Responder",
            bd=0,
            fg="#FFFFFF",
            padx=5,
            bg="#229954",
            font=("Calibri", 13),
            state=self.btnAnswerStatus
        )
        self.btnAnswer.pack()
        self.btnAnswer.place(x=309, y=95)


        self.errorLabel = tk.Label(self.window, 
            text="No hay errores de validación por mostrar...", 
            font=("Calibri", 11, ''), 
            foreground="#333333", 
            width=400,
            background="#FFFFFF",
            borderwidth=0
        ).pack(ipadx=0, ipady=8, padx=20)

    
        tk.Label(self.window, 
            text="Resultados", 
            font=("Calibri", 13, 'bold'), 
            foreground="#333333", 
            background="#FFFFFF",
            width=400,
            borderwidth=0
        ).pack(ipadx=0, ipady=8, padx=20, pady=(20,0))


        self.resultFrame = tk.Frame(self.window, bg="#FFFFFF", bd=0, width=400)
        self.resultFrame.pack(pady=0, padx=20, ipady=30)

        
        self.title1 = tk.Label(self.resultFrame, 
            text="Oración",
            font=("Calibri", 13, 'bold'),
            background="#FFFFFF"
        )
        self.sentence = tk.Label(self.resultFrame, 
            text="------------------------------",
            font=("Calibri", 13),
            background="#FFFFFF"
        )
        self.title2 = tk.Label(self.resultFrame, 
            text="Tokenización 1",
            font=("Calibri", 13, 'bold'),
            background="#FFFFFF"
        )
        self.token1 = tk.Label(self.resultFrame, 
            text="------------------------------",
            font=("Calibri", 13),
            background="#FFFFFF"
        )
        self.title3 = tk.Label(self.resultFrame, 
            text="Análisis léxico",
            font=("Calibri", 13, 'bold'),
            background="#FFFFFF"
        )
        self.lexicResult = tk.Label(self.resultFrame, 
            text="------------------------------",
            font=("Calibri", 13),
            background="#FFFFFF"
        )
        self.title4 = tk.Label(self.resultFrame, 
            text="Tokenización 2",
            font=("Calibri", 13, 'bold'),
            background="#FFFFFF"
        )
        self.token2 = tk.Label(self.resultFrame, 
            text="------------------------------",
            font=("Calibri", 13),
            background="#FFFFFF"
        )
        self.title5 = tk.Label(self.resultFrame, 
            text="Análisis sintáctico",
            font=("Calibri", 13, 'bold'),
            background="#FFFFFF"
        )
        self.sintacticResult = tk.Label(self.resultFrame, 
            text="------------------------------",
            font=("Calibri", 13),
            background="#FFFFFF"
        )
        self.title6 = tk.Label(self.resultFrame, 
            text="Tokenización 3",
            font=("Calibri", 13, 'bold'),
            background="#FFFFFF"
        )
        self.token3 = tk.Label(self.resultFrame, 
            text="------------------------------",
            font=("Calibri", 13),
            background="#FFFFFF"
        )
        self.title7 = tk.Label(self.resultFrame, 
            text="Respuesta",
            font=("Calibri", 13, 'bold'),
            background="#FFFFFF"
        )
        self.answer = tk.Label(self.resultFrame, 
            text="------------------------------",
            font=("Calibri", 13),
            background="#FFFFFF"
        )
        
        
        self.title1.grid(column=0, row=0)
        self.sentence.grid(column=1, row=0)
        self.title2.grid(column=0, row=1)
        self.token1.grid(column=1, row=1)
        self.title3.grid(column=0, row=2)
        self.lexicResult.grid(column=1, row=2)
        self.title4.grid(column=0, row=3)
        self.token2.grid(column=1, row=3)
        self.title5.grid(column=0, row=4)
        self.sintacticResult.grid(column=1, row=4)
        self.title6.grid(column=0, row=5)
        self.token3.grid(column=1, row=5)
        self.title7.grid(column=0, row=6)
        self.answer.grid(column=1, row=6)


        self.window.mainloop()
        
    # def clickedAutoLex(self):
    #     self.cmpLex.delete('1.0', END)
    #     cadenaOriginal = self.automataController.esValido(self.txtPregunta.get()) #retorno variables "error_palabra", "caracter_error", "estadoacp"
    #     self.cmpLex.insert(INSERT, "Validación de la cadena:\n" + cadenaOriginal) 
    #     tokens1 = self.auto_lex.tokenizado() #retorno de la cadena de id's
    #     self.txtLexToken.insert(INSERT, tokens1)


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