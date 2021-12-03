import pandas as pd
df = pd.read_csv("daymart_bluemart_prices_no_null.csv")
new_df = pd.wide_to_long(df, "price_", i="product_name", j="store", suffix='\\w+')
new_df = new_df.rename({"price_":"price"}, axis=1)
new_df.to_csv("daymart_bluemart_prices_clean.csv", index=True)