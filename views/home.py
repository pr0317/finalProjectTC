from controllers.lexicalAnalyser import LexicalAnalyser
from controllers.sintacticAnalyser import SintacticAnalyser
from controllers.answerAnalyser import AnswerAnalyser
import tkinter as tk
import os

class Home:
    def __init__(self):
        self.window = tk.Tk()
        self.lexicalAnalyser = LexicalAnalyser()
        self.sintacticAnalyser = SintacticAnalyser()
        self.answerAnalyser = AnswerAnalyser()
        self.exitoMsg = "No hay errores de validación por mostrar..."
    
    def setup(self):

        self.window.iconbitmap(os.path.abspath('resources/favicon.ico'))
        self.window.title("Universidad Central - Ingeniería de sistemas")
        self.window.geometry('500x520')
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
            width=47,
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
            state="normal",
            command=self.lexicalAssistant
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
            state="disabled",
            command=self.sintacticAssistant
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
            state="disabled",
            command=self.answerAssistant
        )
        self.btnAnswer.pack()
        self.btnAnswer.place(x=309, y=95)


        self.errorLabel = tk.Label(self.window, 
            text=self.exitoMsg, 
            font=("Calibri", 11, ''), 
            foreground="#333333", 
            width=400,
            background="#FFFFFF",
            borderwidth=0
        )
        self.errorLabel.pack(ipadx=0, ipady=8, padx=20)

    
        tk.Label(self.window, 
            text="Resultados", 
            font=("Calibri", 13, 'bold'), 
            foreground="#333333", 
            background="#FFFFFF",
            width=400,
            borderwidth=0
        ).pack(ipadx=0, ipady=8, padx=20, pady=(20,0))


        self.bgResults = tk.Label(self.window, 
            text="--------------------", 
            background="#FFFFFF",
            borderwidth=0
        )
        self.bgResults.pack()
        self.bgResults.place(x=20, y=310, width=460, height=190)


        self.resultFrame = tk.Frame(self.window, bg="#FFFFFF", bd=0, width=400)
        self.resultFrame.pack()

        
        self.title1 = tk.Label(self.resultFrame, 
            text="Oración",
            foreground="#333333",
            font=("Calibri", 10, 'bold'),
            background="#FFFFFF"
        )


        self.sentence = tk.Label(self.resultFrame, 
            text="--------------------",
            foreground="#333333",
            font=("Calibri", 10),
            background="#FFFFFF"
        )


        self.title2 = tk.Label(self.resultFrame, 
            text="Tokenización 1",
            foreground="#333333",
            font=("Calibri", 10, 'bold'),
            background="#FFFFFF"
        )


        self.token1 = tk.Label(self.resultFrame, 
            text="--------------------",
            foreground="#333333",
            font=("Calibri", 10),
            background="#FFFFFF"
        )


        self.title3 = tk.Label(self.resultFrame, 
            text="Análisis léxico",
            foreground="#333333",
            font=("Calibri", 10, 'bold'),
            background="#FFFFFF"
        )


        self.lexicResult = tk.Label(self.resultFrame, 
            text="--------------------",
            foreground="#333333",
            font=("Calibri", 10),
            background="#FFFFFF"
        )


        self.title4 = tk.Label(self.resultFrame, 
            text="Tokenización 2",
            foreground="#333333",
            font=("Calibri", 10, 'bold'),
            background="#FFFFFF"
        )


        self.token2 = tk.Label(self.resultFrame, 
            text="--------------------",
            foreground="#333333",
            font=("Calibri", 10),
            background="#FFFFFF"
        )


        self.title5 = tk.Label(self.resultFrame, 
            text="Análisis sintáctico",
            foreground="#333333",
            font=("Calibri", 10, 'bold'),
            background="#FFFFFF"
        )


        self.sintacticResult = tk.Label(self.resultFrame, 
            text="--------------------",
            foreground="#333333",
            font=("Calibri", 10),
            background="#FFFFFF"
        )


        self.title6 = tk.Label(self.resultFrame, 
            text="Tokenización 3",
            foreground="#333333",
            font=("Calibri", 10, 'bold'),
            background="#FFFFFF"
        )


        self.token3 = tk.Label(self.resultFrame, 
            text="--------------------",
            foreground="#333333",
            font=("Calibri", 10),
            background="#FFFFFF"
        )


        self.title7 = tk.Label(self.resultFrame, 
            text="Respuesta",
            foreground="#333333",
            font=("Calibri", 10, 'bold'),
            background="#FFFFFF"
        )


        self.answer = tk.Label(self.resultFrame, 
            text="--------------------",
            foreground="#333333",
            font=("Calibri", 10),
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

        self.window.geometry("+10+10")
        self.window.mainloop()

    def lexicalAssistant(self): 
        self.token1_Final = self.lexicalAnalyser.run(self)

    def sintacticAssistant(self):
        self.token2_Final = self.sintacticAnalyser.run(self)

    def answerAssistant(self):
        self.answerAnalyser.run(self)