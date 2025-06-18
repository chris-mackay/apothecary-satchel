import streamlit as st
import pandas as pd
from io import StringIO

st.title('Apothecary Satchel')
st.write('Filter and search all ingredients and effects in The Elder Scrolls V: Skyrim and The Elder Scrolls Online')

st.link_button("UESP Skyrim", "https://en.uesp.net/wiki/Skyrim:Ingredients")
st.link_button("UESP Oblivion", "https://en.uesp.net/wiki/Oblivion:Ingredients")
st.link_button("ESO HUB", "https://eso-hub.com/en/alchemy-reagents-and-solvents")

game = st.radio(
    "Select game to view ingredients",
    ["The Elder Scrolls V: Skyrim", "The Elder Scrolls IV: Oblivion", "The Elder Scrolls Online"]
)

if game == "The Elder Scrolls V: Skyrim":
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_skyrim.csv")

    search_str = st.text_input("Filter ingredients", "")

    values = st.slider("Select a value range", 0.0, 15.0, (0.0, 15.0))
    st.write("Value range", values)

    weights = st.slider("Select a weight range", 0.0, 0.5, (0.0, 0.5))
    st.write("Weight range", weights)

    df = df[df["Value"].between(values[0], values[1])]
    df = df[df["Weight"].between(weights[0], weights[1])]
elif game == "The Elder Scrolls IV: Oblivion":
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_oblivion.csv")
    search_str = st.text_input("Filter ingredients", "")
else:
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_eso.csv")
    search_str = st.text_input("Filter ingredients", "")

mask = df.apply(lambda row: row.astype(str).str.contains(search_str, case=False, na=False)).any(axis=1)
df = df[mask]

st.write(df)