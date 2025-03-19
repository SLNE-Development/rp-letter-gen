# Farbkonfiguration und Bildverarbeitung für Buchstaben

Dieses Projekt generiert YAML-Konfigurationen und bearbeitet Bilder für verschiedene Farben.

## 📌 Funktionen

✅ **Generierung von YAML-Dateien** mit Farbnamen
✅ **Ersetzen von Farben in PNG-Dateien** basierend auf Hex-Werten
✅ **Automatische Aktualisierung von `font.yml`** mit allen verfügbaren Bitmaps

## 🔧 Installation

1. **Python 3 installieren** (falls nicht vorhanden)
2. **Projekt klonen oder herunterladen:**

```bash
git clone git@github.com:SLNE-Development/rp-letter-gen.git
cd rp-letter-gen
```

3. **Abhängigkeiten installieren:**

```bash
pip install -r requirements.txt
```

## 🚀 Nutzung

### YAML & Bilder mit interaktiven Eingaben generieren

Starte `generate.py` und gib deine Werte ein:

```bash
python generate.py
```

👉 **Beispiel-Eingabe:**

```plaintext
Gib den Farbnamen ein (z.B. 'blue'): red
Gib die Textfarbe als Hex-Wert ein (z.B. '#FFFFFF'): #FF0000
Gib die Hintergrundfarbe als Hex-Wert ein (z.B. '#000000'): #000000
```
