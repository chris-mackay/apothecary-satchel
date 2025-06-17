import streamlit as st
import pandas as pd

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

st.title('Apothecary Satchel')
st.write('Filter and search all ingredients and effects in The Elder Scrolls V: Skyrim')

df = pd.read_csv('ingredients.csv')

search_str = st.text_input("Filter ingredients", "")

mask = df.apply(lambda row: row.astype(str).str.contains(search_str, case=False, na=False)).any(axis=1)
df = df[mask]

values = st.slider("Select a value range", 0.0, 15.0, (0.0, 15.0))
st.write("Value range", values)

weights = st.slider("Select a weight range", 0.0, 0.5, (0.0, 0.5))
st.write("Weight range", weights)

df = df[df["Value"].between(values[0], values[1])]
df = df[df["Weight"].between(weights[0], weights[1])]

st.write(df)