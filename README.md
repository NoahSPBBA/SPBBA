-------------------------------------------------------
## Zeitreihenanalyse: BMW Aktie vs. Google-Trends "BMW"
-------------------------------------------------------

### Projektziel:
Ziel dieses Projekts ist es, eine bivariate Zeitreihenanalyse durchzuführen, um zu untersuchen, ob ein Zusammenhang zwischen dem Google-Suchinteresse an "BMW" und der Kursentwicklung der BMW-Aktie besteht. Neben einer explorativen Analyse werden auch Prognosemodelle getestet.

---------------------------------------------------------------------------------
### Projektstruktur:
- data.exploration.py // Datenimport, Bereinigung, Indexbildung, Visualisierung
- descriptive_stats.py // Lagekennzahlen, Streuungsmaße, Wachstum, Korrelationen
-  time_series_modeling.py // ARIMA & SARIMAX-Modelle inkl. Prognose
-  daten_vereint.csv // Bereinigte, synchronisierte Zeitreihen (Google & BMW)
- README.md # Projektdokumentation
---------------------------------------------------------------------------------


---------------------------------------------------------------------------------
### Analyseüberblick
#### 1. Datenquellen: 
- **BMW Aktie**: Historische Kursdaten (Yahoo Finance)
- **Google Trends**: Suchinteresse für den Begriff „BMW“ (Wöchentlich)

#### 2. Datenaufbereitung
- Vereinheitlichung auf wöchentliche Frequenz
- Indexbildung mit Basiswert = 100
- Inner Join auf gemeinsame Datumswerte

#### 3. Statistische Auswertung
- Lage- und Streuungsmaße (Mittelwert, Median, Varianz, etc.)
- Korrelations- und Kreuzkorrelationsanalyse (Lag-Analyse)
- Prüfung auf Stationarität (ADF-Test)

#### 4. Modellierung
- **ARIMA**-Modell zur univariaten Prognose des BMW-Kurses
- **SARIMAX**-Modell mit Google Trends als exogene Variable
---------------------------------------------------------------------------------

### Ergebnisse

- **Korrelation**: Nur schwacher Zusammenhang zwischen Google Trends und BMW-Aktie
- **Kreuzkorrelation**: Kein klarer Vorlaufeffekt beobachtbar
- **SARIMAX**: Kein signifikanter Einfluss des Google-Suchinteresses
- **ARIMA-Prognose**: Stabile, plausible Vorhersage ohne externe Variablen

  

1. Reposition klonen:
   git clone https://github.com/NoahSPBBA/SPBBA.git
2. Benötigte Libraries:
   - `pandas`, `matplotlib`, `seaborn`
  - `statsmodels`


### Projektbeteiligte
Antonia Strohmenger
Noah Wolf
