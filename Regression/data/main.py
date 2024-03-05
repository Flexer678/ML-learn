import pandas as pd
import matplotlib.pyplot as plt
pumpkins = pd.read_csv('./Regression/data/US-pumpkins.csv')
pumpkins.head()

print(pumpkins.head())

#columns to select??? 
columns_to_select = ['Package', 'Low Price', 'High Price', 'Date']

#getting 
pumpkins = pumpkins.loc[:, columns_to_select]

print(pumpkins)
# What function would you use to view the last five rows?
pumpkins.isnull().sum()

price = (pumpkins['Low Price'] + pumpkins['High Price']) / 2

month = pd.DatetimeIndex(pumpkins['Date']).month


new_pumpkins = pd.DataFrame({'Month': month, 'Package': pumpkins['Package'], 'Low Price': pumpkins['Low Price'],'High Price': pumpkins['High Price'], 'Price': price})
pumpkins = pumpkins[pumpkins['Package'].str.contains('bushel', case=True, regex=True)]

new_pumpkins.loc[new_pumpkins['Package'].str.contains('1 1/9'), 'Price'] = price/(1 + 1/9)

new_pumpkins.loc[new_pumpkins['Package'].str.contains('1/2'), 'Price'] = price/(1/2)



price = new_pumpkins.Price
month = new_pumpkins.Month
plt.scatter(price, month)
plt.show()