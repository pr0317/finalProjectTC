class auto_Entero:
    def __init__(self, cadena):
        self.cadena = cadena
        self.estadoFinal = "D"

    def Entero(self):
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
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser un dígito, un símbolo + o símbolo -"
            elif self.estado == "B":
                if str.isdigit(self.transicion):
                    self.estado = "D"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser unicamente dígito"
            elif self.estado == "C":
                if str.isdigit(self.transicion):
                    self.estado = "D"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser unicamente dígito"
            elif self.estado == "D":
                if str.isdigit(self.transicion):
                    self.estado = "D"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser unicamente dígito"

        if self.estado == self.estadoFinal:
            return "Éxito: ¡El valor ingresado es un número entero!"
        else:
            return "Error: El valor ingresado no corresponde a un tipo entero, el automata no completo todos los estados"