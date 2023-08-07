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
        self.operadoresSumRest=['+', '-']
        self.operadoresMultDiv=['*', '/']

    '''
    tratarOperacion()
    Elimina los espacios en blanco de la cadena y lo convertimos en vector de numpy
    '''
    def tratarOperacion(self):
        self.__operacion=[self.__operacion.replace(" ","")] 
    
    '''
    calcular()
    Calcula la operación pedida: trata la operacion para quitarle espacios en blanco y realiza la operacion 
    descomponiendola en operaciones mas sencillas.
    '''    
    def calcular(self):
        Operaciones=[]
        Operadores=[]
        Operaciones2=[]
        Operadores2=[]
        self.tratarOperacion() #Elimina espacios en blanco
        Operaciones,Operadores=self.descomponerOperacion(self.__operacion,self.operadoresSumRest)
        Operaciones2,Operadores2=self.descomponerOperacion(Operaciones,self.operadoresMultDiv)
        print(Operadores)
        print(Operaciones)
        print(Operadores2)
        print(Operaciones2)

    def descomponerOperacion(self,operacionADescomponer,OperadoresDescomponedor):
        Operadores=[]
        Operaciones=[]
        Operadores=self.obtenerOperadores(operacionADescomponer,OperadoresDescomponedor)
        Operaciones=self.obtenerOperaciones(operacionADescomponer,OperadoresDescomponedor)
        return Operaciones,Operadores

    def obtenerOperadores(self,operacionADescomponer,OperadoresAObtener):
        ListaOperadoresCuentas=[]
        for operacion in operacionADescomponer:
            OperadoresCuenta=[]
            for caracter in operacion:
                if caracter in OperadoresAObtener:
                    OperadoresCuenta.append(caracter)
            
            if(len(OperadoresCuenta)>0):
                ListaOperadoresCuentas.append(OperadoresCuenta)

        return ListaOperadoresCuentas

    def obtenerOperaciones(self,operacionADescomponer,OperadoresDescomponedor):
        ListaOperacionesCuentas=[]
        for operacion in operacionADescomponer:
            OperacionesCuenta=[]
            if(self.hayOperacion(operacion,OperadoresDescomponedor)):
                for caracter in operacion:
                    if caracter not in OperadoresDescomponedor:
                        OperacionesCuenta.append(caracter)
                    else:
                        ListaOperacionesCuentas.append(OperacionesCuenta)
                        OperacionesCuenta=[]
                
                ListaOperacionesCuentas.append(OperacionesCuenta) #Para añadir el ultimo número de cada operacion

        return ListaOperacionesCuentas


    def hayOperacion(self,operacion,operadoresDescomponedor):
        hayOperacion=False
        for caracter in operacion:
            if caracter in operadoresDescomponedor:
                hayOperacion=True

        return hayOperacion




































    
    

        
    
   
    
'''    
    ____obtenerOperadores()
    Obtiene los operaciores de la operacion
    
    def __obtenerOperadores(self,operacion,operadoresAObtener):
        operadoresConseguidos=[]
        for caracter in operacion:
            if caracter in operadoresAObtener:
                operadoresConseguidos.append(caracter)
        return operadoresConseguidos

    
    ____obtenerNúmeros()
    Obtiene los números de la operacion
    
    def __obtenerOperacionesMultDiv(self,OperadoresDivisores):
        operacion=""
        for caracter in self.__operacion:
            if(caracter in OperadoresDivisores):
                self.__operacionesMultDiv.append(operacion)
                operacion=""
            else:
                operacion+=caracter
        self.__operacionesMultDiv.append(operacion) #Para añadir el ultimo número de la operacion

    def __calcularMultiplicacionesDivisiones(self):
        operadoresConseguidos=[]
        #Recorrer las operaciones de multiplicaciónDvisiton
        for operacionMulDiv in self.__operacionesMultDiv:
            if(self.__hayOperacion(operacionMulDiv,self.__operadoresMultDiv)):#Si hay operacion
                #Conseguir los numeros
                operadoresConseguidos=self.__obtenerOperadores(operacionMulDiv,self.__operadoresMultDiv)
                #Realizar operacion
                #Actualizar vector de operaciones

    def __hayOperacion(self,operacion,operadoresABuscar):
        hayOperacion=False
        for caracter in operacion:
            if caracter in operadoresABuscar:
                hayOperacion=True
        return hayOperacion
    
    ____obtenerNúmeros()
    Obtiene los números de la operacion
    
    def __obtenerNumeros(self):
        numero=""
        for operacion in self.__operacion:
            if(operacion in self.__operadoresUsados):
                self.__Numeros.append(float(numero))
                numero=""
            else:
                numero+=operacion
        self.__Numeros.append(float(numero)) #Para añadir el ultimo número de la operacion

    ''''''
    ____operaciones()
    Realiza el cálculo de la operacion
   
    def __Realizaroperaciones(self,numeros,operadores):
        resultado=0
        while(len(self.__Numeros)>1):
            operando1=numeros[0]
            operando2=numeros[1]
            if operadores[0] == '+':
                resultado=self.__suma(operando1,operando2)
            elif(operadores[0] == '-'):
                 resultado=self.__resta(operando1,operando2)
            elif(operadores[0] == '*'):
                 resultado=self.__multiplicacion(operando1,operando2)
            elif(operadores[0] == '/'):
                 resultado=self.__division(operando1,operando2)


            operadores.pop(0)
            numeros.pop(0) #Se borra el primer numero de la operacion
            numeros.pop(0) #Se borra el segundo numero de la operacion
            numeros.insert(0,resultado)
            print(numeros)

        return resultado
    
    def __suma(self,op1,op2):
        return op1+op2
    
    def __resta(self,op1,op2):
        return op1-op2
    
    def __multiplicacion(self,op1,op2):
        return op1*op2
    
    def __division(self,op1,op2):
        return op1/op2'''