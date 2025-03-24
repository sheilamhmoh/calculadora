import sys

class Calculadora:
    def multiplicar(self, num1, num2):
        try:
            resultado = float(num1) * float(num2)
            return resultado
        except ValueError:
            return "Ingresa dos números válidos"  # Puedes devolver un mensaje claro si los datos no son válidos.

if __name__ == "__main__":
    if len(sys.argv) == 3:
        num1 = sys.argv[1]
        num2 = sys.argv[2]
        calc = Calculadora()
        resultado = calc.multiplicar(num1, num2)
        
        # Si el resultado es un número, lo mostramos, de lo contrario, mostramos el mensaje de error.
        if isinstance(resultado, float):
            print(f"Este es el resultado de la multiplicación: {resultado}")
        else:
            print(resultado)  # Imprime el mensaje de error si no es un número.
    else:
        print("Ingresa los dos números que deseas multiplicar.")
