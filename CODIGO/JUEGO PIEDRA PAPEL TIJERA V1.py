import random

def iniciar_juego():
    """
    Función principal que ejecuta el avance del sistema.
    Implementa bucles para la continuidad y condicionales para la lógica.
    """
    opciones = ["piedra", "papel", "tijera"]
    
    # Variables de estado 
    victorias_usuario = 0
    victorias_maquina = 0
    
    print("--- HOLA, ESTO ES UNA PRUEBA ---")
    print("JUEGO: Piedra, Papel o Tijera, proximamente entre pokemones")
    print("Escribe 'salir' para finalizar la ejecución y ver tus puntos.\n")
    
    # bucle
    # Mantiene el ciclo de ejecución activo hasta que el jugador decida salir.
    while True:
        entrada_usuario = input("selecciona entre: (piedra, papel, tijera): ").lower()
        
        # final de la partida
        if entrada_usuario == 'salir':
            print("\n       --- RESULTADOS FINALES ---")
            print( )
            print(f"Tu puntuación: {victorias_usuario} | Puntuación del Sistema: {victorias_maquina}")
            print( )
            print("es toda we, cerrando esta prueba...")
            print( )
            break
            
        # Integre la validación de perspectivas por si el usuario escribe mal o falta una letra, esto solo en pruebas planeo quitarlo en un futuroo
        if entrada_usuario not in opciones:
            print("⚠️ escribiste mal, revisa y digita de nuevo tu eleccion.\n")
            continue
            
        # Lógica del sistema
        # aqui en la parte de "el sistema seleccion" queria poner "gengar escogio" pero no tendria sentido sin las imagenes asi que base
        # todo en el juego clasico, al final creo que si implementare eso pero por ahora esto es una simple propuesta 
        eleccion_sistema = random.choice(opciones)
        print(f"El Sistema seleccionó: {eleccion_sistema}")
        
        # ESTRUCTURAS LÓGICAS
    
        if entrada_usuario == eleccion_sistema:
            print("Resultado: EMPATE .\n")
        elif (entrada_usuario == "piedra" and eleccion_sistema == "tijera") or \
             (entrada_usuario == "papel" and eleccion_sistema == "piedra") or \
             (entrada_usuario == "tijera" and eleccion_sistema == "papel"):
            print("Resultado: ¡GANASTEEE!\n")
            victorias_usuario += 1
        else:
            print("Resultado: TE GANO UNA MAQUINAAAA 😹.\n")
            victorias_maquina += 1

# con esto se inicia el scrip
if __name__ == "__main__":
    iniciar_juego()
