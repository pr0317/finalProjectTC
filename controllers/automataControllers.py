from models.auto_lex import auto_Lex


class automataController:

    def esValido(self, variable):
        oracion = auto_Lex.valida(variable)
        return oracion.esValido()
    
    def tokenizado1(self, variable):
        tokenizated = auto_Lex.tokens()
        return tokenizated.tokenizado1()