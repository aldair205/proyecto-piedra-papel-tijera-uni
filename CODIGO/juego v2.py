import random
import json
import os

# este es elarchivo que servirá para guardar nuestras estadisticas (backend)
# este archivo se genera solo 
ARCHIVO_BD = "backend_historial.json"

def cargar_historial():
    """Carga el historial de partidas desde el archivo JSON (Backend)."""
    if not os.path.exists(ARCHIVO_BD):
        return {"victorias_usuario": 0, "victorias_maquina": 0, "empates": 0, "partidas_jugadas": 0}
    
    # esta linea evita que el programa se caiga en caso de tener mala suerte y el archivo se corrompa
    try:
        with open(ARCHIVO_BD, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, IOError):
        print("⚠️ Advertencia: Error al leer el progreso en el juego. Restableciendo datos.")
        return {"victorias_usuario": 0, "victorias_maquina": 0, "empates": 0, "partidas_jugadas": 0}

def guardar_historial(historial):
    """Guarda los datos actualizados en el archivo JSON (Persistencia de datos)."""
    try:
        with open(ARCHIVO_BD, "w", encoding="utf-8") as archivo:
            json.dump(historial, archivo, indent=4, ensure_ascii=False)
    except IOError:
        print("❌ Error: No se pudo guardar la información.")

def mostrar_estadisticas(historial):
    """Muestra el estado actual del registro de partidas."""
    print("\n=========================================")
    print("         HISTORIAL DE PARTIDAS  ")
    print("=========================================")
    print(f" Partidas Totales Jugadas : {historial['partidas_jugadas']}")
    print(f" Partidas Ganadas         : {historial['victorias_usuario']}")
    print(f" Partidas Perdidas        : {historial['victorias_maquina']}")
    print(f" Partidas Empatadas       : {historial['empates']}")
    print("=========================================\n")

def jugar():
    """Lógica principal del juego y interacción con el usuario."""
    opciones = ["piedra", "papel", "tijera"]
    historial = cargar_historial()
    
    print("¡Espero que te guste este juego de Piedra, Papel o Tijera!")
    mostrar_estadisticas(historial)
    print("Escribe 'salir' para cerrar el juego y guardar los datos.\n")
    
    # esta estructura es la encargada del bucle el este juego y que no se acabe 
    while True:
        entrada_usuario = input("cual es tu jugada? (piedra, papel, tijera): ").strip().lower()
        
        if entrada_usuario == "salir":
            print("\nGuardando tu historial...")
            guardar_historial(historial)
            mostrar_estadisticas(historial)
            print("¡Gracias por jugar! ADIOSSSS.")
            break
            
        # esto se encarga de verificar que no se escribio mal, lo que hayamos elegido y el el caso que si te avisa
        if entrada_usuario not in opciones:
            print("⚠️ ⚠️ escribiste mal, revisa y digita de nuevo tu eleccion.\n")
            continue
            
        # esto es lo que permite que el sistema eliga alasar
        eleccion_sistema = random.choice(opciones)
        print(f"El Sistema seleccionó: {eleccion_sistema}")
        
        # esto se encarga del procesamiento de resultados
        historial["partidas_jugadas"] += 1
        
        if entrada_usuario == eleccion_sistema:
            print(" Empate.\n")
            historial["empates"] += 1
        elif (entrada_usuario == "piedra" and eleccion_sistema == "tijera") or \
             (entrada_usuario == "papel" and eleccion_sistema == "piedra") or \
             (entrada_usuario == "tijera" and eleccion_sistema == "papel"):
            print("🏆 GANASTEEE!!\n")
            historial["victorias_usuario"] += 1
        else:
            print("TE GANO UNA MAQUINAAAA 😹.\n")
            historial["victorias_maquina"] += 1
            
        # esto hace que se guarde la jugada en cada turno para evitar posibles problemas
        guardar_historial(historial)

if __name__ == "__main__":
    jugar()