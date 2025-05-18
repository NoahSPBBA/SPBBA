import pandas as pd


def read_data(aktie_trends):


# ------------------------------------------
# Pfade zu den Datein
# ------------------------------------------
    aktien_pfad = r"C:\Users\noahw\Documents\FH Business Analytics\6. Semester\Vertiefung BBA\Menden\bmw_aktie.csv"
    trends_pfad = r"C:\Users\noahw\Documents\FH Business Analytics\6. Semester\Vertiefung BBA\Menden\googletrends_bmw.csv"

# ------------------------------------------
# 1. BMW-Aktien-Daten einlesen und bereinigen
# ------------------------------------------
    bmw_df = pd.read_csv(aktien_pfad)

# Datum in UTC konvertieren und auf reines Datum kürzen
    bmw_df["Date"] = pd.to_datetime(bmw_df["Date"], utc=True).dt.date

# Nur relevante Spalten verwenden
    bmw_clean = bmw_df[["Date", "Close"]].copy()

# Index-Spalte berechnen 
    bmw_clean["Close_Index"] = bmw_clean["Close"] / bmw_clean["Close"].iloc[0] * 100

# ------------------------------------------
# 2. Google Trends-Daten einlesen und bereinigen
# ------------------------------------------
    with open(trends_pfad, "r", encoding="utf-8") as f:
        lines = f.readlines()

# Nur gültige Datenzeilen behalten
    data_lines = [line.strip() for line in lines if "," in line and "Woche" not in line]
    google_data = [line.split(",") for line in data_lines]

# In DataFrame umwandeln
    google_df = pd.DataFrame(google_data, columns=["Week", "Interest"])

# Datumsformat und Typen konvertieren
    google_df["Week"] = pd.to_datetime(google_df["Week"], utc=True).dt.date
    google_df["Interest"] = pd.to_numeric(google_df["Interest"])

# Spalte für Zusammenführung umbenennen
    google_df = google_df.rename(columns={"Week": "Date"})

# ------------------------------------------
# 3. Zusammenführen (inner join auf 'Date')
# ------------------------------------------
    combined_df = pd.merge(bmw_clean, google_df, on="Date", how="inner")

# Index-Spalte für Google Trends berechnen 
    if not combined_df.empty:
     combined_df["Interest_Index"] = combined_df["Interest"] / combined_df["Interest"].iloc[0] * 100
    else:
        print("Warnung: Keine gemeinsamen Zeitpunkte gefunden – prüfe die Datumsformate.")

def csv_combined(combined_df):
# ------------------------------------------
# 4. CSV speichern und Vorschau
# ------------------------------------------
    combined_df.to_csv("daten_vereint.csv", index=False)

    print("Daten erfolgreich vorbereitet und gespeichert als 'daten_vereint.csv'.")
    print(combined_df.head())

def vis_1():
# Visualisierung
    import matplotlib.pyplot as plt

# --------------------------------------
# Datei einlesen (zuvor gespeichert)
# --------------------------------------
    df = pd.read_csv("daten_vereint.csv")

# --------------------------------------
# Diagramm erstellen
# --------------------------------------
    plt.figure(figsize=(12, 6))

    plt.plot(df["Date"], df["Close_Index"], label="BMW Aktie (Index)", linewidth=2)
    plt.plot(df["Date"], df["Interest_Index"], label="Google Trends (Index)", linewidth=2)

    # Optional: Basislinie bei 100
    plt.axhline(100, color="gray", linestyle="--", linewidth=1)

    # Diagramm formatieren
    plt.title("BMW Aktie vs. Google-Suchinteresse (indexiert)")
    plt.xlabel("Datum")
    plt.ylabel("Indexwert (Basis = 100)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Diagramm anzeigen
    plt.show()

if __name__ == "__main__":
    vis_1()