import hashlib

def es_primo(numero):
    """Verifica si un número es primo."""
    
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True


def validar_entero_positivo(valor):
    """Valida que el valor ingresado sea un entero positivo."""
    
    try:
        numero = int(valor)

        if numero <= 0:
            return None

        return numero

    except ValueError:
        return None

def diffie_hellman():

    print("\n=== DIFFIE-HELLMAN ===")

    p = validar_entero_positivo(
        input("Ingrese número primo p: ")
    )

    g = validar_entero_positivo(
        input("Ingrese generador g: ")
    )

    a = validar_entero_positivo(
        input("Ingrese clave privada de A: ")
    )

    b = validar_entero_positivo(
        input("Ingrese clave privada de B: ")
    )

    if not all([p, g, a, b]):
        print("Error: Todos los datos deben ser enteros positivos.")
        return

    if not es_primo(p):
        print("Error: p debe ser un número primo.")
        return

    # Claves públicas
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Clave compartida
    clave_A = pow(B, a, p)
    clave_B = pow(A, b, p)

    print("\n=== RESULTADOS ===")
    print(f"Clave pública de A: {A}")
    print(f"Clave pública de B: {B}")
    print(f"Clave compartida calculada por A: {clave_A}")
    print(f"Clave compartida calculada por B: {clave_B}")

def hash_sha256():

    print("\n=== HASH SHA-256 ===")

    texto = input("Ingrese texto: ").strip()

    if texto == "":
        print("Error: El texto no puede estar vacío.")
        return

    resultado = hashlib.sha256(
        texto.encode()
    ).hexdigest()

    print("\n=== RESULTADO ===")
    print(f"Hash SHA-256:\n{resultado}")

def menu():

    while True:

        print("\n==============================")
        print(" PROGRAMA DE CRIPTOGRAFÍA ")
        print("==============================")
        print("1. Diffie-Hellman")
        print("2. Hash SHA-256")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            diffie_hellman()
        elif opcion == "2":
            hash_sha256()
        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()