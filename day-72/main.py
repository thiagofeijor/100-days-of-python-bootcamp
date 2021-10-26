import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

df.DATE = pd.to_datetime(df.DATE)

#df.groupby("TAG").count()
#df.head()

pivoted_df = clean_df.pivot(index='DATE', columns='TAG', values='POSTS')
pivoted_df.fillna(0, inplace=True) 
pivoted_df

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in pivoted_df.columns:
    plt.plot(pivoted_df.index, pivoted_df[column],
             linewidth=3, label=pivoted_df[column].name)

plt.legend(fontsize=16)
