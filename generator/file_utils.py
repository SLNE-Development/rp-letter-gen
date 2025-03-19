import os
import re

def read_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def generate_color_yml(color_name):
    files = read_directory("raw")
    raw_config_yml_file = next((f for f in files if f.endswith(".yml")), None)
    if not raw_config_yml_file:
        print("Keine .yml-Datei im 'raw'-Ordner gefunden!")
        return

    raw_file_path = os.path.join("raw", raw_config_yml_file)

    with open(raw_file_path, "r", encoding="utf-8") as file:
        yaml_content = file.read()

    updated_content = re.sub(r'\braw\b', color_name, yaml_content)
    updated_content = re.sub(r'letter_raw_', f'letter_{color_name}_', updated_content)

    output_dir = os.path.join("colors", color_name)
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = os.path.join(output_dir, f"letters_{color_name}.yml")

    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Neue YAML-Datei gespeichert unter: {output_file_path}")