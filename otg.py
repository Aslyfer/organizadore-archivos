import os
import shutil

def organizar_archivos(carpeta_descargas):
    # Lista de extensiones y los nombres de las carpetas correspondientes
    extensiones = {
        'documentos': ['.pdf', '.doc', '.docx', '.txt'],
        'imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
        'videos': ['.mp4', '.mkv', '.avi'],
        'musica': ['.mp3', '.wav', '.flac'],
        'archivos_comprimidos': ['.zip', '.rar', '.7z'],
        'otros': []
    }

    # Recorre cada archivo en la carpeta de descargas
    for archivo in os.listdir(carpeta_descargas):
        archivo_path = os.path.join(carpeta_descargas, archivo)

        # Ignora directorios y archivos ocultos
        if os.path.isfile(archivo_path) and not archivo.startswith('.') and not ('.py'):
            # Obtiene la extensión del archivo
            _, extension = os.path.splitext(archivo)

            # Encuentra la carpeta correspondiente según la extensión
            carpeta_destino = 'otros'  # Carpeta por defecto si no coincide con ninguna extensión conocida
            for categoria, extensiones_permitidas in extensiones.items():
                if extension.lower() in extensiones_permitidas:
                    carpeta_destino = categoria
                    break

            # Crea la carpeta de destino si no existe
            carpeta_destino_path = os.path.join(carpeta_descargas, carpeta_destino)
            if not os.path.exists(carpeta_destino_path):
                os.makedirs(carpeta_destino_path)

            # Mueve el archivo a la carpeta de destino
            shutil.move(archivo_path, os.path.join(carpeta_destino_path, archivo))

if __name__ == "__main__":
    carpeta_descargas = "."  # Reemplaza con la ruta de tu carpeta de descargas
    organizar_archivos(carpeta_descargas)
    print("Archivos organizados exitosamente.")
