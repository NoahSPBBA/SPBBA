## Projekt:  BMW Aktienkurs & Google Trends Analyse ##

## Projektdetails
- Programmiersprache: Python
- Libraries: pandas, matplotlib, seaborn, numpy
- Datenquellen:
- BMW Aktienkurse (CSV-Datei)
- Google Trends Daten zum Suchbegriff "BMW" (CSV-Datei)

## Analyseinhalte
1. Deskriptive Statistik
- Lagekennzahlen (Mittelwert, Median, Spannweite)
- Streuungsmaße (Standardabweichung, Varianz, Range)

    Interpretation:
        BMW-Kurse sind volatiler als das Suchinteresse bei Google.
        Das öffentliche Interesse zeigt eine geringere Schwankung.

2. Wachstumsraten

    BMW Aktie:
        Absolut: +45.66 €
        Relativ: +134.2 %

    Google Trends Interesse:
        Relativ: +21.52 %

    Interpretation:
        Der Aktienkurs hat sich mehr als verdoppelt, während das Suchinteresse nur moderat gestiegen ist.

3. Zusammenhangsanalyse
    Korrelationsanalyse zwischen Google Trends und BMW-Aktienkurs.

    Ergebnis:
        Keine starke lineare Korrelation (Lag 0: 0.123).
        Kein signifikanter Vorlaufeffekt des Google-Suchinteresses auf den Aktienkurs.
   
## Visualisierungen

- Boxplots zur Verteilung von Aktienkurs und Google-Trends-Interesse
- Histogramme zur Kurs- und Interessenverteilung
- Korrelationsdiagramm (Scatter Plot)
- Balkendiagramm zur Visualisierung der Korrelation bei unterschiedlichen Lags

## Ausführung
1. Reposition klonen:
   git clone https://github.com/NoahSPBBA/SPBBA.git
2. Benötigte Libraries installieren:
   pip install pandas matplotlib seaborn
3. Skripte ausführen:
   python data_exploration.py

## Projektbeteiligte
Antonia Strohmenger
Noah Wolf
