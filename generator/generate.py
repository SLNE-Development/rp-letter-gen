from file_utils import generate_color_yml
from process_images import process_images
from update_font_yml import update_font_yml

def main():
    color_name = input("Gib den Farbnamen ein (z.B. 'blue'): ").strip()
    text_color = input("Gib die Textfarbe als Hex-Wert ein (z.B. '#FFFFFF'): ").strip()
    background_color = input("Gib die Hintergrundfarbe als Hex-Wert ein (z.B. '#000000'): ").strip()

    print(f"\nGeneriere Dateien für Farbe: {color_name}\n")

    generate_color_yml(color_name)
    process_images(color_name, text_color, background_color)
    update_font_yml()

    print("\nGenerierung abgeschlossen!")

if __name__ == "__main__":
    main()