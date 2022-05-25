import os
import json

class SintacticAnalyser:
    def run(self, home):
        self.home = home
        self.terminales = ["$", "interrogacion","plural","que","una","el","su","un","estar","encendido","a","yo","usted","tema","conexion","internet","bombillo","router","servicio","mantenimiento","no_pasado","colaborar","tener","desear","en","de"]
        self.simboloInicial = "O"
        self.error = ""
        self.token2 = self.home.question.get("1.0",'end-1c')
        self.analizer()
        self.printValues()

    def buscar_table(self): # abre el .json con la informacion
        with open(os.path.abspath('resources/TAS.json'), encoding='utf-8-sig') as json_file:
            return json.load(json_file)

    def analizer(self):
        M = self.buscar_table()
        w = self.home.question.get("1.0",'end-1c').split(" ")
        n_w = self.home.question.get("1.0",'end-1c').split(" ")
        w.append("$") # w$
        n_w.append("$") # n_w$
        pila = ["$"]
        pila.append(self.simboloInicial)
        ae = w[0] # apunta ae al primer simbolo de w$
        X = ""
        n = len(w) # id + id * id $
        i = 0

        try:
            while X != "$" and i < n:
                X = pila[-1] # obtener el simbolo de la cima de la pila

                if(X in self.terminales or X == "$"):
                    if(X == ae):
                        pila.pop()
                        i = i + 1
                        if X != "$":
                            ae = w[i]
                            n_w.pop(0)
                    else:
                        self.error = "Error de sintáxis en la palabra " + ae
                        break
                else:
                    if M[X][ae] != "":
                        pila.pop()
                        if M[X][ae] != ["e"]:
                            for simbol in reversed(M[X][ae]):
                                pila.append(simbol)
                    else:
                        self.error = "Error de sintáxis en la palabra " + ae
                        break
        except:
            self.error = "Error general de sintáxis"

    def printValues(self):
        self.home.token3.config(text = '--------------------')
        self.home.answer.config(text = '--------------------')

        if self.error == "": # Proceso exitoso
            self.home.errorLabel.config(text = self.home.exitoMsg)
            self.home.token2.config(text = self.token2)
            self.home.sintacticResult.config(text = "Oración correcta sintácticamente")
            self.home.btnLexicalAnalysis.config(state = "normal")
            self.home.btnSintacticAnalysis.config(state = "normal")
            self.home.btnAnswer.config(state = "normal")
        else:
            self.home.errorLabel.config(text = self.error)
            self.home.token2.config(text = 'Error')
            self.home.sintacticResult.config(text = "Oración incorrecta sintácticamente")
            self.home.btnLexicalAnalysis.config(state = "normal")
            self.home.btnSintacticAnalysis.config(state = "normal")
            self.home.btnAnswer.config(state = "disabled")