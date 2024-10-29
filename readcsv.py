import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
#print(df.head(20))
print(df.to_string(index=False))

#read specific col

col_list = ["calories", "duration","age"]
df = pd.read_csv("data.csv", usecols=col_list)
#print(df["duration"])
df.info()
df.head()





#df.plot()
#df["duration"].plot(kind = 'hist')
#df.plot(kind = 'scatter', x = 'duration', y = 'calories')
#plt.show()
