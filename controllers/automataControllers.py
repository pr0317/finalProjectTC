from models.auto_reserved import automataReserved
from models.auto_entero import automataEntero
from models.auto_id import automataId

class automataController:

    def esReserved(self, reserved):
        reserved1 = automataReserved(reserved)
        return reserved1.reserved()

    def esEntero(self, variable):
        real1 = automataEntero(variable)
        return real1.Real()
    
    def esId(self, variable):
        id1 = automataId(variable)
        return id1.is_id()