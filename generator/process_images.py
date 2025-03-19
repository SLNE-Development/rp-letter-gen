import os
from PIL import Image
from file_utils import read_directory

def hex_to_rgba(hex_color):
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 6:  # Falls kein Alpha-Wert angegeben ist, setze ihn auf 255
        hex_color += "FF"
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4, 6))

def process_images(color_name, text_color_hex, background_color_hex):
    files = read_directory("raw")
    png_files = [f for f in files if f.endswith(".png")]

    if not png_files:
        print("Keine .png-Dateien im 'raw'-Ordner gefunden!")
        return

    output_dir = os.path.join("colors", color_name)
    os.makedirs(output_dir, exist_ok=True)

    text_color = hex_to_rgba(text_color_hex)
    background_color = hex_to_rgba(background_color_hex)

    for file_name in png_files:
        input_path = os.path.join("raw", file_name)
        output_path = os.path.join(output_dir, file_name)

        image = Image.open(input_path).convert("RGBA")
        pixels = image.load()

        for x in range(image.width):
            for y in range(image.height):
                r, g, b, a = pixels[x, y]
                if (r, g, b) == (255, 255, 255):  # Weiß ersetzen
                    pixels[x, y] = text_color
                elif (r, g, b) == (0, 0, 0):  # Schwarz ersetzen
                    pixels[x, y] = background_color

        image.save(output_path)
        print(f"Gespeichert: {output_path}")