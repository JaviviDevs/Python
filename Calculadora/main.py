from CalculadoraCientifica import CalculadoraCientifica

'''
Main()
Pide la entrada de datos (la operacion) al usuario y calcula la operacion
mediante la creación del objeto calculadora.
'''
def main():
    # Lógica principal de tu programa

    #ejemplos a probar: 
    # 5+3
    # 10*5/2
    # 2*(3+4)-8/2
    # 1+(2*2+(3*3))-(8+5)-1
    # 1+(2*2+(2*2))+2+(3*3)
    # (10+10)-(20-5)*4/10
    
    # (10+-10)*5
    # (10+10)*5+(10+3
    operacion=input("Por favor introduzca la operación a calcular: ")
    calculadora=CalculadoraCientifica(operacion)
    calculadora.calcular()

# Main
if __name__ == "__main__":
    main()