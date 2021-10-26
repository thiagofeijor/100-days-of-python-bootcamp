import pandas as pd
import matplotlib.pyplot as plt
sets = pd.read_csv('data/sets.csv')

sets[sets["year"] == 1949]

sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()

sets_by_year['set_num'].tail()

plt.plot(sets_by_year.index, sets_by_year.set_num)

plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

theme_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
theme_by_year.rename(columns = {'theme_id': 'nr_themes'}, inplace = True)
theme_by_year.tail()

ax1 = plt.gca()
ax2 = ax1.twinx() 

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(theme_by_year.index[:-2], theme_by_year.nr_themes[:-2], 'b')

ax1.set_xlabel('Year')
ax1.set_xlabel('Number of sets', color='green')
ax2.set_xlabel('Number of themes', color='blue')

"""<img src="https://i.imgur.com/49FNOHj.jpg">"""