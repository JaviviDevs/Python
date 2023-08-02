'''
Calculadora
Calcula la operacion pedida
'''
class Calculadora:

    '''
    __init__()
    Contrcutor de la clase
    @param operacion: operacion a realizar
    '''
    def __init__(self, operacion):
        self.__operacion = operacion
        self.__Numeros = []
        self.__operadores = []
        self.__operadoresUsados=['+', '-', '*', '/']
        
    '''
    __calcular()
    Calcula la operación pedida: trata la operacion para quitarle espacios en blanco, obtiene los números
    y operadores y realiza los cálculos.
    '''    
    def calcular(self):
        self.__tratarOperacion() #Elimina espacios en blanco
        self.__obtenerOperadores() #Obtiene los operadores
        self.__obtenerNumeros() #Obtiene los números

        print(self.__operacion)
        print(self.__Numeros)
        print(self.__operadores)

        print(self.__operaciones()) #Realiza el cálculo
        
    
    '''
    __tratarOperacion()
    Elimina los espacios en blanco de la cadena
    '''
    def __tratarOperacion(self):
        self.__operacion=self.__operacion.replace(" ","")
    
    '''
    ____obtenerOperadores()
    Obtiene los operaciores de la operacion
    '''
    def __obtenerOperadores(self):
        for caracter in self.__operacion:
            if caracter in self.__operadoresUsados:
                self.__operadores.append(caracter)

    '''
    ____obtenerNúmeros()
    Obtiene los números de la operacion
    '''
    def __obtenerNumeros(self):
        numero=""
        for operacion in self.__operacion:
            if(operacion in self.__operadoresUsados):
                self.__Numeros.append(float(numero))
                numero=""
            else:
                numero+=operacion
        self.__Numeros.append(float(numero)) #Para añadir el ultimo número de la operacion

    '''
    ____operaciones()
    Realiza el cálculo de la operacion
    '''
    def __operaciones(self):
        resultado=0
        while(len(self.__Numeros)>1):
            operando1=self.__Numeros[0]
            operando2=self.__Numeros[1]
            if self.__operadores[0] == '+':
                resultado=self.__suma(operando1,operando2)
            elif(self.__operadores[0] == '-'):
                 resultado=self.__resta(operando1,operando2)

            self.__operadores.pop(0)
            self.__Numeros.pop(0) #Se borra el primer numero de la operacion
            self.__Numeros.pop(0) #Se borra el segundo numero de la operacion
            self.__Numeros.insert(0,resultado)
            print(self.__Numeros)

        return resultado
    
    def __suma(self,op1,op2):
        return op1+op2
    
    def __resta(self,op1,op2):
        return op1-op2