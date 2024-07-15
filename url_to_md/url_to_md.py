import requests
from markdownify import markdownify as md
from urllib.parse import urlparse
import os
from datetime import datetime

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def url_to_markdown(url, filename=None):
    if not is_valid_url(url):
        print("URL no válida. Por favor, introduce una URL correcta.")
        return

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción para códigos de error
        markdown = md(response.text, heading_style="ATX")
        
        if not filename:
            filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
        else:
            filename = f"{filename}.md"
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(markdown)
        
        print(f"Contenido descargado y convertido a Markdown exitosamente. Guardado como {filename}.")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el contenido: {e}")

def main():
    url = input("Por favor, introduce la URL: ")
    nombre_archivo_usuario = input("Introduce un nombre para el archivo (deja en blanco para usar el nombre por defecto): ").strip()
    url_to_markdown(url, nombre_archivo_usuario if nombre_archivo_usuario else None)

if __name__ == "__main__":
    main()