def menu():
    print("\n==== Simulación de intercambio de claves Diffie-Hellman ====")
    print("1.Calcular clave pública")
    print("2.Calcular clave compartida")
    print("3.Salir")

def validar_entero(mensaje):
    #Función para validar que la entrada sea un número entero positivo
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Entrada no válida: el número no puede ser negativo. Intente nuevamente.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
        
def validar_primo(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True

def calcular_clave_publica(g, a, p):
    return pow(g, a, p)

def calcular_clave_compartida(B, a, p):
    return pow(B, a, p)

def solicitar_primo():
    p = validar_entero("Ingrese el número primo (p): ")
    while not validar_primo(p):
        print("El número ingresado no es primo. Intente nuevamente.")
        p = validar_entero("Ingrese el número primo (p): ")
    return p

def solicitar_base(p):
    g = validar_entero("Ingrese la base (g): ")
    while g <= 1 or g >= p:
        print(f"La base (g) debe ser un número entero mayor que 1 y menor que p={p}. Intente nuevamente.")
        g = validar_entero("Ingrese la base (g): ")
    return g

def solicitar_clave_privada(p):
    a = validar_entero("Ingrese su clave privada (a): ")
    while a <= 1 or a >= p-1:
        print(f"La clave privada (a) debe ser un número entero mayor que 1 y menor que p-1={p-1}. Intente nuevamente.")
        a = validar_entero("Ingrese su clave privada (a): ")
    return a

def solicitar_clave_publica(p):
    B = validar_entero("Ingrese la clave pública del otro usuario (B): ")
    while B <= 1 or B >= p:
        print(f"La clave pública (B) debe ser un número entero mayor que 1 y menor que p={p}. Intente nuevamente.")
        B = validar_entero("Ingrese la clave pública del otro usuario (B): ")
    return B

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            p = solicitar_primo()
            g = solicitar_base(p)
            a = solicitar_clave_privada(p)
            A = calcular_clave_publica(g, a, p)
            print(f"\ncalculando A = ({g}^{a}) mod {p}")
            print(f"\n==== Su clave pública es: {A} ====")    

        elif opcion == '2':
            p = solicitar_primo()
            B = solicitar_clave_publica(p)
            a = solicitar_clave_privada(p)
            clave_compartida_K = calcular_clave_compartida(B, a, p)
            print(f"\ncalculando K = ({B}^{a}) mod {p}")
            print(f"\n==== Su clave compartida es: {clave_compartida_K} ====")

        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":    
    main()