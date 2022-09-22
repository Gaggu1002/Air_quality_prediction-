import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


df2 =  pd.read_excel("CO2 dataset.xlsx")
df2["Year"] = pd.to_datetime(df2["Year"],format="%Y",)
df2.index = df2["Year"]


final_arima = ARIMA(df2['CO2'],order = (4,1,3)).fit()
def pred(n):
    pred_5=final_arima.forecast(n)
    plt.figure(figsize=(12,5), dpi=100)
    plt.plot(final_arima.fittedvalues)
    plt.plot(pred_5)
    plt.legend(["Original_data","Predicted"])
    plt.savefig("chart.png")
    plt.clf()
    return list(pred_5)