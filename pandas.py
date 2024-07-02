import pandas as pd
import matplotlib.pyplot as plt

# Wikipedia page for total wealth data
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_total_wealth'

# read HTML tables from URL
tables = pd.read_html(url)

# extract the first table (which contains the wealth data)
wealth_table = tables[0]

wealth_table["Total wealth (USD bn)"] = wealth_table['Total wealth (USD bn)'].replace("—",pd.NA)

# remove unnecessary columns

wealth_table = wealth_table[['Country (or area)', 'Total wealth (USD bn)']]

# remove rows with missing values
wealth_table = wealth_table.dropna()

top10 = wealth_table.head(10)

# plot a bar chart of the top 10 countries by total wealth
plt.bar(top10['Country (or area)'], top10['Total wealth (USD bn)'])
plt.xticks(rotation=90)
plt.ylabel('Total wealth (USD bn)')
plt.title('Top 10 Countries by Total Wealth')
plt.show()
