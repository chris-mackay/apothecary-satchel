import streamlit as st
import pandas as pd

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

st.title('Apothecary Satchel')
st.write('Filter and search all ingredients and effects in The Elder Scrolls V: Skyrim')

df = pd.read_csv('ingredients.csv')

search_str = st.text_input("Filter ingredients and effects", "")

mask = df.apply(lambda row: row.astype(str).str.contains(search_str, case=False, na=False)).any(axis=1)
filtered_df = df[mask]

st.write(filtered_df)

