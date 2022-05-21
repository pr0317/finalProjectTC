class Auto_Entero:
    def __init__(self, cadena):
        self.cadena = cadena
        self.estadoFinal = "D"
        self.error = ""
        self.correcto = False
        self.process()

    def process(self):
        self.estado = "A"
        for i in range(0, len(self.cadena)):
            self.transicion = self.cadena[i]
            if self.estado == "A":
                if self.transicion == "+":
                    self.estado = "B"
                elif self.transicion == "-":
                    self.estado = "C"
                elif str.isdigit(self.transicion):
                    self.estado = "D"
                else:
                    self.error = "carácter " + str(i+1)
                    break
            elif self.estado == "B":
                if str.isdigit(self.transicion):
                    self.estado = "D"
                else:
                    self.error = "carácter " + str(i+1)
                    break
            elif self.estado == "C":
                if str.isdigit(self.transicion):
                    self.estado = "D"
                else:
                    self.error = "carácter " + str(i+1)
                    break
            elif self.estado == "D":
                if str.isdigit(self.transicion):
                    self.estado = "D"
                else:
                    self.error = "carácter " + str(i+1)
                    break

        if self.estado == self.estadoFinal and self.error == "":
            self.correcto = True
        else:
            self.correcto = False