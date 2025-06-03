# Dil

Ein einfacher Editor, der das Arbeiten mit `.vdad`-Dateien ermoeglicht. Die Anwendung basiert auf `tkinter` und kann zu einer Windows-Executable kompiliert werden.

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
   python vdad_editor.py
   ```
3. Erstellen einer Windows-Executable:
   ```bash
   pyinstaller --onefile vdad_editor.py
   ```
   Die fertige `.exe` befindet sich anschliessend im Ordner `dist`.

Der Editor unterstuetzt grundlegende Funktionen wie Neue Datei, Oeffnen, Speichern und Speichern unter.
