import streamlit as st
import pandas as pd

WEIGHT_MAX_MORROWIND = 50.0
WEIGHT_MAX_OBLIVION = 5.0
WEIGHT_MAX_SKYRIM = 1.0

VALUE_MAX_MORROWIND = 500.0
VALUE_MAX_OBLIVION = 75.0
VALUE_MAX_SKYRIM = 250.0

st.title('Apothecary Satchel')
st.write('Filter and search all ingredients and effects in the following Elder Scrolls games')

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    st.link_button("The Elder Scrolls III: Morrowind", "https://en.uesp.net/wiki/Morrowind:Ingredients")

with col2:
    st.link_button("The Elder Scrolls IV: Oblivion", "https://en.uesp.net/wiki/Oblivion:Ingredients")

with col3:
    st.link_button("The Elder Scrolls V: Skyrim", "https://en.uesp.net/wiki/Skyrim:Ingredients")

with col4:
    st.link_button("The Elder Scrolls Online", "https://eso-hub.com/en/alchemy-reagents-and-solvents")

game = st.radio(
    "Select game to view ingredients",
    ["The Elder Scrolls III: Morrowind", "The Elder Scrolls IV: Oblivion", "The Elder Scrolls V: Skyrim", "The Elder Scrolls Online"]
)

if game == "The Elder Scrolls III: Morrowind":
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_morrowind.csv")
    search_str = st.text_input("Filter ingredients", "")
elif game == "The Elder Scrolls IV: Oblivion":
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_oblivion.csv")
    search_str = st.text_input("Filter ingredients", "")
elif game == "The Elder Scrolls V: Skyrim":
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_skyrim.csv")
    search_str = st.text_input("Filter ingredients", "")
else:
    st.link_button("Alchemy Simulator", "https://eso-hub.com/en/potion-maker")
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_eso.csv")
    search_str = st.text_input("Filter ingredients", "")

def highlight_match(val):
    if search_str.lower() in str(val).lower():
        return 'background-color: rgba(139,230,139,0.4)'
    return ''

if game != "The Elder Scrolls Online":
    if game == "The Elder Scrolls III: Morrowind":
        weights = st.slider("Select a weight range", 0.0, WEIGHT_MAX_MORROWIND, (0.0, WEIGHT_MAX_MORROWIND))
        st.write("Weight range", weights)

        values = st.slider("Select a value range", 0.0, VALUE_MAX_MORROWIND, (0.0, VALUE_MAX_MORROWIND))
        st.write("Value range", values)

        df = df[df["Weight"].between(weights[0], weights[1])]
        df = df[df["Value"].between(values[0], values[1])]

    elif game == "The Elder Scrolls IV: Oblivion":
        weights = st.slider("Select a weight range", 0.0, WEIGHT_MAX_OBLIVION, (0.0, WEIGHT_MAX_OBLIVION))
        st.write("Weight range", weights)

        values = st.slider("Select a value range", 0.0, VALUE_MAX_OBLIVION, (0.0, VALUE_MAX_OBLIVION))
        st.write("Value range", values)

        df = df[df["Weight"].between(weights[0], weights[1])]

        df = df[df["Value"].between(values[0], values[1])]
    elif game == "The Elder Scrolls V: Skyrim":
        weights = st.slider("Select a weight range", 0.0, WEIGHT_MAX_SKYRIM, (0.0, WEIGHT_MAX_SKYRIM))
        st.write("Weight range", weights)

        values = st.slider("Select a value range", 0.0, VALUE_MAX_SKYRIM, (0.0, VALUE_MAX_SKYRIM))
        st.write("Value range", values)

        df = df[df["Weight"].between(weights[0], weights[1])]
        df = df[df["Value"].between(values[0], values[1])]

mask = df.apply(lambda row: row.astype(str).str.contains(search_str, case=False, na=False)).any(axis=1)
df = df[mask]

if search_str != "":
    df = df.style.applymap(highlight_match)

st.write(df)