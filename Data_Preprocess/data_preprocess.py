import pandas as pd

df = pd.read_csv("Quality_of_life_Index_from_2012_to_2026.csv")

#df.replace("2012-Q1", 2012, inplace=True)

#df.replace("2013-Q1", 2013, inplace=True)

#f.to_csv('Quality_of_life_Index_processed.csv', index=False)

df_short = df[274:280]

df_short.to_csv('short_dataset.csv', index=False)
#print(df_short.head())