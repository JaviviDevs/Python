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
        self.operadores=['+', '-','*', '/']

    '''
    tratarOperacion()
    Elimina los espacios en blanco de la cadena y lo convertimos en vector de numpy
    '''
    def tratarOperacion(self):
        self.__operacion=[self.__operacion.replace(" ","")] 
    
    def tratarDimensiones(self,Operaciones,Operadores):
        OperacionesTratadas=[]
        OperadoresTratados=[]
        
        for Operacion in Operaciones:
            OperacionesTratadas.append(Operacion[0])
        
        for Operadors in Operadores[0]:
            OperadoresTratados.append(Operadors)

        return OperacionesTratadas,OperadoresTratados
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
        self.sustituirOperacionesPorResultado(Operaciones,Operaciones2,Operadores2,self.operadoresMultDiv)

        if(len(Operadores))>0:
            OperacionesTratadas,OperadoresTratados=self.tratarDimensiones(Operaciones,Operadores)
            print(OperacionesTratadas,OperadoresTratados)
            print(self.realizarOperacion(OperacionesTratadas,OperadoresTratados))
        else:
            OperacionesTratadas,OperadoresTratados=self.tratarDimensiones(Operaciones,Operadores2)
            print(OperacionesTratadas,OperadoresTratados)
            print(OperacionesTratadas[0])
        

    #************************* PROCESO DE DESCOMPOSICION DE LA OPERACION ************************
    '''
    descomponerOperacion()
    Descompone una operacion en operaciones más simples
    @param operacionADescomponer: operacion a descomponer en operaciones más sencillas
    @param operadoresDescomponedor: operadores que dividen la operación en otras mas sencillas
    @return Operaciones: matriz que almacena las operaciones sencillas en las que se ha dividido la operacion
    @return Operadores: matriz que almacena los operadores que han servido para descomponer la operacion
    '''
    def descomponerOperacion(self,operacionADescomponer,OperadoresDescomponedor):
        Operadores=[]
        Operaciones=[]
        Operadores=self.obtenerOperadores(operacionADescomponer,OperadoresDescomponedor)
        Operaciones=self.obtenerOperaciones(operacionADescomponer,OperadoresDescomponedor)
        return Operaciones,Operadores

    '''
    obtenerOperadores()
    Obtiene los operadores que descomponen la operacion
    @param operacionADescomponer: operacion a descomponer en operaciones más sencillas
    @param operadoresAObtener: tipo de operadores que quieren obtenerse
    @return ListaOperadoresCuentas: matriz que almacena los operadores que han servido para descomponer la operacion
    '''
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

    '''
    obtenerOperaciones()
    Obtiene las operaciones sencillas en las que se descompuso la operacion
    @param operacionADescomponer: operacion a descomponer en operaciones más sencillas
    @param operadoresDescomponedor: operadores que dividen la operación en otras mas sencillas
    @return Operaciones: matriz que almacena las operaciones sencillas en las que se ha dividido la operacion

    Cuando el operadores es una suma recta, ej: 6+5*4+3*2 devuelve: [[6],[5,*,4],[3,*,2]]
    Cuando el operadores es una multiplicacion division, ej: [[6],[5,*,4],[3,*,2]] devuelve: [[5,4],[3,2]]
    es decir, como se ve en los condicionales, descompone de manera diferente las operaciones:
    descompone de una manera las sumas y restas, y de otra la division y multiplicación, todo esto
    para tener una estructura de datos favorable para calcular las operaciones. 
    Ya que si se descompusiesen igual, para la operación  6+5*4+3*2*2 ocurriria lo siguiente:
    6+5*4+3*2*2-->[[6],[5,*,4],[3,*,2,*,2]] -->[[5],[4],[3],[2],[2]] y de esta manera, no se sabe
    si por ejemplo la operacion es 5*4*3 y luego otra 2*2 o si es 5*4, y luego 3*2*2.

    '''
    def obtenerOperaciones(self,operacionADescomponer,OperadoresDescomponedor):
        ListaOperacionesCuentas=[]
        for operacion in operacionADescomponer:
            OperacionesCuenta=[]
            numero=""
            if(self.hayOperacion(operacion)):
                for caracter in operacion:
                    if caracter not in self.operadores:
                        numero+=caracter
                    else:
                        OperacionesCuenta.append(numero)
                        numero=""

                        if caracter not in OperadoresDescomponedor:
                            OperacionesCuenta.append(caracter)
                        elif(caracter not in self.operadoresMultDiv):
                            ListaOperacionesCuentas.append(OperacionesCuenta)
                            OperacionesCuenta=[]

                #Para añadir el ultimo número de cada operacion
                OperacionesCuenta.append(numero) 
                ListaOperacionesCuentas.append(OperacionesCuenta) 

        return ListaOperacionesCuentas

    '''
    hayOperacion()
    Para un elemento de la matriz que contiene las operaciones simplificadas, detecta si hay una operacion
    o no. Por ejemplo [[7],[5,*,6]]: 7 --> devuelve False mientras 5*6 devuelve True
    @param operacion: elemento de la matriz de operaciones a analizar
    @return hayOp: True si encuentra el operador, false si no.
    '''
    def hayOperacion(self,operacion):
        hayOp=False
        for caracter in operacion:
            if caracter in self.operadores:
                hayOp=True

        return hayOp

    #**********************************************************************************************
    #************************** METODOS PARA REALIZAR LAS OPERACIONES *****************************
    

    def sustituirOperacionesPorResultado(self,operacionesASustituir,operaciones,operadores,operadorABuscar):
        resultados=[]
        for operacion,operadors in zip(operaciones,operadores):
            # Los corchetes son para forzar que el formato del vector operacionesASustituir sea para 
            # el ejemplo 3*4*4+5*5*5
            # [[3],[16],[125]], sino acabaria siendo [[3],16,125] y daría problemas con la indexación.
            resultados.append([self.realizarOperacion(operacion,operadors)]) 

        posicionOperaciones=0
        while(len(resultados)>0):
            if(self.hayOperacion(operacionesASustituir[posicionOperaciones])):
                resultado=resultados.pop(0)
                operacionesASustituir[posicionOperaciones]=resultado

            posicionOperaciones=posicionOperaciones+1

        print("OPERACIONES FINAL")
        print(operacionesASustituir)

    '''
    Realizaroperacion()
    Realiza las operaciones suma, resta, multiplicación y división.
    @param numeros: lista de números de la operacion.Ej: [5,6,7,8]
    @param operadores: lista de operadores de la operación [*,*,/]
    @return resultado: resultado de la operacion
    '''
    def realizarOperacion(self,operacion,operadores):
        numeros=operacion.copy()
        operadors=operadores.copy()
        resultado=0
        while(len(numeros)>1):
            operando1=float(numeros.pop(0)) #Se borra el primer numero de la operacion
            operando2=float(numeros.pop(0)) #Se borra el segundo numero de la operacion
            operador=operadors.pop(0)
            if operador == '+':
                resultado=self.suma(operando1,operando2)
            elif(operador== '-'):
                 resultado=self.resta(operando1,operando2)
            elif(operador== '*'):
                 resultado=self.multiplicacion(operando1,operando2)
            elif(operador== '/'):
                 resultado=self.division(operando1,operando2)
                 
            numeros.insert(0,resultado)

        return resultado
    
    '''
    suma()
    Hace la suma de dos números (dos operandos)
    @param op1: operandos1
    @param op2: operandos2
    @return op1+op2: Suma de los operandos
    '''
    def suma(self,op1,op2):
        return op1+op2
    
    '''
    resta()
    Hace la resta de dos números (dos operandos)
    @param op1: operandos1
    @param op2: operandos2
    @return op1+op2: Resta de los operandos
    '''
    def resta(self,op1,op2):
        return op1-op2
    

    '''
    multiplicacion()
    Hace la multiplicacion de dos números (dos operandos)
    @param op1: operandos1
    @param op2: operandos2
    @return op1+op2: Multiplica de los operandos
    '''
    def multiplicacion(self,op1,op2):
        return op1*op2
    
    '''
    division()
    Hace la suma de dos números (dos operandos)
    @param op1: operandos1
    @param op2: operandos2
    @return op1+op2: Suma de los operandos
    '''
    def division(self,op1,op2):
        return op1/op2

































    
    

        
    