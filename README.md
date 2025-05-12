## Zeitreihenanalyse: Google Trends Analyse

## Projektbeschreibung
In diesem Projekt analysieren wir die Entwicklung von Suchanfragen aus Google Trends. 
Dabei untersuchen wir unter anderem Trends zu Kryptowährungen sowie den Vergleich zwischen zwei bekannten Persönlichkeiten aus dem Sport. 
Ziel ist es, mithilfe von Datenanalysen und Visualisierungen interessante Erkenntnisse über das Suchverhalten von Nutzern zu gewinnen.

## Analyse-Themen
Bitcoin vs. Ethereum (Kryptowährungstrends)
Cristiano Ronaldo vs. Lionel Messi (Sportliche Popularität)

## Dantenquelle
Die verwendeten Daten wurden direkt über [Google Trends](https://trends.google.com/) heruntergeladen.

| Datensatz                 | Beschreibung                   |
|---------------------------|---------------------------------|
| `google_btc_eth.csv`      | Suchtrends zu Bitcoin & Ethereum |
| `google_ronaldo_messi.csv`| Suchtrends zu Ronaldo & Messi  |

## Branches:
- Master/Main
- Data(prep.)
- analysis: btc - eth
- analysis: ronaldo - messi
- merge- report (bericht)

## Projektstruktur
google-trends-analysis/
- data/                  # Roh- und bereinigte Datensätze
- notebooks/             # Jupyter Notebooks für Analysen
- src/                   # Python-Module für Datenverarbeitung
- tests/                 # Unit-Tests für Python-Module
- .gitignore             # Ignorierte Dateien
- requirements.txt       # Python-Abhängigkeiten
- README.md              # Projektbeschreibung

  
## Teilnehmer:
- Noah Wolf
- Antonia Strohmenger
  
## Installation:
1. Repository klonen:
- git clone https://github.com/username/SPBBA.git
2. ```bash
git clone https://github.com/euer-repo/world-bank-wdi-analysis.git
cd world-bank-wdi-analysis
pip install -r requirements.txt
3.

## Quellen:https://trends.google.com/trends?geo=DE&hl=de
