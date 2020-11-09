# GdW KW 46

Beispiele für einfache Python-Konstrukte.
* tips.csv aus <https://www.kaggle.com/jsphyg/tipping>

Wir lesen den Datensatz tips.csv lediglich ein, um für Fingerübungen eine Quelle für ein paar Datenstrukturen zu haben.

## Bibliotheken und Daten laden

Falls in der folgenden Zelle Fehler auftreten, ggf. vorher im Terminal ausführen:
    
```sh
conda install pandas numpy matplotlib
conda install seaborn
```

für seaborn siehe auch <https://seaborn.pydata.org/installing.html>:

```sh
pip install seaborn
```


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series, DataFrame

Wir laden den Datensatz explizit aus der (hier von Kaggle bezogenen) csv-Datei:

df = pd.read_csv('tips.csv')
type(df)

(Der Tips-Datensatz wäre auch Teil von Seaborn:)

df = sns.load_dataset("tips")

## Explorative Datenanalyse (EDA)

df.head(3)

df.describe(include='all')

EDA und so weiter: in höheren Semestern, in Mathematik etc.: Siehe z.B. <https://www.kaggle.com/sanjanabasu/tips-dataset>


## Übung KW 45 GdW




Spaltennamen = df.columns.tolist()
Spaltennamen

Rechnung = df['total_bill'].tolist()
display(type(Rechnung))

print(Rechnung)

#### Aufgabe: Wie viele Rechnungen haben wir?

XXXXXX

#### Aufgabe: Die Rechnungswerte sortiert

RechnungSortiert = XXXXXXXXXX
print(RechnungSortiert)

#### Aufgabe: Drucke die kleinsten (resp. größten) 5 Beträge aus RechnungSortiert

print(XXXXXXX)
print(XXXXXXX)

### Basis-Statistiken

Berechne für die Liste `Rechnung`:

* Mittelwert (auch Erwartungswert, Schwerpunkt der Verteilung): Summe aller Rechnungen geteilt durch Anzahl
* Median: nicht der Mittelwert der Liste, sondern der Wert des mittleren Elements der sortierten Liste

* durchschnittliches Abweichungsquadrat (auch Stichprobenvarianz, empirische Varianz): Durchschnitt aller quadrierten Abweichungen vom Mittelwert, <https://de.wikipedia.org/wiki/Empirische_Varianz>
* Standardabweichung: Quadratwurzel der Varianz

#### Aufgabe: Mittelwert


Mittelwert = XXXXXXXXXXX
Mittelwert

#### Aufgabe: Median

Median = XXXXXXXXX
Median

#### Aufgabe: Varianz

SummeQuadrierteAbweichungen = 0
for XXXXXXXX :
    XXXXXX 
    
Varianz = XXXXXX
display(Varianz)

#### Aufgabe: Standardabweichung

Standardabweichung = XXXXXXX
display(Standardabweichung)

Vergleichen Sie ihre Ergebnisse mit der Ausgabe von `df.describe()` oben: Was fällt Ihnen auf?

#### Aufgabe: Funktion `Basisstatistiken`

Definiere eine Funktion `Basisstatistiken`, die den Mittelwert und die Standardabweichung einer Liste von Zahlen zurückgibt.


def Basisstatistiken(Zahlenliste):
    ...

## Umsätze nach Wochentagen

SpalteWochentage = df.day.tolist()
Wochentage = set(SpalteWochentage)
Wochentage

UmsaetzeWochentage = { day: {'Umsaetze': df.loc[df.day==day].total_bill.tolist() }
                        for day in Wochentage }
print(UmsaetzeWochentage)

`UmsaetzeWochentage` ist ein Dictionary, dessen Werte selbst wiederum aus einem Dictionary und Listen bestehen.

Gesucht: Ergänzung dieser Datenstruktur um `durchschnittlicherTagesumsatz` für jeden Tag.



for Tag in UmsaetzeWochentage:
    TagUmsaetze = UmsaetzeWochentage[Tag]['Umsaetze']
    UmsaetzeWochentage[Tag]['durchschnittlicherTagesumsatz'] = round(sum(TagUmsaetze) / len(TagUmsaetze), 2)

print(UmsaetzeWochentage['Fri'])

UmsaetzeWochentage['Fri']['durchschnittlicherTagesumsatz']

