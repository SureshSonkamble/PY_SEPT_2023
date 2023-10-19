import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
#print(df.head(20))
#print(df.to_string()) 
#df.plot()
#df["duration"].plot(kind = 'hist')
df.plot(kind = 'scatter', x = 'duration', y = 'calories')
plt.show()
