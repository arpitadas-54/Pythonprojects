import pandas as pd
df=pd.read_csv('data.csv')#read the csv file

#prints the first 5 rows
print("First 5 rows:")
print(df.head())

#prints the last 5 rows
print("\nLast 5 rows:")
print(df.tail())

#filtering data
filtered_df=df[df['Score']>4.0]
print(filtered_df)

#handling missing data
print(df.isnull()) #check for missing values

#fill missing values with a placeholder(e.g.,'Unknown')
df_filled=df.fillna('Unknown')
print(df_filled)

#drops rows with missing values
df_dropped=df.dropna()
print(df_dropped)

#create a new csv file with the modified dataframe
df.to_csv('modified_data.csv', index=False)