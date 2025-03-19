import os
import yaml

def update_font_yml():
    font_yml_path = "colors/font.yml"

    if not os.path.exists(font_yml_path):
        print("Fehler: 'colors/font.yml' existiert nicht!")
        return

    with open(font_yml_path, "r", encoding="utf-8") as file:
        font_data = yaml.safe_load(file)

    if "bitmaps" not in font_data:
        font_data["bitmaps"] = {}

    color_folders = [d for d in os.listdir("colors") if os.path.isdir(os.path.join("colors", d)) and d != "font.yml"]

    for color in color_folders:
        bitmap_key = f"letter_{color}_bitmap"
        font_data["bitmaps"][bitmap_key] = {
            "texture": f"surf/letters/{color}/bitmap",
            "rows": 8,
            "columns": 6,
            "ascent": 7,
            "height": 7
        }

    with open(font_yml_path, "w", encoding="utf-8") as file:
        yaml.dump(font_data, file, default_flow_style=False, allow_unicode=True)

    print(f"'colors/font.yml' wurde aktualisiert!")