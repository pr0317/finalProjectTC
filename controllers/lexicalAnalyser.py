from models.auto_id import Auto_Id
from models.auto_entero import Auto_Entero
from models.auto_key import Auto_Key

class LexicalAnalyser:
    def run(self, home):
        self.home = home
        self.error = ""
        self.question = home.question.get("1.0",'end-1c')
        self.generateToken1()
        self.printValues()
        return self.token1

    def generateToken1(self):
        self.token1 = []
        words = self.question.split(" ")
        self.counter = 0
        
        for word in words:
            self.counter = self.counter + 1
            autoKey = Auto_Key(word)
            autoId = Auto_Id(word)
            autoEntero = Auto_Entero(word)

            if autoKey.correcto == False and autoEntero.correcto == False and autoId.correcto == False:
                self.error = "Error léxico: Palabra " + word + " " + autoKey.error + ", INT: " + autoEntero.error + " ID: " + autoId.error
                break
            else:
                if autoKey.correcto == True:
                    self.token1.append("key")
                elif autoEntero.correcto == True:
                    self.token1.append("int")
                elif autoId.correcto == True:
                    self.token1.append("id")

    def printValues(self):
        self.home.sentence.config(text = self.question)
        self.home.token2.config(text = '--------------------')
        self.home.sintacticResult.config(text = '--------------------')
        self.home.token3.config(text = '--------------------')
        self.home.answer.config(text = '--------------------')

        if self.error == "": # Proceso exitoso
            self.home.errorLabel.config(text = self.home.exitoMsg)
            self.home.token1.config(text = ' '.join([str(elem) for elem in self.token1]))
            self.home.lexicResult.config(text = "Oración correcta " + str(self.counter) + " Palabra(s) analizada(s)")

            self.home.btnLexicalAnalysis.config(state = "normal")
            self.home.btnSintacticAnalysis.config(state = "normal")
            self.home.btnAnswer.config(state = "disabled")
        else:
            self.home.errorLabel.config(text = self.error)
            self.home.token1.config(text = 'Error')
            self.home.lexicResult.config(text = "Oración incorrecta " + str(self.counter) + " Palabra(s) analizada(s)")

            self.home.btnLexicalAnalysis.config(state = "normal")
            self.home.btnSintacticAnalysis.config(state = "disabled")
            self.home.btnAnswer.config(state = "disabled")