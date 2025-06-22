import streamlit as st
import pandas as pd

DAGGERFALL = "The Elder Scrolls II: Daggerfall"
MORROWIND = "The Elder Scrolls III: Morrowind"
OBLIVION = "The Elder Scrolls IV: Oblivion"
SKYRIM = "The Elder Scrolls V: Skyrim"
ELDER_SCROLLS_ONLINE = "The Elder Scrolls Online"

WEIGHT_MAX_DAGGERFALL = 3.0
WEIGHT_MAX_MORROWIND = 50.0
WEIGHT_MAX_OBLIVION = 5.0
WEIGHT_MAX_SKYRIM = 1.0

VALUE_MAX_DAGGERFALL = 500.0
VALUE_MAX_MORROWIND = 500.0
VALUE_MAX_OBLIVION = 75.0
VALUE_MAX_SKYRIM = 250.0

st.title('Apothecary Satchel')
st.write('Filter and search all reagents and effects in the main line Elder Scrolls games')

col1, col2, col3 = st.columns([1.08,1,1])

with col1:
    st.link_button(DAGGERFALL, "https://en.uesp.net/wiki/Daggerfall:Ingredients")
    st.link_button(MORROWIND, "https://en.uesp.net/wiki/Morrowind:Ingredients")

with col2:
    st.link_button(OBLIVION, "https://en.uesp.net/wiki/Oblivion:Ingredients")
    st.link_button(SKYRIM, "https://en.uesp.net/wiki/Skyrim:Ingredients")

with col3:
    st.link_button(ELDER_SCROLLS_ONLINE, "https://eso-hub.com/en/alchemy-reagents-and-solvents")

game = st.radio(
    "Select game to view reagents",
    [DAGGERFALL, 
     MORROWIND, 
     OBLIVION, 
     SKYRIM, 
     ELDER_SCROLLS_ONLINE]
)

if game == DAGGERFALL:
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_daggerfall.csv")

elif game == MORROWIND:
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_morrowind.csv")

elif game == OBLIVION:
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_oblivion.csv")

elif game == SKYRIM:
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_skyrim.csv")

elif game == ELDER_SCROLLS_ONLINE:
    st.link_button("Alchemy Simulator", "https://eso-hub.com/en/potion-maker")
    st.link_button("Market Trade Center", "https://eso-hub.com/en/trading?category=4&sort=last_seen_at&sortdir=desc&server=NA")
    df = pd.read_csv("https://raw.githubusercontent.com/chris-mackay/apothecary-satchel/refs/heads/main/data_eso.csv")

search_str = st.text_input("Filter reagents", "")

def highlight_match(val):
    if search_str.lower() in str(val).lower():
        return 'background-color: rgba(139,230,139,0.4)'
    return ''

if game != ELDER_SCROLLS_ONLINE:
    if game == DAGGERFALL:
        weights = st.slider("Select a weight range", 0.0, WEIGHT_MAX_DAGGERFALL, (0.0, WEIGHT_MAX_DAGGERFALL))
        st.write("Weight range", weights)

        values = st.slider("Select a value range", 0.0, VALUE_MAX_DAGGERFALL, (0.0, VALUE_MAX_DAGGERFALL))
        st.write("Value range", values)

    elif game == MORROWIND:
        weights = st.slider("Select a weight range", 0.0, WEIGHT_MAX_MORROWIND, (0.0, WEIGHT_MAX_MORROWIND))
        st.write("Weight range", weights)

        values = st.slider("Select a value range", 0.0, VALUE_MAX_MORROWIND, (0.0, VALUE_MAX_MORROWIND))
        st.write("Value range", values)

    elif game == OBLIVION:
        weights = st.slider("Select a weight range", 0.0, WEIGHT_MAX_OBLIVION, (0.0, WEIGHT_MAX_OBLIVION))
        st.write("Weight range", weights)

        values = st.slider("Select a value range", 0.0, VALUE_MAX_OBLIVION, (0.0, VALUE_MAX_OBLIVION))
        st.write("Value range", values)

    elif game == SKYRIM:
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