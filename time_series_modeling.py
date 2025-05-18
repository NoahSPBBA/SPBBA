#-----------------
#Zeitreihenanalyse
#-----------------

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#------------
# ARIMA-MODEL
#------------
def arima_model():
    df = pd.read_csv("daten_vereint.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    # Nur die Close_Index-Zeitreihe verwenden
    series = df["Close_Index"]

    # ACF und PACF anzeigen
    plot_acf(series.dropna(), lags=30)
    plt.title("Autokorrelation (ACF)")
    plt.show()

    plot_pacf(series.dropna(), lags=30)
    plt.title("Partielle Autokorrelation (PACF)")
    plt.show()

    # Modell schätzen: ARIMA(p, d, q)
    model = ARIMA(series, order=(2, 1, 2))  # Beispielwerte
    model_fit = model.fit()

    # Zusammenfassung
    print(model_fit.summary())

    # Prognose (z. B. 10 Wochen)
    forecast = model_fit.forecast(steps=10)
    print("\nPrognose für die nächsten 10 Wochen:")
    print(forecast)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(series, label="Original")
    plt.plot(forecast.index, forecast, label="Prognose", color="red")
    plt.title("ARIMA Prognose – BMW Close Index")
    plt.xlabel("Datum")
    plt.ylabel("Indexwert")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    arima_model()

#--------------
# SARIMAX-Model
#--------------

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

def sarimax_model():
    # Daten laden
    df = pd.read_csv("daten_vereint.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    y = df["Close_Index"]              # Zielgröße: BMW Aktie
    exog = df["Interest_Index"]        # Exogene Variable: Google Trends

    # SARIMAX-Modell (keine Saisonalität für den Anfang)
    model = SARIMAX(y, exog=exog, order=(2, 1, 2))  # wie ARIMA(2,1,2)
    model_fit = model.fit(disp=False)

    # Zusammenfassung
    print(model_fit.summary())

    # Prognose mit exogenen Werten der nächsten 10 Wochen
    future_exog = [exog.iloc[-1]] * 10  # Einfacher Dummy: gleichbleibendes Interesse
    forecast = model_fit.forecast(steps=10, exog=future_exog)

    print("\nSARIMAX-Prognose (mit Google Trends):")
    print(forecast)

    plt.figure(figsize=(10, 5))
    plt.plot(y, label="Original (BMW Index)")
    plt.plot(forecast.index, forecast, label="SARIMAX Prognose", color="orange")
    plt.title("SARIMAX Prognose – BMW Close Index mit Google Trends")
    plt.xlabel("Datum")
    plt.ylabel("Indexwert")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sarimax_model()