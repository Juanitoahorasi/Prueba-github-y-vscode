
# Definimos las funciones (operaciones aritmeticas)
def sumar(a,b) :
    return a + b
def restar(a,b):
    return a - b
def multiplicar(a,b) :
    return a * b
def dividir(a,b):
    if b ==  0:
        
        raise ValueError("Syntax Error - no se puede dividir por cero.")
    return a/b
# Definimos el menu de la calculadora

"""menu"""
def calculadora():
    print ("--- Calculadora ---")
    try:
        a = float(input("Primer Numero"))  
        b = float(input("Segundo Numero"))
    except ValueError:
        print("Error: Debe ingresar un numero entero valido.")
        return
    print ("1) Sumar 2) Restar 3) Multiplicar 4) Dividir")
    opcion = input("Elija una opcion")
    try:
        if opcion == "1": resultado = sumar(a,b)
        elif opcion == "2": resultado = restar(a,b)
        elif opcion == "3": resultado = multiplicar(a,b)
        elif opcion == "4": resultado = dividir(a,b)
        else: 
            print("Opcion invalida.")
            return
        print("El resultado es: ", resultado )
    except ValueError as e:
        print(f"Eror: {e}")
    print("Reinicie para realizar otra operacion.")
# Definimos como se ejecuta el programa principal , llamando a la funcion calculadora.
        
if __name__ == "__main__":
    calculadora()
    
   
    