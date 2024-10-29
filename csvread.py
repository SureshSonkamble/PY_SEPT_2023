#Suresh Sonkamble
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')

#new_df = df.dropna() #dropna remove empty cell
#print(new_df.to_string())
df.duplicated()  #remove duplicate
print(df.to_string())
print(df.info())
#print(pd.options.display.max_rows)
#print(df.head())
df.plot()
plt.show()
