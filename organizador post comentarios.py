import os
import shutil
from pathlib import Path

def limpiar_pantalla():
    # Limpia la pantalla de la consola.
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def obtener_ruta_base():
    # Pregunta y devuelve la ruta base para operar.
    while True:
        print("¿Dónde deseas realizar la acción?")
        print("\nOpciones de ubicación:")
        print("  [1] Documentos")
        print("  [2] Escritorio")
        print("  [3] Descargas")
        opcion = input("\nEscribe el número de tu opción: ").strip()

        home = Path.home()
        if opcion == "1":
            return home / "Documents"
        elif opcion == "2":
            return home / "Desktop"
        elif opcion == "3":
            return home / "Downloads"
        else:
            print("\n--- Opción no válida. Por favor, elige un número de la lista. ---")
            input("Presiona Enter para continuar...")
            limpiar_pantalla()

def crear_carpetas():
    # Crea una carpeta principal y las subcarpetas indicadas.
    limpiar_pantalla()
    print("--- Módulo: Crear Nuevas Carpetas ---\n")
    base_path = obtener_ruta_base()
    if not base_path:
        return

    print(f"\nUbicación seleccionada: {base_path}")
    nombre_principal = input("Escribe el nombre de la carpeta principal: ").strip()

    if not nombre_principal:
        print("\n--- No se escribió un nombre. Volviendo al menú principal. ---")
        return

    # Reemplaza espacios por guiones bajos.
    nombre_principal_saneado = "_".join(nombre_principal.split())
    carpeta_principal = base_path / nombre_principal_saneado

    try:
        os.makedirs(carpeta_principal, exist_ok=True)
        print(f"\n¡Éxito! Se creó la carpeta principal en: {carpeta_principal}")

        subcarpetas = input("\nEscribe los nombres de las subcarpetas separados por comas (o deja en blanco si no deseas): ").strip()
        if subcarpetas:
            lista_subcarpetas = subcarpetas.split(",")
            print("\nCreando subcarpetas...")
            for sub in lista_subcarpetas:
                sub_saneado = "_".join(sub.strip().split())
                if sub_saneado:
                    ruta_sub = carpeta_principal / sub_saneado
                    os.makedirs(ruta_sub, exist_ok=True)
                    print(f"  - Subcarpeta '{sub_saneado}' creada.")
            print("\n--- Resumen de creación ---")
            print(f"Carpeta principal: {carpeta_principal.name}")
            print(f"Subcarpetas creadas: {', '.join([s.strip() for s in lista_subcarpetas if s.strip()])}")
            print("--------------------------")
        else:
            print("\nNo se crearon subcarpetas.")

    except OSError as e:
        print(f"\n--- Error al crear carpetas: {e} ---")

def ver_carpetas():
    # Muestra las carpetas existentes en una ubicación.
    limpiar_pantalla()
    print("--- Módulo: Ver Carpetas Existentes ---\n")
    base_path = obtener_ruta_base()
    if not base_path:
        return

    print(f"\nMostrando carpetas en: {base_path}\n")
    try:
        # Lista solo los directorios, no archivos.
        carpetas = [item for item in os.listdir(base_path) if os.path.isdir(base_path / item)]
        if carpetas:
            for i, carpeta in enumerate(carpetas, 1):
                print(f"  {i}. {carpeta}")
        else:
            print("No se encontraron carpetas en esta ubicación.")
    except FileNotFoundError:
        print(f"--- El directorio no existe: {base_path} ---")


def eliminar_carpetas():
    # Elimina una carpeta y todo su contenido.
    limpiar_pantalla()
    print("--- Módulo: Eliminar Carpetas ---\n")
    ruta_str = input("Pega la ruta completa de la carpeta que deseas eliminar: ").strip()

    if not ruta_str:
        print("\nNo se ingresó una ruta.")
        return

    ruta_a_eliminar = Path(ruta_str)

    if ruta_a_eliminar.is_dir():
        print(f"\nSe encontró la carpeta: {ruta_a_eliminar}")
        confirmacion = input("¿Estás seguro de que deseas eliminarla y TODO su contenido? (s/n): ").lower()
        if confirmacion == 's':
            try:
                shutil.rmtree(ruta_a_eliminar)
                print(f"\n--- La carpeta '{ruta_a_eliminar.name}' ha sido eliminada exitosamente. ---")
            except OSError as e:
                print(f"\n--- Error al eliminar la carpeta: {e} ---")
        else:
            print("\nOperación cancelada.")
    else:
        print("\n--- La ruta ingresada no corresponde a una carpeta válida. ---")

def mover_archivos():
    # Mueve archivos de una carpeta de origen a una de destino.
    limpiar_pantalla()
    print("--- Módulo: Mover Archivos ---\n")
    origen_str = input("Pega la ruta de la carpeta de ORIGEN (de donde quieres mover los archivos): ").strip()
    destino_str = input("Pega la ruta de la carpeta de DESTINO (a donde quieres mover los archivos): ").strip()
    
    origen = Path(origen_str)
    destino = Path(destino_str)

    if not origen.is_dir() or not destino.is_dir():
        print("\n--- Una o ambas rutas no son carpetas válidas. Por favor, verifica. ---")
        return

    try:
        archivos = [f for f in os.listdir(origen) if os.path.isfile(origen / f)]
        if not archivos:
            print(f"\nLa carpeta de origen '{origen.name}' no contiene archivos.")
            return

        print(f"\nArchivos encontrados en '{origen.name}': {len(archivos)}")
        contador_movidos = 0
        for archivo in archivos:
            try:
                shutil.move(str(origen / archivo), str(destino / archivo))
                print(f"  - Moviendo '{archivo}' -> OK")
                contador_movidos += 1
            except Exception as e:
                print(f"  - Error al mover '{archivo}': {e}")
        
        print(f"\n--- Proceso completado. Se movieron {contador_movidos} archivos a '{destino.name}'. ---")

    except Exception as e:
        print(f"\n--- Ocurrió un error general: {e} ---")


def main():
    # Muestra el menú principal y gestiona el programa.
    limpiar_pantalla()
    print("¡Bienvenido al Organizador de Carpetas!")

    while True:
        print("\n--- Menú Principal ---")
        print("¿Qué te gustaría hacer?")
        print("  [1] Crear un nuevo set de carpetas")
        print("  [2] Ver carpetas existentes en una ubicación")
        print("  [3] Eliminar un set de carpetas")
        print("  [4] Mover archivos a una carpeta")
        print("  [5] Salir")

        opcion_menu = input("\nEscribe el número de tu opción: ").strip()

        if opcion_menu == "1":
            crear_carpetas()
        elif opcion_menu == "2":
            ver_carpetas()
        elif opcion_menu == "3":
            eliminar_carpetas()
        elif opcion_menu == "4":
            mover_archivos()
        elif opcion_menu == "5":
            print("\nPrograma finalizado correctamente. ¡Hasta luego!\n")
            break
        else:
            print("\n--- Opción no válida. Por favor, elige un número del menú. ---")
        
        input("\nPresiona Enter para volver al menú principal...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()
