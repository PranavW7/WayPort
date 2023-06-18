import pandas as pd
import json

f = open(r'.\..\datasets\airports-indigo-147.json')
data = json.load(f)
f.close()

df = pd.DataFrame(data)

print(df.shape)

# Only Indian Airports
df2 = df[df["country"] == "India"] 
print(df2.head, df2.shape)

df2.



