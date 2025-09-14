import os
from pathlib import Path

opciones = ["1","2","3","documentos", "escritorio", "descargas"]
bandera = False  #Bandera para saber si se debe salir

while bandera == False:
    #Se pregunta la ubicación del archivo
    print("¿Dónde deseas crear la carpeta principal?")
    print("Opciones: " + "\n1. Documentos" + "\n2. Escritorio" + "\n3. Descargas" + "\n4. Salir")
    opcion = input("Escribe tu opción: ").strip().lower()  #Se eliminan espacios y se pasa a minúscula
    
    if opcion == "4" or opcion == "Salir":
        print("Saliendo del programa.")
        bandera = True

    #Bucle para validar opción
    while opcion not in opciones and bandera==False:
        print("Opción no válida.")
        opcion = input("Intente otra vez. Dé Enter si desea salir: ").strip().lower()
        if opcion == "":  #Si el usuario presiona Enter sin escribir nada, marcamos bandera
            print("Saliendo del programa.")
            bandera = True

    if not bandera:
        home = Path.home()  #Se obtiene la raíz del usuario

        #Se construye la ruta en base a lo que escogió el usuario
        try:
            if opcion == "documentos" or opcion == "1":
                base_path = home / "Documents"
            elif opcion == "escritorio" or opcion == "2":
                base_path = home / "Desktop"
            elif opcion == "descargas" or opcion == "3":
                base_path = home / "Downloads"
        except:
            print("Saliendo del programa.")
            bandera = True

    if not bandera:
        #Se pregunta el nombre de la carpeta principal
        print("\n")
        nombre_principal = input("Escribe el nombre de la carpeta principal: ").strip()

        if not nombre_principal:
            print("No escribiste nombre. Saliendo del programa.")
            bandera = True
        else:
            #Se quitan espacios extra y se reemplazan los espaciones internos por "_"
            nombre_principal = "_".join(nombre_principal.split())
            carpeta_principal = base_path / nombre_principal
            os.makedirs(carpeta_principal, exist_ok=True) #Se crean todas las carpetas no existentes, y si existen no da error gracias a la función "exist_ok=True"

    if not bandera:
        #Se pregunta nombre de las subcarpetas
        subcarpetas = input("Escribe los nombres de las subcarpetas separados por comas: ").strip()
        if subcarpetas:
            lista_subcarpetas = subcarpetas.split(",")
            for sub in lista_subcarpetas: #Se recorre cada elemento de la lista
                sub = sub.strip()
                if sub: #Se verifica que no esté vacío
                    sub = "_".join(sub.split()) 
                    ruta_sub = carpeta_principal / sub
                    os.makedirs(ruta_sub, exist_ok=True)

        print(f"\nCarpetas creadas en: {carpeta_principal}")
