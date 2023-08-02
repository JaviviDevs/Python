from Calculadora import Calculadora

# Definición de la función "main"
def main():
    # Lógica principal de tu programa
    operacion=input("Por favor introduzca la operación a calcular: ")
    calculadora=Calculadora(operacion)
    calculadora.calcular()

# Verificación para asegurarnos de que estamos ejecutando este archivo directamente
if __name__ == "__main__":
    main()