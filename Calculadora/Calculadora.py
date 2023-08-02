class Calculadora:

    def __init__(self, operacion):
        self.__operacion = operacion
        self.__operacionSeparada = []
        
    def calcular(self):
        self.__tratarOperacion()

        print(self.__operacion)

    
    '''
    __tratarOperacion
    Elimina los espacios en blanco de la cadena
    '''
    def __tratarOperacion(self):
        self.__operacion=self.__operacion.replace(" ","")

    