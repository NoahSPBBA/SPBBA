-------------------------------------------------------
## Zeitreihenanalyse: BMW Aktie vs. Google-Trends "BMW"
-------------------------------------------------------

### Projektziel:
Ziel dieses Projekts ist es, eine bivariate Zeitreihenanalyse durchzuführen, um zu untersuchen, ob ein Zusammenhang zwischen dem Google-Suchinteresse an "BMW" und der Kursentwicklung der BMW-Aktie besteht. Neben einer explorativen Analyse werden auch Prognosemodelle getestet.

---------------------------------------------------------------------------------
### Projektstruktur:
- data.exploration.py // Datenimport, Bereinigung, Indexbildung, Visualisierung
- descriptive_stats.py // Lagekennzahlen, Streuungsmaße, Wachstum, Korrelationen
- time_series_modeling.py // ARIMA & SARIMAX-Modelle inkl. Prognose
- daten_vereint.csv // Bereinigte, synchronisierte Zeitreihen (Google & BMW)
- README.md # Projektdokumentation
---------------------------------------------------------------------------------


---------------------------------------------------------------------------------
### Analyseüberblick
#### Datenquellen: 
- **BMW Aktie**: Historische Kursdaten (Yahoo Finance)
- **Google Trends**: Suchinteresse für den Begriff „BMW“ (Wöchentlich)

#### Datenaufbereitung
- Vereinheitlichung auf wöchentliche Frequenz
- Indexbildung mit Basiswert = 100
- Inner Join auf gemeinsame Datumswerte

#### Statistische Auswertung
- Lage- und Streuungsmaße (Mittelwert, Median, Varianz, etc.)
- Korrelations- und Kreuzkorrelationsanalyse (Lag-Analyse)
- Prüfung auf Stationarität (ADF-Test)

#### Modellierung
- **ARIMA**-Modell zur univariaten Prognose des BMW-Kurses
- **SARIMAX**-Modell mit Google Trends als exogene Variable
---------------------------------------------------------------------------------

### Ergebnisse: Hier erklären wir den Code und die Ergebnisse

data.exploration.py:
- Einlesen & Bereinigen der Daten
BMW-Aktie (bmw_aktie.csv)
Nur Spalten Date und Close werden verwendet.
Es wird ein Indexwert (Close_Index) berechnet: Close_Index = Close / Close[erste Zeile] * 100
-> Dadurch wird der Aktienkurs auf eine Basis von 100 normiert – das macht die Entwicklung vergleichbar.

- Google Trends (googletrends_bmw.csv)
Datei wird zeilenweise eingelesen, da das Google-Exportformat unregelmäßig ist.
Es wird die Spalte "Interest" bereinigt (Numerisch + Datumsformat).
Umbenannt zu "Date" -> damit Join mit der Aktie möglich ist.
Auch hier wird ein Index berechnet: Interest_Index = Interest / Interest[erste Zeile] * 100

- Zusammenführen (Join)
Beide Datenreihen werden über das Datum (Date) mit inner join verbunden.

Visualisierung
![Grafik: vis_1](Bilder_git/vis_1.png)
Bilder_git/vis_1.png
Interpretation:
BMW Aktie (blau): Schwankt stark – hohe Volatilität, vor allem 2023–2024
Google Trends (orange): Viel konstanter, leicht steigender Trend, keine heftigen Ausschläge
Beide Reihen starten bei Indexwert 100 (links am Anfang der Zeitachse)

Was fällt auf?
Die BMW-Aktie steigt über den Zeitraum stark an (auf über 300 Punkte indexiert), während Google Trends maximal leicht mitzieht
Kein klarer Gleichlauf → auf den ersten Blick nur schwache Korrelation
----------------------------------------------------------------------------------------------------------------------------------
descriptive_stats.py:
- Hier haben wir statistische Kennzahlen ausgerechnet:
  --- LAGEKENNZAHLEN ---

Mittelwerte:
BMW Aktie (Close): 74.02
BMW Index: 217.57
Google Trends: 84.93
Google Index: 107.51

Median:
BMW Aktie (Close): 73.11
BMW Index: 214.88
Google Trends: 85.0
Google Index: 107.59

Minimum:
BMW Aktie (Close): 34.02
Google Trends: 69

Maximum:
BMW Aktie (Close): 105.96
Google Trends: 100

-> Interpretation:
BMW hat hohe Streuung (34 – 106 €), Google Trends ist viel stabiler.
Der Mittelwert ≈ Median → symmetrische Verteilung.

--- STREUUNGSMASSE ---

Standardabweichung:
BMW Close: 15.98
BMW Index: 46.97
Google Trends: 5.84
Google Index: 7.4

Varianz:
BMW Close: 255.33
BMW Index: 2205.79 -> hoch volatil
Google Trends: 34.16
Google Index: 54.74 -> geringe Schwankung

Range (Spannweite):
BMW Close: 71.94
Google Trends: 31

-> Interpretation:
BMW-Kurs ist deutlich volatiler als das Suchinteresse.

--- WACHSTUMSRATEN ---

Absolute Wachstumsrate:
BMW Aktie: 45.66 EUR (von 34.02 auf 79.68)

Relative Wachstumsrate:
BMW Aktie: 134.2 %

Indexbildung (erste Woche = 100):
Letzter Indexwert: 234.2

Google Trends:
  Absolute Wachstumsrate: 17
  Relative Wachstumsrate: 21.52 %

Indexbildung (letzter Wert):
  BMW Index: 234.2
  Google Index: 121.52

-> Die BMW-Aktie ist deutlich stärker gewachsen als das Suchinteresse.

--- ZUSAMMENHANGSMAßE ---

Korrelation (BMW Index vs. Google Index): 0.123

--- ZUSAMMENHANGSMAßE ---

Korrelation (BMW Index vs. Google Index): 0.123

Kreuzkorrelation mit Lag (Google voraus):
Lag 0 Wochen: 0.123
Lag 1 Wochen: 0.104
Lag 2 Wochen: 0.084
Lag 3 Wochen: 0.067
Lag 4 Wochen: 0.064
Lag 5 Wochen: 0.061

-> Interpretation:
Es gibt keine starke lineare Beziehung zwischen Google-Trends und BMW-Aktie.
Google-Trends erklären keine Kursveränderung zeitlich voraus.

Visualisierung:
![Grafik:boxplot_verteilungAktienInterest](Bilder_git/boxplot_verteilungAktieInterest.png)
- Was zeigt der Boxplot?
BMW Close (Aktienkurs): Hat eine größere Streuung und Ausreißer nach unten (unterhalb der unteren "Whiskers").
Google Interest (Suchvolumen): Deutlich konzentrierter um den Median, wenig Ausreißer.

- Interpretation:
Der Aktienkurs ist volatiler als das Google-Suchinteresse.
Die Verteilung von „Interest“ ist symmetrischer und stabiler.

![Grafik:Histogramme](Bilder_git/histogramme.png)
- Links: BMW Close
Leichte Rechtsschiefe (mehr hohe Werte), aber relativ symmetrisch.
Hohe Frequenz bei Kursen zwischen 65 € und 90 €.

- Rechts: Google Interest
Deutlichere Glockenkurve -> fast normalverteilt.
Mehrheit der Werte zwischen 80 und 90.

- Interpretation:
BMW-Kurse schwanken stärker 
Google-Trends ist konzentrierter und normal verteilt – zeigt gleichmäßiges Nutzerinteresse über die Zeit.

![Grafik:streudiagramm](Bilder_git/streudiagramm.png)
- Was sehen wir?
Jeder Punkt ist ein Zeitpunkt (Woche).
X-Achse: Google-Suchinteresse (Index)
Y-Achse: BMW-Kurs (Index)

- Interpretation:
Die Punkte sind weit gestreut, keine klare lineare Beziehung.
Korrelation ist sehr schwach positiv (wie auch der berechnete Korrelationswert: 0.123).
Es scheint kein starker Zusammenhang zu bestehen – das Interesse in Google beeinflusst die Aktie nicht direkt messbar.


1. Reposition klonen:
   git clone https://github.com/NoahSPBBA/SPBBA.git
2. Benötigte Libraries:
   - `pandas`, `matplotlib`, `seaborn`
  - `statsmodels`


### Projektbeteiligte
Antonia Strohmenger
Noah Wolf
