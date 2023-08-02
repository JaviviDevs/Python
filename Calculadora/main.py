from Calculadora import Calculadora

'''
Main()
Pide la entrada de datos (la operacion) al usuario y calcula la operacion
mediante la creación del objeto calculadora.
'''
def main():
    # Lógica principal de tu programa
    operacion=input("Por favor introduzca la operación a calcular: ")
    calculadora=Calculadora(operacion)
    calculadora.calcular()

# Main
if __name__ == "__main__":
    main()