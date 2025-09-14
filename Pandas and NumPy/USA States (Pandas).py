import pandas as pd

df = pd.read_csv('Work/RealEstate-USA.csv', delimiter = ",", index_col = 'brokered_by')

print (df)

print(df.dtypes)
print(df.describe())
print(df.shape)

print()

sample_data = df['status']
print(sample_data)
print()

sample_data2 = df[['status', 'price']]
print(sample_data2)

print()
print("df_index_col")
print()

df_index_col = pd.read_csv('Work/RealEstate-USA.csv', delimiter = ",", index_col = 'brokered_by')

print(df_index_col)
print(df_index_col.info())
print(df_index_col.dtypes)

second_row_index = df_index_col.loc[103378]
print(second_row_index)

second_row_index2 = df_index_col.loc[df_index_col['price'] > 50000]
print(second_row_index2)

print()
print("Using 'iloc'")
print()

second_row_iloc = df_index_col.iloc[0]
print(second_row_iloc)

second_row_iloc2 = df_index_col.iloc[[1, 3, 5]]
print(second_row_iloc2)

print()
print("Pandas' Dataframe Manupulation")
print()

df.drop(df.index[1])
df.drop(df.index[2])
df.drop(df.index[3])

df.rename(columns = {'status' : 'status_changed'}, inplace = False)

selected_rows = df.query('price > 50000')
print(selected_rows.to_string())
print(len(selected_rows))