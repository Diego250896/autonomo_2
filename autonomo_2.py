# 1. Configuración inicial
palabra_secreta = input("Ingrese una palabra secreta: ").lower()
intentos_maximos = 5
contador_errores = 0

# Lista para guardar las letras que el jugador va adiviniando
letras_adivinadas = []

print(f"\n¡El juego comienza! Tienes {intentos_maximos} oportunidades para fallar.")

# 2. Bucle principal (Mientras no se pasen los errores y falten letras por adivinar)
while contador_errores < intentos_maximos:
    print("\n" + "="*30)
    
    # BUCLE FOR: Para mostrar el progreso de la palabra (_ _ _ o letras)
    palabra_completa = True
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            palabra_completa = False  # Si falta aunque sea una letra, no ha ganado aún
            
    print("\n") # Salto de línea para dar espacio

    # CONDICIONAL: Si ya no quedan letras ocultas, ¡Ganó!
    if palabra_completa:
        print(" ¡GANADOR! Has adivinado la palabra secreta.")
        break

    # 3. Solicitar una letra al jugador
    letra_ingresada = input("Adivine una letra: ").lower()

    # Validar que ingrese solo un carácter válido
    if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue

    # 4. CONDICIONALES IF-ELSE: Verificar si la letra es correcta o no
    if letra_ingresada in letras_adivinadas:
        print("Ya habías ingresado esa letra, intenta con otra.")
        
    elif letra_ingresada in palabra_secreta:
        print(f"¡Bien hecho! La letra '{letra_ingresada}' es correcta.")
        letras_adivinadas.append(letra_ingresada)
        
    else:
        contador_errores += 1
        print(f" Error número: {contador_errores}")
        print(f"Te quedan {intentos_maximos - contador_errores} oportunidades.")
        letras_adivinadas.append(letra_ingresada)

# 5. Fin del juego (Si sale del bucle por agotar los errores)
if contador_errores == intentos_maximos:
    print("\n Fin del juego. ¡Te has quedado sin oportunidades!")
    print(f"La palabra secreta era: {palabra_secreta}")


    