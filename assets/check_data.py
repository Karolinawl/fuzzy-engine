import pandas as pd
import requests
import numpy as np
import plotly.express as px
df = pd.read_csv('fuzzy-engine/data/etsy_shops_data.csv')
print(df.head(10))
print("Rows:", len(df))
print("Columns:", df.columns.tolist())
print(df.info())