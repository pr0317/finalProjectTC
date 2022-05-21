class Auto_Id:

    def __init__(self, texto):
        self.texto = texto
        self.estadosFinales = ["B","C","D"]
        self.error = ""
        self.correcto = False
        self.process()

    def process(self):
        self.estado = 'A'

        for i in range(0, len(self.texto)):
            self.transicion = self.texto[i]

            if self.estado == "A":
                if self.isalpha(self.transicion):
                    self.estado = "B"
                else:
                    self.error = "carácter " + str(i+1)
                    break
            elif self.estado == "B":
                if self.isalpha(self.transicion):
                    self.estado = "C"
                elif self.transicion.isnumeric():
                    self.estado = "D" #digito --> aqui deberia entrar en la pos 1, q2
                else:
                    self.error = "carácter " + str(i+1)
                    break
            elif self.estado == "C":
                if self.isalpha(self.transicion):
                    self.estado = "C"
                elif self.transicion.isnumeric():
                    self.estado = "D"
                else:
                    self.error = "carácter " + str(i+1)
                    break
            elif self.estado == "D":
                if self.transicion.isnumeric():
                    self.estado = "D"
                elif self.isalpha(self.transicion):
                    self.estado = "C"
                else:
                    self.error = "carácter " + str(i+1)
                    break

        if self.estado in self.estadosFinales and self.error == "":
            self.correcto = True
        else:            
            self.correcto = False

    def isalpha(self, caracter):
        return (str.isalpha(caracter))