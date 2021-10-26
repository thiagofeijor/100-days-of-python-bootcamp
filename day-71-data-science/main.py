import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')

df.isna()

clean_df = df.dropna()
clean_df.tail()
clean_df.head()

low_risk = clean_df.sort_values('Starting Median Salary', ascending=False)
low_risk[['Undergraduate Major', 'Starting Median Salary']].head()

pd.options.display.float_format = '{:,.2f}'.format 
clean_df.groupby('Group').mean()

clean_df['Undergraduate Major'].loc[43]
clean_df.loc[43]

print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]

print(clean_df['Starting Median Salary'].min())
