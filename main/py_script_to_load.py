
import dask.dataframe as dd
import datetime
import pytz

base_code_map = {"B02512":"Unter","B02598":"Hinter","B02617":"Weiter","B02682":"Schmecken","B02764":"Danach-NY","B02765":"Grun","B02835":"Dreist","B02836":"Drinnen"}


def raw_data_14_insert(data_url_14,db_url):
    df1 = dd.read_csv(data_url_14)
    df1 = df1.fillna("__")

    
    df1['Base'] = df1['Base'].map(base_code_map)

    df1['Date/Time'] = dd.to_datetime(df1['Date/Time'])
    df1['Date/Time'] = df1['Date/Time'].dt.tz_localize(pytz.timezone('America/New_York')).dt.tz_convert(pytz.utc)

    df1.to_sql("test_table1",db_url,index=True,if_exists='replace',parallel=False)


def raw_data_15_insert(data_url_15,db_url):
    # pass
    df2 = dd.read_csv(data_url_15)
    df2 = df2.fillna("__")

    df2['Dispatching_base_num'] = df2['Dispatching_base_num'].map(base_code_map)
    df2['Affiliated_base_num'] = df2['Affiliated_base_num'].map(base_code_map)

    df2['Pickup_date'] = dd.to_datetime(df2['Pickup_date'])
    df2['Pickup_date'] = df2['Pickup_date'].dt.tz_localize(pytz.timezone('America/New_York')).dt.tz_convert(pytz.utc)

    df2.to_sql("test_table3",db_url,index=True,if_exists='replace',parallel=False)




def lookup_insert(data_url_lookup,db_url):
    # pass
    df_lookup = dd.read_csv(data_url_lookup)
    df_lookup.to_sql("test_table2_lookup",db_url,index=True,if_exists='replace',parallel=False)


if __name__ == "__main__":
    db_url = "mysql://root:root@mysql_container:3306/test_db"
    data_url_15 = r"Data/uber-raw-data-janjune-15.csv"
    data_url_14 = r"Data/uber-raw-data*4.csv"
    data_url_lookup = r"Data/taxi-zone-lookup.csv"

    # engine=

    raw_data_14_insert(data_url_14,db_url)
    print("14 inserted successfully to database")
    raw_data_15_insert(data_url_15,db_url)
    print("15 inserted successfully to database")
    lookup_insert(data_url_lookup,db_url)
    print("lookup inserted successfully to database")

    print("Insertion finished")


