class auto_Id:

    def __init__(self, texto):
        self.texto = texto
        self.estadoFinal = "D"

    def isalpha(self, caracter):
        # letra(letra|digito)
        return (str.isalpha(caracter))

    def is_id(self):
        self.estado = 'A'

        for i in range(0, len(self.texto)):
            self.transicion = self.texto[i]

            if self.estado == "A":

                if self.isalpha(self.transicion):
                    self.estado = "B"
                else:
                    return "El carácter <" + self.transicion + "> en la posición " + str(i+1) + ", debe ser una letra"

            elif self.estado == "B":
                if self.isalpha(self.transicion):
                    self.estado = "C" #letra
                elif self.transicion.isnumeric:
                    self.estado = "D"  #digito --> aqui deberia entrar en la pos 1, q2
                else:
                    return "xxEl caracter <"+ self.transicion +">  en la posicion "+ str(+1) +", debe ser una letra o un digito"
            elif self.estado == "C":
                if self.isalpha(self.transicion):
                    self.estado = "C"
                elif self.transicion.isnumeric:
                    self.estado = "D"
                else:
                    return "El caracter <"+self.transicion+"> en la posicion "+str(i+1)+", debe ser una letra o un digito"
            elif self.estado == "D":
                if self.transicion.isnumeric:
                    self.estado = "D"
                elif self.transicion == str.isalpha:
                    self.estado = "C"
                else:
                    return "El caracter <"+self.transicion+"> en la posicion "+str(i+1)+", debe ser una letra o un digito"

        if self.estado == self.estadoFinal:
            return "Éxito: ¡El valor ingresado es un Identificador!"
        else:            
            return "Error: El valor ingresado no es un Identificador, el automata no completo todos los estados"