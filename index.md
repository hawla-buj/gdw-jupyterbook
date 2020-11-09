GdW 2020, Einführung Jupyterbook
====================




Achtung, nicht verwechseln:
* *Jupyter Notebook* (bekannt aus Programmieren 1) ist eine Umgebung, um in Python zu programmieren. Speicherformat ist u.A. *ipynb*
* *Jupyterbook* ist ein Tool, um Markdown- und ipynb-Dateien im Netz und als pdf zu publizieren.

schon passiert / Vorbereitung:

* <http://jbusse.de/dsci-lab/dsci-lab-use.html>

## Lernziele

Aufgabe: aus dem Netz Dateien herunteladen, und 

* diese in ein eigenes Arbeits-Verzeichnis zu kopieren, 
* diese mit einem einfachen Editor - z.B. *miniconda* - zu bearbeiten,
* diese mit Jupyterbook in eine html-Website und ein pdf zu übersetzen.

Dazu wichtig sind Linux-Befehle wie z.B.

* `cd`, `cd ~`, `cd ..`
* `ls`, `ls -als`
* `cp`, `cp -r`
* `mkdir`
* `rm`, `rmdir`, `rm -rf`

Insgesamt sollte Sicherheit in der Navigation und der Behandlung von Dateien aus dem Terminal heraus entstehen.


## KW43

heute (KW 43): Download eines Jupyterbooks aus GitHub zur eigenen Bearbeitung

Konvention: Im Verzeichnis `~/dsci` liegen im dsci-lab die Dateien, die JB online zur Verfügung stellt.

```sh
cd ~/dsci
ls
```

Erstmaliger Download eines Git-Projektes: Klonen! (Das Projekt ist public, wir benötigen also kein Passwort.)

```sh
cd ~/dsci
git clone https://github.com/hawla-buj/gdw-jupyterbook
```

Es wird das Verzeichnis `gdw-jupyterbook` angelegt und mit dem Inhalt aus GitHub gefüllt - inclusive Herkunftsinformationen.

Um das Projekt ggf. einmal zu aktualisieren, wechselt man in das Verzeichnis hinein, und setzt ein `pull` ab:

```sh
cd ~/dsci/gdw-jupyterbook/
git pull
```
Aufgabe: Bearbeiten Sie diese Dateien - und zwar in einer eigenen Kopie. Eigenen Arbeitsbereich anlegen z.B. so:

```sh
cd
mkdir mein-dsci
```

Eine Kopie des eben heruntergeladenen GitHub-Projektes anlegen:

```sh
cd
cp -r dsci/gdw-jupyterbook mein-dsci
```

Und die Datei `kessel-vogt.md` bearbeiten:

```sh
cd ~/mein-dsci/gdw-jupyterbook
mousepad kessel-vogt.md &
```

Die von Ihnen bearbeitete Datei in eine Website übersetzen:

```sh
cd ~/mein-dsci/gdw-jupyterbook
jb build .
```

```{note}
Ggf. wird ein Fehler angezeigt:

* `Exception occurred ... fileExistsError [Errno 17]: File exists: ...`

Lösung: Lösche das Verzeichnis `_build`, z.B. so:

```sh
rm -rf _build
```

Um die Website anzuschauen: rechte Maustaste auf den im Terminal angezeigten Link!


## KW44

Ziel der Sitzung: Erstellen von Inhalt mit Markdown und Jupyterbook
* zuerst eher spielerisch
* aber auch ernsthaft

### interesse.md

Ort: Ihr Verzeichnis `~/mein-dsci/gdw-jupyterbook`:

```
cd ~/mein-dsci/gdw-jupyterbook
```

**(1) Datei und Inhalt erstellen**
Legen Sie bitte die Datei `interesse.md` an und editieren diese, z.B. so:

```sh
touch interesse.md
mousepad interesse.md &
```

Inhalt der Datei `interesse.md`:

* Erste Zeile: Überschrift 1 mit Ihrem Interesse
* alle weiteren Zeilen: Beschreibung eines privaten Interesses in ca 100 Wörtern

WICHTIG: Wir werden diese Datei kurs-öffentlich zur Verfügung stellen. Bitte schreiben Sie nur Dinge, die notfalls auch öffentlich sichtbar werden dürfen, und die keinesfalls einen Rückschluss auf Ihre Person erlauben. Achten Sie unbedingt auf Ihre Anonymität; nennen Sie insbesonde nicht Ihren Namen oder andere persönliche Daten im Text.


**(2) Publizieren**
Fügen Sie die neu erstellte Datei in das Inhaltsverzeichnis ein. Editieren Sie dazu die Datei `_toc.yml`:

```sh
mousepad _toc.yml &
```

Fügen Sie als letzte Zeile die Information `- file: interesse` hinzu. Achten Sie auf die richtige Einrückung! Auch beachten: wir benötigen hier *nicht* die Endung `.md`.

Erstellen Sie die html-Dateien:
```sh
jb build .
```

**(3) GdW-Ergebnissicherung**

* Laden Sie die Datei `interesse.md` auf Moodle hoch: [Markdown-Datei interesse.md](https://moodle.haw-landshut.de/mod/assign/view.php?id=223408)


### abstract.md

Wie oben, aber jetzt GdW-bezogen:
* Legen Sie bitte die Datei `abstract.md` an und editieren diese.
* Inhalt: Zusammenfassung der wichtigsten Inhalte eines beliebigen Unterkapitels (freie Auswahl aus 1.1 - 1.3, 2.1 - 2.3., 3.1 - 3.5) aus Kessel/Vogt.
* Umfang etwas mehr: 200 Wörter


