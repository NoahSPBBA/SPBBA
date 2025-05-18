#------------------------
# Statistische Kennzahlen
#------------------------

import pandas as pd

#-----------------
# 1.Lagekennzahlen
#-----------------
def lagekennzahlen():  
    df = pd.read_csv("daten_vereint.csv")

    print("\n--- LAGEKENNZAHLEN ---")

#---------------
# 1.1 Mittelwert
#---------------
    print("\nMittelwerte:")
    print("BMW Aktie (Close):", round(df["Close"].mean(), 2))
    print("BMW Index:", round(df["Close_Index"].mean(), 2))
    print("Google Trends:", round(df["Interest"].mean(), 2))
    print("Google Index:", round(df["Interest_Index"].mean(), 2))

#-----------
# 1.2 Median
#-----------

    print("\nMedian:")
    print("BMW Aktie (Close):", round(df["Close"].median(), 2))
    print("BMW Index:", round(df["Close_Index"].median(), 2))
    print("Google Trends:", round(df["Interest"].median(), 2))
    print("Google Index:", round(df["Interest_Index"].median(), 2))

#-------------
# 1.3 Min. Max
#-------------
    print("\nMinimum:")
    print("BMW Aktie (Close):", round(df["Close"].min(), 2))
    print("Google Trends:", df["Interest"].min())

    print("\nMaximum:")
    print("BMW Aktie (Close):", round(df["Close"].max(), 2))
    print("Google Trends:", df["Interest"].max())

#---------------------------
if __name__ == "__main__":
     lagekennzahlen()
#---------------------------



#----------------
# 2.Streuungsmaße
#---------------- 
def streuungsmaße():
    df = pd.read_csv("daten_vereint.csv")
    print("\n--- STREUUNGSMASSE ---")
     
#-----------------------
# 2.1 Standardabweichung
#-----------------------
    print("\nStandardabweichung:")
    print("BMW Close:", round(df["Close"].std(), 2))
    print("BMW Index:", round(df["Close_Index"].std(), 2))
    print("Google Trends:", round(df["Interest"].std(), 2))
    print("Google Index:", round(df["Interest_Index"].std(), 2))

#------------
# 2.2 Varianz
#------------
    print("\nVarianz:")
    print("BMW Close:", round(df["Close"].var(), 2))
    print("BMW Index:", round(df["Close_Index"].var(), 2))
    print("Google Trends:", round(df["Interest"].var(), 2))
    print("Google Index:", round(df["Interest_Index"].var(), 2))

#---------
# 2.3 Range
#---------
    print("\nRange (Spannweite):")
    print("BMW Close:", round(df["Close"].max() - df["Close"].min(), 2))
    print("Google Trends:", df["Interest"].max() - df["Interest"].min())

#--------------------------
if __name__ == "__main__":
    streuungsmaße()
#--------------------------



#------------------
# 3. Wachstumsraten
#------------------
def wachstumsraten():
    df = pd.read_csv("daten_vereint.csv")
    print("\n--- WACHSTUMSRATEN ---")

#----------------------------
# 3.1 Absolute Wachstumtsrate
#----------------------------
    print("\nAbsolute Wachstumsrate:")
    wachstum_abs = df["Close"].iloc[-1] - df["Close"].iloc[0]
    print(f"BMW Aktie: {round(wachstum_abs, 2)} EUR (von {round(df['Close'].iloc[0], 2)} auf {round(df['Close'].iloc[-1], 2)})")

#--------------------------
# 3.2 Rel. Wachstumsrate (%)
#--------------------------
    print("\nRelative Wachstumsrate:")
    wachstum_rel = (df["Close"].iloc[-1] / df["Close"].iloc[0] - 1) * 100
    print(f"BMW Aktie: {round(wachstum_rel, 2)} %")

#-----------------
# 3.3 Indexbildung
#-----------------
    print("\nIndexbildung (erste Woche = 100):")
    index_neu = df["Close"] / df["Close"].iloc[0] * 100
    print("Letzter Indexwert:", round(index_neu.iloc[-1], 2))

#--------------
# Google Trends
#--------------
    print("\nGoogle Trends:")

    wachstum_trend_abs = df["Interest"].iloc[-1] - df["Interest"].iloc[0]
    wachstum_trend_rel = (df["Interest"].iloc[-1] / df["Interest"].iloc[0] - 1) * 100

    print(f"  Absolute Wachstumsrate: {wachstum_trend_abs}")
    print(f"  Relative Wachstumsrate: {round(wachstum_trend_rel, 2)} %")

    print("\nIndexbildung (letzter Wert):")
    print("  BMW Index:", round(df["Close_Index"].iloc[-1], 2))
    print("  Google Index:", round(df["Interest_Index"].iloc[-1], 2))

#-------------------------
if __name__ == "__main__":
    wachstumsraten()
#-------------------------


#----------------------
# 4. Zusammenhangsmaße
#----------------------
def zusammenhangsmaße():
    df = pd.read_csv("daten_vereint.csv")
    print("\n--- ZUSAMMENHANGSMAßE ---")

#----------------
# 4.1 Korrelation
#----------------
    korrelation = df["Close_Index"].corr(df["Interest_Index"])
    print(f"\nKorrelation (BMW Index vs. Google Index): {round(korrelation, 3)}")

#---------------------------
# 4.2 Kreuzkorrelation (Lag)
#---------------------------
    print("\nKreuzkorrelation mit Lag (Google voraus):")
    
     # Wir prüfen z. B. Lags von 0 bis 5 Wochen
    for lag in range(6):
        shifted_interest = df["Interest_Index"].shift(lag)
        lag_corr = df["Close_Index"].corr(shifted_interest)
        print(f"Lag {lag} Wochen: {round(lag_corr, 3)}")


if __name__ == "__main__":
    zusammenhangsmaße()
#-------------------------

#---------------
# Visualisierung
#---------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#----------------------
# 1. Vis.Lagekennzahlen
#----------------------
def vis_lagekennzahlen():
    df = pd.read_csv("daten_vereint.csv")

    # Boxplot: Verteilung im Vergleich    
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df[["Close", "Interest"]])
    plt.title("Boxplot: Verteilung BMW Close vs. Google Interest")
    plt.grid(True)
    plt.show()

    # Histogramme nebeneinander
    plt.figure(figsize=(12, 5))

    # Histogram für BMW
    plt.subplot(1, 2, 1)
    plt.hist(df["Close"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Histogramm: BMW Close")
    plt.xlabel("Preis")
    plt.ylabel("Häufigkeit")

    # Histogram für Google
    plt.subplot(1, 2, 2)
    plt.hist(df["Interest"], bins=20, color="lightgreen", edgecolor="black")
    plt.title("Histogramm: Google Interest")
    plt.xlabel("Trend-Wert")
    plt.ylabel("Häufigkeit")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    vis_lagekennzahlen()


#-------------------------
# 4. Vis.Zusammenhangsmaße
#-------------------------
def vis_zusammenhangsmaße_kor():
    df = pd.read_csv("daten_vereint.csv")

    plt.figure(figsize=(8, 6))
    plt.scatter(df["Interest_Index"], df["Close_Index"], alpha=0.6)
    plt.title("Streudiagramm: Google Trends vs. BMW Aktie (Indexiert)")
    plt.xlabel("Google Interest (Index)")
    plt.ylabel("BMW Close (Index)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    vis_zusammenhangsmaße_kor()

# lag_korrelation
def vis_lag_kor():
    df = pd.read_csv("daten_vereint.csv")

    max_lag = 20
    lag_values = []
    correlations = []

    for lag in range(max_lag + 1):
        shifted = df["Interest_Index"].shift(lag)
        corr = df["Close_Index"].corr(shifted)
        lag_values.append(lag)
        correlations.append(corr)

    plt.figure(figsize=(10, 5))
    plt.bar(lag_values, correlations, color="steelblue")
    plt.title("Kreuzkorrelation: Google Trends → BMW Close (Index)")
    plt.xlabel("Lag (Wochen)")
    plt.ylabel("Korrelationskoeffizient")
    plt.xticks(range(0, max_lag + 1, 2))
    plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
    plt.grid(True, axis="y")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    vis_lag_kor()

