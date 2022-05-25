import os
import json
from tkinter import N

class AnswerAnalyser:
    def run(self, home):
        self.home = home
        self.question = home.question.get("1.0",'end-1c')
        self.error = ""
        self.answer = []
        self.stopwords = ["DET", "PREP"]
        self.constants = ["yo", "usted"]
        self.generarToken3()
        self.generarRespuesta()
        self.printValues()

    def getDB(self):
        with open(os.path.abspath('resources/KNOWLEDGE_BASE.json'), encoding='utf-8-sig') as json_file:
            return json.load(json_file)

    def getTerminals(self): # abre el .json con la informacion
        with open(os.path.abspath('resources/TERMINALS.json'), encoding='utf-8-sig') as json_file:
            return json.load(json_file)

    def generarToken3(self):
        self.token3 = []
        words = self.question.split(" ")

        for idx, item in enumerate(self.home.token2_Final):
            if words[idx] in self.constants:
                self.token3.append(words[idx])
            elif item is None or (item in self.stopwords or words[idx] in self.stopwords):
                self.token3.append(None)
            else:
                self.token3.append(item)

        self.token3String = ''
        for ittk in self.token3:
            if ittk is not None:
                if self.token3String == '':
                    self.token3String = ittk
                else:
                    self.token3String = self.token3String + ' ' + ittk

    def generarRespuesta(self):
        knowledgeBase = self.getDB()
        pregunta = self.question.split(" ")
        token2 = self.home.token2_Final
        token3 = self.token3

        try:
            for key,item in enumerate(token2):
                if item is not None:
                    itemToken3 = token3[key]
                    itemPregunta = pregunta[key]
                    if itemToken3 in self.constants: # Es una constante
                        self.answer.append(itemToken3)
                    elif itemPregunta in knowledgeBase["verbos"]:
                        palabraAsociada = knowledgeBase["verbos"][itemPregunta]
                        self.answer.append(palabraAsociada)
                        if palabraAsociada in knowledgeBase["palabras_asociadas"]:
                            self.answer.append(knowledgeBase["palabras_asociadas"][palabraAsociada])
                    elif (key+1) == len(token2): # Es el ultimo
                        dato = self.answer[len(self.answer)-4]
                        if dato in knowledgeBase["datos"]:
                            self.answer.append(knowledgeBase["datos"][dato])
                    else:
                        terminales = self.getTerminals()
                        for terminal in terminales:
                            if terminal["name"] == item: # Busca el valor en terminales
                                self.answer.append(terminal["content"][0])
        except:
            self.error = "No es posible responder la pregunta en estructura profunda"

    def printValues(self):
        if self.error == "": # Proceso exitoso
            self.home.errorLabel.config(text = self.home.exitoMsg)
            self.home.token3.config(text = self.token3String)
            self.home.answer.config(text = ' '.join([str(elem) for elem in self.answer]))
        else:
            self.home.errorLabel.config(text = self.error)
            self.home.token3.config(text = 'Error')
            self.home.answer.config(text = "No fue posible imprimir la respuesta")