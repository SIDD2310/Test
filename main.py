import streamlit as st
import pandas as pd
import time

st.title('Test')

df = pd.read_csv('SA1_1.csv')

start_time_display = time.time()
st.dataframe(df)
end_time_display = time.time()
time_to_display_df = end_time_display - start_time_display

@st.cache_resource
def save_parquet():
    df.to_parquet("df.parquet", compression='snappy')
    df_read = pd.read_parquet('df.parquet')
    return df_read

df_read = save_parquet()
start_time_read = time.time()
st.dataframe(df_read)
end_time_read = time.time()
time_to_show_parquet = end_time_read - start_time_read

st.write(f"Time to display parquet file: {time_to_show_parquet} seconds")
st.write(f"Time to display original DataFrame: {time_to_display_df} seconds")