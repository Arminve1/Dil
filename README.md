# Dil

Ein einfacher Editor fuer `.vdad`-Dateien. Dil bietet Funktionen wie Suchen, anpassbare Schriftgroesse, mehrere Tabs und sogar ein kleines Ratespiel. Die Anwendung basiert auf `tkinter` und kann zu einer Windows-Executable kompiliert werden.

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

### Neue Funktionen
- Bilder koennen ueber das Menue **Insert > Image** in das Dokument eingefuegt und angezeigt werden (Unterstuetzung fuer PNG und GIF).
- Unter **Help > Credits** erscheint ein Fenster mit dem Hinweis "Arming-Studios.com".
- Ein dunkler Modus kann unter **View > Dark Mode** aktiviert werden.
- Unter **Help > Surprise** oder per **Ctrl+Shift+H** wird eine geheime Nachricht angezeigt.
- Mehrere Dokumente koennen gleichzeitig in Tabs bearbeitet werden.
- Unter **Edit > Word Count** laesst sich die Wortanzahl des aktuellen Dokuments ermitteln.
- Im Menue **Game > Guess Number** wartet ein kleines Zahlratespiel.
