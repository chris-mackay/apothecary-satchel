import streamlit as st
import pandas as pd
from io import StringIO

st.title('Apothecary Satchel')
st.write('Filter and search all ingredients and effects in The Elder Scrolls V: Skyrim and The Elder Scrolls Online')

st.link_button("UESP Skyrim", "https://en.uesp.net/wiki/Skyrim:Ingredients")
st.link_button("ESO HUB", "https://eso-hub.com/en/alchemy-reagents-and-solvents")

game = st.radio(
    "Select game to view ingredients",
    ["The Elder Scrolls V: Skyrim", "The Elder Scrolls Online"]
)

data_skyrim = StringIO("""Ingredient,Weight,Value,PrimaryEffect,SecondaryEffect,TertiaryEffect,QuaternaryEffect
Abecean Longfin,0.5,15,Weakness to Frost,Fortify Sneak,Weakness to Poison,Fortify Restoration
Bear Claws,0.1,2,Restore Stamina,Fortify Health,Fortify One-Handed,Damage Magicka Regen
Bee,0.1,3,Restore Stamina,Ravage Stamina,Regenerate Stamina,Weakness to Shock
Beehive Husk,1,5,Resist Poison,Fortify Light Armor,Fortify Sneak,Fortify Destruction
Bleeding Crown,0.3,10,Weakness to Fire,Fortify Block,Weakness to Poison,Resist Magic
Blisterwort,0.2,12,Damage Stamina,Restore Health,Frenzy,Fortify Smithing
Blue Butterfly Wing,0.1,2,Damage Stamina,Damage Magicka Regen,Fortify Conjuration,Fortify Enchanting
Blue Dartwing,0.1,1,Resist Shock,Restore Health,Fortify Pickpocket,Fear
Blue Mountain Flower,0.1,2,Restore Health,Fortify Conjuration,Fortify Health,Damage Magicka Regen
Bone Meal,0.5,5,Damage Stamina,Fortify Conjuration,Resist Fire,Ravage Stamina
Briar Heart,0.5,20,Restore Magicka,Fortify Block,Paralysis,Fortify Magicka
Butterfly Wing,0.1,3,Restore Health,Lingering Damage Stamina,Fortify Barter,Damage Magicka
Canis Root,0.1,5,Damage Stamina,Fortify Marksman,Fortify One-Handed,Paralysis
Charred Skeever Hide,0.5,1,Restore Stamina,Resist Poison,Cure Disease,Restore Health
Chaurus Eggs,0.2,10,Weakness to Poison,Fortify Stamina,Damage Magicka,Invisibility
Chicken's Egg,0.5,2,Resist Magic,Waterbreathing,Damage Magicka Regen,Lingering Damage Stamina
Creep Cluster,0.2,1,Restore Magicka,Fortify Carry Weight,Damage Stamina Regen,Weakness to Magic
Crimson Nirnroot,0.2,10,Damage Health,Invisibility,Damage Stamina,Resist Magic
Cyrodilic Spadetail,0.3,15,Damage Stamina,Fear,Fortify Restoration,Ravage Health
Daedra Heart,0.5,250,Damage Stamina Regen,Damage Magicka,Restore Health,Fear
Deathbell,0.1,4,Damage Health,Ravage Stamina,Slow,Weakness to Poison
Dragon's Tongue,0.1,5,Resist Fire,Fortify Barter,Fortify Illusion,Fortify Two-Handed
Dwarven Oil,0.3,15,Weakness to Magic,Regenerate Magicka,Fortify Illusion,Restore Magicka
Ectoplasm,0.1,25,Restore Magicka,Fortify Destruction,Fortify Magicka,Damage Health
Elves Ear,0.1,10,Restore Magicka,Weakness to Frost,Fortify Marksman,Resist Fire
Eye of Sabre Cat,0.1,2,Restore Stamina,Damage Magicka,Ravage Health,Restore Health
Falmer Ear,0.2,10,Damage Health,Frenzy,Resist Poison,Fortify Lockpicking
Fire Salts,0.3,50,Weakness to Frost,Restore Magicka,Resist Fire,Regenerate Magicka
Fly Amanita,0.1,2,Resist Fire,Frenzy,Fortify Two-Handed,Regenerate Stamina
Frost Mirriam,0.1,1,Resist Frost,Fortify Sneak,Ravage Magicka,Damage Stamina Regen
Frost Salts,0.3,100,Weakness to Fire,Resist Frost,Restore Magicka,Fortify Conjuration
Garlic,0.3,1,Resist Poison,Fortify Stamina,Regenerate Magicka,Regenerate Health
Giant Lichen,0.3,5,Ravage Health,Weakness to Poison,Weakness to Shock,Restore Magicka
Giant's Toe,1,20,Damage Stamina,Fortify Carry Weight,Fortify Health,Damage Stamina Regen
Glow Dust,0.5,20,Damage Magicka,Fortify Destruction,Damage Magicka Regen,Resist Shock
Glowing Mushroom,0.2,5,Resist Shock,Fortify Destruction,Fortify Smithing,Fortify Health
Grass Pod,0.1,1,Resist Poison,Ravage Magicka,Fortify Alteration,Restore Magicka
Hagraven Claw,0.3,20,Resist Magic,Lingering Damage Magicka,Fortify Enchanting,Fortify Barter
Hagraven Feathers,0.1,20,Damage Magicka,Frenzy,Fortify Conjuration,Weakness to Shock
Hanging Moss,0.3,1,Damage Magicka,Damage Magicka Regen,Fortify Health,Fortify One-Handed
Hawk Beak,0.3,15,Restore Stamina,Resist Frost,Fortify Carry Weight,Resist Shock
Hawk Feathers,0.1,15,Cure Disease,Fortify Light Armor,Fortify One-Handed,Fortify Sneak
Histcarp,0.3,6,Restore Stamina,Fortify Magicka,Damage Stamina Regen,Waterbreathing
Honeycomb,1,5,Restore Stamina,Fortify Block,Fortify Light Armor,Ravage Stamina
Human Flesh,0.3,1,Damage Health,Paralysis,Restore Magicka,Fortify Sneak
Human Heart,1,0,Damage Health,Damage Magicka Regen,Damage Magicka,Frenzy
Ice Wraith Teeth,0.3,30,Weakness to Frost,Fortify Heavy Armor,Invisibility,Weakness to Fire
Imp Stool,0.3,0,Damage Health,Paralysis,Lingering Damage Health,Restore Health
Jarrin Root,0.5,10,Damage Health,Damage Stamina,Damage Magicka,Damage Magicka Regen
Jazbay Grapes,0.2,1,Weakness to Magic,Fortify Magicka,Regenerate Magicka,Ravage Health
Juniper Berries,0.1,1,Weakness to Fire,Regenerate Health,Fortify Marksman,Damage Stamina Regen
Large Antlers,0.1,2,Restore Stamina,Fortify Stamina,Slow,Damage Stamina Regen
Lavender,0.1,1,Resist Magic,Fortify Stamina,Ravage Magicka,Fortify Conjuration
Luna Moth Wing,0.1,5,Damage Magicka,Fortify Light Armor,Regenerate Health,Invisibility
Moon Sugar,0.3,50,Weakness to Fire,Resist Frost,Restore Magicka,Regenerate Magicka
Mora Tapinella,0.3,4,Restore Magicka,Lingering Damage Health,Regenerate Stamina,Fortify Illusion
Mudcrab Chitin,0.3,2,Restore Stamina,Cure Disease,Resist Poison,Resist Fire
Niamira's Rot,0.3,0,Damage Magicka,Fear,Fortify Lockpicking,Regenerate Health
Nightshade,0.1,8,Damage Health,Damage Magicka Regen,Lingering Damage Stamina,Fortify Destruction
Nirnroot,0.2,10,Damage Health,Damage Stamina,Invisibility,Resist Magic
Nordic Barnacle,0.2,5,Damage Magicka,Waterbreathing,Regenerate Health,Fortify Pickpocket
Orange Dartwing,0.1,1,Restore Stamina,Ravage Magicka,Fortify Pickpocket,Lingering Damage Health
Pearl,0.1,2,Restore Stamina,Restore Magicka,Fortify Block,Resist Shock
Pine Thrush Egg,0.5,2,Restore Stamina,Fortify Lockpicking,Weakness to Poison,Resist Shock
Powdered Mammoth Tusk,0.1,2,Restore Stamina,Weakness to Fire,Fortify Sneak,Fear
Purple Mountain Flower,0.1,2,Restore Stamina,Fortify Sneak,Lingering Damage Magicka,Resist Frost
Red Mountain Flower,0.1,2,Restore Magicka,Ravage Magicka,Fortify Magicka,Damage Health
River Betty,0.3,15,Damage Health,Fortify Alteration,Slow,Fortify Carry Weight
Rock Warbler Egg,0.5,2,Restore Health,Fortify One-Handed,Damage Stamina,Weakness to Magic
Sabre Cat Tooth,0.1,2,Restore Stamina,Fortify Heavy Armor,Fortify Smithing,Weakness to Poison
Salt Pile,0.2,2,Weakness to Magic,Fortify Restoration,Slow,Regenerate Magicka
Scaly Pholiata,0.3,4,Weakness to Magic,Fortify Illusion,Regenerate Stamina,Fortify Carry Weight
Silverside Perch,0.3,15,Restore Stamina,Damage Stamina Regen,Ravage Health,Resist Frost
Skeever Tail,0.2,3,Damage Stamina Regen,Ravage Health,Damage Health,Fortify Light Armor
Slaughterfish Egg,0.2,3,Resist Poison,Fortify Pickpocket,Lingering Damage Health,Fortify Stamina
Slaughterfish Scales,0.1,3,Resist Frost,Lingering Damage Health,Fortify Heavy Armor,Fortify Block
Small Antlers,0.1,2,Weakness to Poison,Fortify Restoration,Lingering Damage Stamina,Damage Health
Small Pearl,0.1,2,Restore Stamina,Fortify One-Handed,Fortify Restoration,Resist Frost
Snowberries,0.1,4,Resist Fire,Fortify Enchanting,Resist Frost,Resist Shock
Spider Egg,0.2,5,Damage Stamina,Damage Magicka Regen,Fortify Lockpicking,Fortify Marksman
Spriggan Sap,0.2,15,Damage Magicka Regen,Fortify Enchanting,Fortify Smithing,Fortify Alteration
Swamp Fungal Pod,0.5,3,Resist Shock,Lingering Damage Magicka,Paralysis,Restore Health
Taproot,0.5,15,Weakness to Magic,Fortify Illusion,Regenerate Magicka,Restore Magicka
Thistle Branch,0.1,1,Resist Frost,Ravage Stamina,Resist Poison,Fortify Heavy Armor
Torchbug Thorax,0.1,1,Restore Stamina,Lingering Damage Magicka,Weakness to Magic,Fortify Stamina
Troll Fat,1,15,Resist Poison,Fortify Two-Handed,Frenzy,Damage Health
Tundra Cotton,0.1,1,Resist Magic,Fortify Magicka,Fortify Block,Fortify Barter
Vampire Dust,0.2,25,Invisibility,Regenerate Health,Restore Magicka,Cure Disease
Void Salts,0.2,125,Weakness to Shock,Resist Magic,Damage Health,Fortify Magicka
Wheat,0.1,5,Restore Health,Fortify Health,Damage Stamina Regen,Lingering Damage Magicka
White Cap,0.3,0,Weakness to Frost,Fortify Heavy Armor,Restore Magicka,Ravage Magicka
Wisp Wrappings,0.1,2,Restore Stamina,Fortify Destruction,Fortify Carry Weight,Resist Magic""")

data_eso = StringIO("""Ingredient,PrimaryEffect,SecondaryEffect,TertiaryEffect,QuaternaryEffect
Beetle Scuttle,Breach,Increase Armor,Protection,Vitality
Blessed Thistle,Ravage Health,Restore Stamina,Increase Weapon Power,Speed
Blue Entoloma,Restore Health,Ravage Magicka,Cowardice,Invisible
Bugloss,Restore Health,Restore Magicka,Increase Spell Resist,Cowardice
Butterfly Wing,Restore Health,Uncertainty,Lingering Health,Vitality
Chaurus Egg,Ravage Magicka,Restore Stamina,Detection,Timidity
Clam Gall,Increase Spell Resist,Hindrance,Vulnerability,Defile
Columbine,Restore Health,Restore Magicka,Restore Stamina,Unstoppable
Corn Flower,Ravage Health,Restore Magicka,Increase Spell Power,Detection
Crimson Nirnroot,Restore Health,Spell Critical,Gradual Ravage Health,Timidity
Dragon Rheum,Restore Magicka,Enervation,Speed,Heroism
Dragon's Bile,Invisible,Vulnerability,Vitality,Heroism
Dragon's Blood,Restore Stamina,Lingering Health,Defile,Heroism
Dragonthorn,Restore Stamina,Fracture,Increase Weapon Power,Weapon Critical
Emetic Russula,Ravage Health,Ravage Magicka,Ravage Stamina,Entrapment
Fleshfly Larva,Ravage Stamina,Vulnerability,Gradual Ravage Health,Vitality
Imp Stool,Ravage Stamina,Increase Armor,Maim,Enervation
Lady's Smock,Restore Magicka,Breach,Increase Spell Power,Spell Critical
Luminous Russula,Restore Health,Ravage Stamina,Maim,Hindrance
Mountain Flower,Restore Health,Restore Stamina,Increase Armor,Maim
Mudcrab Chitin,Increase Spell Resist,Increase Armor,Protection,Defile
Namira's Rot,Spell Critical,Unstoppable,Invisible,Speed
Nightshade,Ravage Health,Protection,Gradual Ravage Health,Defile
Nirnroot,Ravage Health,Uncertainty,Enervation,Invisible
Powdered Mother of Pearl,Speed,Protection,Lingering Health,Vitality
Scrib Jelly,Ravage Magicka,Speed,Vulnerability,Lingering Health
Spider Egg,Invisible,Hindrance,Lingering Health,Defile
Stinkhorn,Ravage Health,Ravage Stamina,Fracture,Increase Weapon Power
Torchbug Thorax,Fracture,Enervation,Detection,Vitality
Vile Coagulant,Ravage Health,Restore Magicka,Protection,Timidity
Violet Coprinus,Ravage Health,Ravage Magicka,Breach,Increase Spell Power
Water Hyacinth,Restore Health,Spell Critical,Weapon Critical,Entrapment
White Cap,Ravage Magicka,Increase Spell Resist,Cowardice,Detection
Wormwood,Weapon Critical,Unstoppable,Detection,Hindrance""")

if game == "The Elder Scrolls V: Skyrim":
    df = pd.read_csv(data_skyrim, sep=",")

    search_str = st.text_input("Filter ingredients", "")

    values = st.slider("Select a value range", 0.0, 15.0, (0.0, 15.0))
    st.write("Value range", values)

    weights = st.slider("Select a weight range", 0.0, 0.5, (0.0, 0.5))
    st.write("Weight range", weights)

    df = df[df["Value"].between(values[0], values[1])]
    df = df[df["Weight"].between(weights[0], weights[1])]

else:
    df = pd.read_csv(data_eso, sep=",")
    search_str = st.text_input("Filter ingredients", "")

mask = df.apply(lambda row: row.astype(str).str.contains(search_str, case=False, na=False)).any(axis=1)
df = df[mask]

st.write(df)