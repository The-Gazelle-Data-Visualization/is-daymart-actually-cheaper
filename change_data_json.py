import pandas as pd

df = pd.read_csv("daymart_bluemart_prices_no_null.csv")
df = df.rename({"product_name":"name"})
df = df.drop(['price_lulu', 'percentage_change'], axis =1)
df = df.reset_index(drop=False)
df.to_json("daymart_bluemart_prices_json.json", "index")