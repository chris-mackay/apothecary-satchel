import streamlit as st
import pandas as pd

DAGGERFALL = "Elder Scrolls II: Daggerfall"
MORROWIND = "Elder Scrolls III: Morrowind"
OBLIVION = "Elder Scrolls IV: Oblivion"
SKYRIM = "Elder Scrolls V: Skyrim"
ELDER_SCROLLS_ONLINE = "Elder Scrolls Online"

st.title('Apothecary Satchel')
st.markdown('**Filter and search all reagents and effects in the main line Elder Scrolls games**')

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.link_button(DAGGERFALL, "https://en.uesp.net/wiki/Daggerfall:Ingredients")
    st.link_button(SKYRIM, "https://en.uesp.net/wiki/Skyrim:Ingredients")

with col2:
    st.link_button(MORROWIND, "https://en.uesp.net/wiki/Morrowind:Ingredients")
    st.link_button(ELDER_SCROLLS_ONLINE, "https://eso-hub.com/en/alchemy-reagents-and-solvents")

with col3:
    st.link_button(OBLIVION, "https://en.uesp.net/wiki/Oblivion:Ingredients")

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

search_str = st.text_input("Filter reagents :mag:", "")

def highlight_match(val):
    if search_str.lower() in str(val).lower():
        return 'background-color: rgba(139,230,139,0.4)'
    return ''

if game != ELDER_SCROLLS_ONLINE:
    max_weight = float(df['Weight'].max())
    max_value = float(df['Value'].max())
    
    weights = st.slider("Select a weight range :scales:", 0.0, max_weight, (0.0, max_weight))
    st.write("Weight range", weights)

    values = st.slider("Select a value range :moneybag:", 0.0, max_value, (0.0, max_value))
    st.write("Value range", values)

    df = df[df["Weight"].between(weights[0], weights[1])]
    df = df[df["Value"].between(values[0], values[1])]

mask = df.apply(lambda row: row.astype(str).str.contains(search_str, case=False, na=False)).any(axis=1)
df = df[mask]

if search_str != "":
    df = df.style.applymap(highlight_match)

st.write(df)