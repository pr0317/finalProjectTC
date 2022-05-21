class Auto_Key:
   
    def __init__(self, texto):
        self.texto = texto
        self.estadoFinal = "B"
        self.error = ""
        self.correcto = False
        self.keys = ["interrogacion", "no_pasado"] 
        self.process()
 
    def process(self):
        self.estado = 'A'

        if self.texto in self.keys:
            self.estado = "B"
        else:
            self.error = "ninguno"

        if self.estado == self.estadoFinal and self.error == "":
            self.correcto = True
        else:
            self.correcto = False            