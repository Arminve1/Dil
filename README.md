# Dil


## Anforderungen
* Python 3
* Optionale Abhaengigkeit: [PyInstaller](https://pyinstaller.org/) zum Erstellen einer `.exe`

## Verwendung
1. Installation der Abhaengigkeiten (nur falls Sie ein `.exe` erstellen moechten):
   ```bash
   pip install pyinstaller
   ```
2. Starten des Editors als Python-Programm:
   ```bash
   python dil_editor.py
   ```
3. Erstellen einer Windows-Executable:
   ```bash
   pyinstaller --onefile dil_editor.py
   ```
   Die fertige `.exe` befindet sich anschliessend im Ordner `dist`.

Der Editor unterstuetzt nun zusaetzliche Funktionen wie Suchen, einstellbare Schriftgroesse und Tastenkombinationen.
