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
    def __init__(self):
        self.sigSumRest=['+', '-']
        self.sigMultDiv=['*', '/']
        self.signos=['+', '-','*', '/']

    
    '''
    tratarOperacion()
    Elimina los espacios en blanco de la cadena y la operacion se convierte en una matriz bidimensional.
    La intención de esto es para que el mismo método que descompone la operación en otras más sencillas
    sirva tanto para descomponer la operación por primera vez, como para las siguientes veces.
    Ej: [[5+5*5+6*6]] -->[[5,5*5,6*6]] --> [[5,5],[6,6]]
    @param opAtratar: operacion a la que se le va a quitar los espacios en blanco y
    convertirla en una matriz
    @return op: misma operación pero sin espacios en blanco y en forma de matriz
    '''
    def tratarOperacion(self,opATratar):
        op=[[opATratar.replace(" ","")]] 
        return op

    '''
    operacionesCombinadas()
    Determina si la operación es simple (solo suma y restas o multiplicaciones y divisiones) o si es
    una operación que combina varios operadores.
    @param: operación a determinar si es combinada o simple
    @return opComb: false --> operación simple, true --> operación combinada
    '''
    def operacionesCombinadas(self,operacion):
        opComb=False
        if self.hayOperador(operacion,self.sigSumRest) and self.hayOperador(operacion,self.sigMultDiv):
            opComb=True
        return opComb
    
    '''
    hayOperador()
    Determina si en una operación se halla un operador determinado
    @param operacion: operación donde buscar el operador
    @param tipoOperador: tipo de operador a buscar. Puede ser [+,-], [*,/] o [+,-,*,/]
    @return hayOp: true--> hay operador, false --> no hay operador
    '''
    def hayOperador(self,operacion,tipoOperador):
        hayOp=False
        for caracter in operacion:
            if caracter in tipoOperador:
                hayOp=True
        return hayOp
    

    ##################################################################################################
    ##################################################################################################
    '''
    calcularOperacion()
    Calcula la operación pedida: trata la operacion para quitarle espacios en blanco 
    y realiza la operacion descomponiendola en operaciones mas sencillas si es necesario.
    @param opACalcular: operación a calcular
    @return resultadoFinal: resultado de la operación
    '''    
    def calcularOperacion(self,opACalcular):
        opACalcular=self.tratarOperacion(opACalcular) #Elimina espacios en blanco
        if self.operacionesCombinadas(opACalcular[0][0]):
            operaciones,signos=self.descomponerOperacion(opACalcular,self.sigSumRest)
            NumerosMultDiv,SignosMultDiv=self.descomponerOperacion(operaciones,self.sigMultDiv)
            #print(signos)
            #print(operaciones)
            self.sustituirOperacionesPorResultado(operaciones,NumerosMultDiv,SignosMultDiv)
            #print(SignosMultDiv)
            #print(NumerosMultDiv)
        else:
            if self.hayOperador(opACalcular[0][0],self.sigSumRest):
                operaciones,signos=self.descomponerOperacion(opACalcular,self.sigSumRest)
            else:
                operaciones,signos=self.descomponerOperacion(opACalcular,self.sigMultDiv)
            #print(signos)
            #print(operaciones)
            
        resultadoFinal=self.realizarOperacion(operaciones[0],signos[0])
        #print(resultadoFinal) 
        return resultadoFinal


       

    # ************************* PROCESO DE DESCOMPOSICION DE LA OPERACION ************************
    '''
    descomponerOperacion()
    Descompone una operacion en operaciones más simples
    @param opADesc: operacion a descomponer en operaciones más sencillas
    @param signosDesc: operadores que dividen la operación en otras mas sencillas
    @return opsNums: matriz que almacena las operaciones sencillas/números de una operación simple
    en las que se ha dividido la operacion
    @return signos: matriz que almacena los operadores que han servido para descomponer la operacion
    '''

    def descomponerOperacion(self,opADesc,signosDesc):
        signos=[]
        opsNums=[]
        for operacion in opADesc[0]:
            if(self.hayOperador(operacion,self.signos)): #Para eliminar elementos que no presentan ninguna operacion por ejemplo [[3],[3*7]]
                signos.append(self.obtenerOperadores(operacion,signosDesc))
                opsNums.append(self.obtenerOperaciones(operacion,signosDesc))

        return opsNums,signos

    '''
    obtenerOperadores()
    Obtiene los operadores que descomponen la operacion
    @param opADesc: operacion a descomponer en operaciones más sencillas
    @param signosAObt: tipo de operadores que quieren obtenerse
    @return operadores: vector que almacena los operadores que han servido para 
    descomponer la operacion
    '''

    def obtenerOperadores(self,opADesc,signosAObt):
        operadores=[]
        for caracter in opADesc:
            if caracter in signosAObt:
                operadores.append(caracter)

        return operadores

    
    '''
    obtenerOperaciones()
    Obtiene las operaciones sencillas en las que se descompuso la operacion 
    o números de una operación sencilla 
    @param opADesc: operacion a descomponer en operaciones más sencillas
    @param signosDesc: operadores que dividen la operación en otras mas sencillas
    @return Operaciones: vector que almacena las operaciones sencillas en las que se ha dividido la operacion

    Recorre letra a letra la operación, si no es un signo, significa que es un número por tanto
    va añadiendo digitos a la variable número. Cuando se encuentre con un signo, si es un signo 
    que no se usa para descomponer la operación, se mete en la operación el número y el operador, y 
    la operación sigue.
    En caso de que si sea un signo que se usa para descomponer, añades al vector la operación.
    '''
    def obtenerOperaciones(self,opADesc,signosDesc):
        opsNums=[]
        numero=""
        operacion=""
        for caracter in opADesc:
            if caracter not in self.signos:
                numero+=caracter
            else:
                if caracter in signosDesc:
                    operacion+=numero
                    opsNums.append(operacion)
                    operacion=""
                else:
                    operacion+=numero
                    operacion+=caracter
                
                numero=""
                      
        #Para añadir el último numero de la ultima operacion, y la ultima operacion
        operacion+=numero
        opsNums.append(operacion)
        return opsNums
    

    #************************** METODOS PARA REALIZAR LAS OPERACIONES *****************************
    '''
    sustituirOperacionesPorResultado()
    Sustituye las suboperaciones de la operación principal por sus resultados
    @param opsASustituir: operación principal que contiene suboperaciones a sustituir.Ej: [[5,5*6/5,4*4]]
    @param operaciones: operandos de las operaciones a calcular.Ej:  [[5,6,5][4,4]]
    @param signos: operadores de las operaciones a calcular. Ej: [[*,/],[*]]
    '''
    def sustituirOperacionesPorResultado(self,opsASustituir,operaciones,signos):
        resultados=self.calcularResultados(operaciones,signos)
        posicionOperaciones=0
        while(len(resultados)>0):
            if(self.hayOperador(opsASustituir[0][posicionOperaciones],self.signos)):
                resultado=resultados.pop(0)
                opsASustituir[0][posicionOperaciones]=resultado

            posicionOperaciones=posicionOperaciones+1

    '''
    calcularResultados()
    Calcula el conjunto de resultados de todas las suboperaciones pendientes.
    @param operaciones: operandos de las operaciones a calcular.Ej:  [[5,6,5][4,4]]
    @param signos: operadores de las operaciones a calcular. Ej: [[*,/],[*]]
    @return resultados: conjunto de resultados de las operaciones. Ej: [6,16]
    '''
    def calcularResultados(self,operaciones,signos):
        resultados=[]
        for operacion,operadors in zip(operaciones,signos):
            resultados.append(self.realizarOperacion(operacion,operadors)) 
        return resultados
    
    '''
    RealizarOperacion()
    Realiza las operaciones suma, resta, multiplicación y división.
    @param numeros: lista de números de la operacion.Ej: [5,6,7,8]
    @param operadores: lista de operadores de la operación [*,*,/]
    @return resultado: resultado de la operacion
    '''
    def realizarOperacion(self,op,signos):
        numeros_op=op.copy()
        signos_op=signos.copy()
        resultado=0
        while(len(numeros_op)>1):
            operando1=float(numeros_op.pop(0)) #Se borra el primer numero de la operacion
            operando2=float(numeros_op.pop(0)) #Se borra el segundo numero de la operacion
            signo=signos_op.pop(0)
            if signo == '+':
                resultado=self.suma(operando1,operando2)
            elif(signo== '-'):
                 resultado=self.resta(operando1,operando2)
            elif(signo== '*'):
                 resultado=self.multiplicacion(operando1,operando2)
            elif(signo== '/'):
                 resultado=self.division(operando1,operando2)
                 
            numeros_op.insert(0,resultado)

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
    
    