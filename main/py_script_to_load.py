
import dask.dataframe as dd

data_loc = r"https://github.com/fivethirtyeight/uber-tlc-foil-response/uber-trip-data"

df1 = dd.read_csv(r"Data\uber-trip-data\uber-raw-data*.csv")

print(df1.head())