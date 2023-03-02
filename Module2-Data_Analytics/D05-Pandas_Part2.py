import pandas as pd
import numpy as np
minwages = pd.read_csv("/Users/ko/Downloads/realwage.csv")
minwages["Country"].unique()
minwages.describe()
minwages.duplicated()
minwages.keys()
minwages["Date"]=pd.to_datetime(minwages["Time"])
minwages.sample(5)
minwages.dtypes
minwages["Time"].sort_values().describe()

minwages["Year"], minwages["day"], minwages["Month"] = minwages["Time"].str.split("-").str(0)
minwages.head()
minwages["Years"] = minwages["Date"].astype("str").str.split("-").str[0].astype(int)
minwages.head()
minwages.isna()
minwages.dropna()
minwages.drop("Unnamed: 0", axis = 1, inplace=True)
minwages
minwages[minwages["value"]]
minwages[(minwages['Country'] == "United States") & (minwages['Pay period'] == 'Annual')].dropna().describe
minwages.index = minwages["Country"]
minwages["value"].loc["Ireland"].describe()
minwages.reset_index(drop=True,inplace=True)

minwages.groupby(["Country", "Pay period", "Series"]).mean()
