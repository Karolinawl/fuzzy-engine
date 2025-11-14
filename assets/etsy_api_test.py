import requests
import numpy as np
import pandas as pd
import plotly.express as px

client_key = #"your_etsy_api_key_here"
url = "https://openapi.etsy.com/v3/application/listings/active"
params = {"limit": 5, "keywords": "crochet"}
headers = {"x-api-key": client_key}

r = requests.get(url, headers=headers, params=params, timeout=30)
print("Status code:", r.status_code)
print(r.text[:1000])