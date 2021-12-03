# Is Daymart Actually Cheaper?
This repo contains the data and code for Data Visualization article: ["Is Daymart Actually Cheaper? A Comparison of NYUAD's New Convenience Store and its Predecessor".](https://www.thegazelle.org/issue/210/columns/day-mart-convenience-store-predecessor)

## Data
- `daymart_bluemart_prices.csv`

  The original dataset containing the prices of 89 products in Daymart, Bluemart and Lulu Hypermarket in wide format. The Bluemart prices were collected from Bluemart's delivery form, while the Lulu prices were collected from the Lulu Hypermarket website. The Daymart prices were collected by visiting the Daymart store at NYUAD. Each product was also assigned a category.
  
- `daymart_bluemart_prices_no_null.csv`

  Contains only the 63 products for which we have price information from Daymart.
  
- `daymart_bluemart_prices_clean.csv`
  
  This is the same as `daymart_bluemart_prices_no_null.csv` in long format.
  
- `daymart_bluemart_prices_json.json`

  JSON version of `daymart_bluemart_prices_no_null.csv`. Used as input for the shopping cart simulation found [here](https://glitch.com/~south-flannel-binder)
  
- `daymart_bluemart_prices_avg_percent_change.csv`

   Average percentage change for each category, created by pivot table from `daymart_bluemart_prices_no_null.csv`
   
## Code
- `change_data_json.py`

  Code to convert `daymart_bluemart_prices_no_null.csv` into JSON format. Produces `daymart_bluemart_prices_json.json`.
  
- `clean_daymart_prices.py`

  Code to convert `daymart_bluemart_prices_no_null.csv` into long format. Produces `daymart_bluemart_prices_clean.csv`.




  
