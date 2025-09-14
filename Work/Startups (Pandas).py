import pandas as pd

df = pd.read_csv('Work/Startups in 2021 end.csv', delimiter = ',')
print(df)

print("Data Types: ", df.dtypes)
print("Information: ", df.info())
print("Last three rows: ", df.tail(3))
print("First three rows: ", df.head(3))

print()

print("Using desribe method: ", df.describe())
print("Shape of data frame: ", df.shape)
print()

city = df['City']
print("Cities: ", city)
print()

country_and_cities = df[['Country', 'City']]
print("Countrries and cities: ", country_and_cities)

second_row = df.loc[1]
print(second_row)
print()

second_row_2 = df.loc[[2, 5]]
print(second_row_2)

second_row_slice = df.loc[4:6]
print(second_row_slice)

second_row_condition = df.loc[df['Industry'] == 'Intelligence']
print(second_row_condition)

print("Now using df_index_col")

df_index_col = pd.read_csv('Work/Startups in 2021 end.csv', delimiter = ',')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

second_row_index = df_index_col.loc[1]
print(second_row_index)

second_row_index_2 = df_index_col.loc[1 : 4]
print(second_row_index_2)

second_row_index_3 = df_index_col.loc[df_index_col['City'] == "London"]
print(second_row_index_3)

print("Now using iloc: ")
print()

example_row = df_index_col.iloc[0]
print(example_row)

example_row_2 = df_index_col.iloc[[1, 3, 5]]
print(example_row_2)

example_row_slice = df_index_col.iloc[2:5]
print(example_row_slice)

print("Dropping, renaming etc:")
print()

df.drop(1, axis = 0, inplace = False)
df.drop(index = 2, inplace = False)
print(df)

print()

df.rename(columns = {'Select Investors': 'Investors'}, inplace = False)
print(df)

sorted_df = df.sort_values(by = 'Valuation ($B)')
print(sorted_df.to_string(index = False))