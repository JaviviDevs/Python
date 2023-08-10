from Calculadora import Calculadora

class CalculadoraCientifica:
    
    '''
    __init__()
    Contrcutor de la clase
    @param operacion: operacion a realizar
    '''
    def __init__(self, operacion):
        self.operacion = operacion
        self.calculadora=Calculadora()
        self.parentesis=['(',')']

    '''
    comprobarParentesis()
    Comprueba que todos los paréntesis estén bien, es decir que todo paréntesis abierto
    sea cerrado
    '''
    def comprobarParentesis(self):
        error=False
        parenAb=0
        parenCerr=0
        for caracter in self.operacion:
            if caracter == self.parentesis[0]:
                parenAb+=1
            elif caracter == self.parentesis[1]:
                parenCerr+=1
        
        if(parenAb != parenCerr):
            error=True

        return error

    '''
    comprobarSignos()
    Comprueba que no hay dos signos seguidos
    '''
    def comprobarSignos(self):
        error=False
        numSignosSeguidos=0
        for caracter in self.operacion:
            if caracter in self.calculadora.signos:
                numSignosSeguidos+=1
            else:
                numSignosSeguidos=0

            if(numSignosSeguidos==2):
                error=True
                break

        return error

    '''
    comprobarFormato()
    Comprueba que el formato de la operacion es correcto(parentesis y signos en orden)
    '''
    def comprobarFormato(self):
        error=False
        if(self.comprobarParentesis()==True or self.comprobarSignos()==True):
            error=True
        return error
    
    '''
    calcular()
    Comprueba si la operación tiene el formato correcto y realiza la operacion
    '''
    def calcular(self):
        synTaxError=self.comprobarFormato() #Se comprueba si el formato es correcto
        if synTaxError==False: #Si el formato es correcto
            opsJer=self.crearJerarquiaOps() #Tratas la operacion para calcularla
            for filaOp in opsJer:
                print(filaOp)
            resultado=self.calcularOpJerarquia(opsJer) #Calculas la operacion
            print(resultado)
        else: #Si no
            print("Systax Error") #Error


    # ************************* PROCESO DE CREACCION DE LA JERARQUIA ************************
    '''
    crearJerarquiOps()
    Crea la jerarquia de operaciones, donde a las diferentes operaciones 
    se le asigna un nivel en función del nivel de anidacion de los paréntesis que contienen 
    la operacion
    @return opsJer: Matriz bidimensional que contiene la jerarquia de operaciones segun niveles
    '''
    def crearJerarquiaOps(self):
        opsJer=self.crearNivelesJer() #Inicializas la jerarquia, estableciendo todos los niveles
        nivel=0
        operacion=""
        for caracter in self.operacion:
            if caracter not in self.parentesis:
                operacion+=caracter
            else:
                if caracter == self.parentesis[0]: #Si caracter = (
                    opsJer[nivel].append(operacion) #Se añade la operacion
                    opsJer[nivel].append('S') #Se añade S, que sera sustituido por el resultado correspondiente 
                    operacion=""    
                    nivel+=1   #Aumentamos 1 el nivel
                
                if caracter == self.parentesis[1]: #Si caracter = )
                    #El "" es para el caso de que se cierran los parentesis, ej : 5+(7+(8)),
                    #pues al ser dos )) seguidos, en el nivel anterior , ya que se sube de nivel
                    #cada vez que hay un ), se añade "" y esto no es deseable.
                    if(operacion!=""):
                        opsJer[nivel].append(operacion) #Se añade la operacion
                        operacion=""
                    nivel-=1 #Disminuimos un nivel
        
        #Añadir la ultima operacion tras el último paréntesis cerrado   
        if(operacion!=""):         
            opsJer[nivel].append(operacion)    
        return opsJer
    
    '''
    crearNivelesJer()
    Crea los diferentes niveles de la jerarquia de operaciones
    @return jerarquia: matriz bidimensional de una columna y cuyo numero de filas = niveles
    '''
    def crearNivelesJer(self):
        numParenAnidados=self.comprobarNumParenAnidados()
        jerarquia=[]
        for nivel in range(numParenAnidados+1): #+1 nivel donde no haya parentesis
            jerarquia.append([nivel])

        return jerarquia
    
    '''
    comprobarNumParenAnidados()
    Calcula el mayor número de paréntesis anidados en la operacion
    @return niveles: mayor número de paréntesis anidados
    '''
    def comprobarNumParenAnidados(self):
        parenAnidados=0
        vParenAnidados=[]
        niveles=1
        for caracter in self.operacion:
            if caracter == self.parentesis[0]:
                parenAnidados+=1
            if caracter == self.parentesis[1]:
                vParenAnidados.append(parenAnidados)
                parenAnidados=0

        #Se ordena el vector que contiene el conjunto de parentesis anidados de mayor a menor, y se
        # devuelve el primer elemento, es decir el mayor número de paréntesis anidados.
        #Ej: (1(2))+(1(2(3)))+(1(2(3(4)))) --> El vector almacenara [2,3,4], ordenado [4,3,2]
        #y devuelve 4
        vParenAnidados.sort(reverse=True) 
        if len(vParenAnidados)>0:
            niveles=vParenAnidados[0]
        return niveles
    
    #**************************************************************************************************

    #********************************************* PROCESO DE CALCULO *********************************

    '''
    calcularOpJerarquia() 
    Calcula las operaciones segun el nivel de la jerarquia dando lugar al resultado final de la operacion
    Se empieza por el nivel mas alto (mayor número) y se asciende por los diferentes niveles hasta llegar al
    nivel 0. En cada nivel la S es sustituida por los resultados del nivel anterior.
    '''
    def calcularOpJerarquia(self,opsJer):
        resultado=0
       
        #1. Recorrer la jerarquia de abajo a arriba
        for nivel in range(len(opsJer)-1, -1, -1): #Itera del mayor nivel(len(opsJer)-1) al 0 (-1+1) en orden decreciente(-1)
            #2. Calcular operaciones de la jerarquia de ese nivel.

            #Para el primer nivel de todos
            if nivel==0:
                # Una vez resueltos todos los paréntesis solo hace falta 
                # concatenar todo y calcular la última operacion
                opsJer=self.concatenarOps(opsJer)
                operacion=opsJer[nivel].pop(1) # Obtengo la operacion
                resultado=self.calculadora.calcularOperacion(operacion) #Calculo la operacion

            #Para el resto de niveles
            else:
                while len(opsJer[nivel])>1: #>1 porque en la posicion 0 esta el nivel
                    operacion=opsJer[nivel].pop(1) # Obtengo la operacion
                    resultado=self.calculadora.calcularOperacion(operacion) #Calculo la operacion
                    opsJer=self.sustituirResultados(opsJer,resultado,nivel-1) #Sustituyo en el nivel superior
            
            print("CALCULANDO...")
            for filaOp in opsJer:
                print(filaOp)
        
        return resultado

    '''
    sustituirResultados()
    Sustituye los resultados de un nivel, en las casilla S del nivel superior
    @param opsJer:matriz que contiene la jerarquia de operaciones
    @param resultado: resultado que sustituye a S
    @param nivel: nivel superior al nivel de donde se calculó el resultado
    @return opsJer: matriz que contiene la jerarquia de operaciones modificada
    '''
    def sustituirResultados(self,opsJer,resultado,nivel):
        posABorrar=0
        for posicion in range(1,len(opsJer[nivel])):
            if opsJer[nivel][posicion]=='S':
                opsJer[nivel][posicion-1]+=str(resultado) #Concatenamos el resultado a la poscion anterior
                posABorrar=posicion
                break

        opsJer[nivel].pop(posABorrar) #Eliminamos la S tras haber sustituido el resultado
        return opsJer
    
    '''
    concatenarOps
    Concatena las operaciones en el nivel 0 (el último), para formar una operacion simple, sin paréntesis.
    @param opsJer:matriz que contiene la jerarquia de operaciones
    @return opsJer: matriz que contiene la jerarquia de operaciones modificada
    '''
    def concatenarOps(self,opsJer):
        CuentaConcatenada=""
        for posicionOp in range(1,len(opsJer[0])):
            CuentaConcatenada+=opsJer[0][posicionOp]
        
        vConcatenado=[0,CuentaConcatenada]
        opsJer[0]=vConcatenado
        return opsJer