import streamlit as st
import pandas as pd
import numpy as np

## --- UI Configuration ---
st.set_page_config(page_title="Mushroom Poisonous Prediction", layout="wide")
st.title("🍄 Mushroom Classifier Input")
st.write("Select the characteristics of the mushroom to check if it's edible or poisonous.")

## --- Input Options Dictionary ---
# These match the 'Attribute Information' from your notebook
options = {
    'cap-shape': {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed', 's': 'sunken'},
    'cap-surface': {'f': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth'},
    'cap-color': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'bruises': {'t': 'bruises', 'f': 'no'},
    'odor': {'a': 'almond', 'l': 'anise', 'c': 'creosote', 'y': 'fishy', 'f': 'foul', 'm': 'musty', 'n': 'none', 'p': 'pungent', 's': 'spicy'},
    'gill-attachment': {'a': 'attached', 'd': 'descending', 'f': 'free', 'n': 'notched'},
    'gill-spacing': {'c': 'close', 'w': 'crowded', 'd': 'distant'},
    'gill-size': {'b': 'broad', 'n': 'narrow'},
    'gill-color': {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'g': 'gray', 'r': 'green', 'o': 'orange', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'stalk-shape': {'e': 'enlarging', 't': 'tapering'},
    'stalk-root': {'b': 'bulbous', 'c': 'club', 'u': 'cup', 'e': 'equal', 'z': 'rhizomorphs', 'r': 'rooted', '?': 'missing'},
    'stalk-surface-above-ring': {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'},
    'stalk-surface-below-ring': {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'},
    'stalk-color-above-ring': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'stalk-color-below-ring': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'},
    'veil-type': {'p': 'partial', 'u': 'universal'},
    'veil-color': {'n': 'brown', 'o': 'orange', 'w': 'white', 'y': 'yellow'},
    'ring-number': {'n': 'none', 'o': 'one', 't': 'two'},
    'ring-type': {'c': 'cobwebby', 'e': 'evanescent', 'f': 'flaring', 'l': 'large', 'n': 'none', 'p': 'pendant', 's': 'sheathing', 'z': 'zone'},
    'spore-print-color': {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'r': 'green', 'o': 'orange', 'u': 'purple', 'w': 'white', 'y': 'yellow'},
    'population': {'a': 'abundant', 'c': 'clustered', 'n': 'numerous', 's': 'scattered', 'v': 'several', 'y': 'solitary'},
    'habitat': {'g': 'grasses', 'l': 'leaves', 'm': 'meadows', 'p': 'paths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}
}

## --- Create Input Form ---
with st.form("mushroom_form"):
    col1, col2, col3 = st.columns(3)
    
    user_inputs = {}
    
    # Distribute inputs across columns for better UI
    for i, (key, val_dict) in enumerate(options.items()):
        current_col = [col1, col2, col3][i % 3]
        # Use the descriptive name for the label, but store the short key code
        display_labels = list(val_dict.values())
        selected_display = current_col.selectbox(f"Select {key}", display_labels)
        
        # Reverse lookup: get 'b' from 'bell'
        short_code = [k for k, v in val_dict.items() if v == selected_display][0]
        user_inputs[key] = [short_code]

    submitted = st.form_submit_button("Prepare Data for Prediction")

if submitted:
    # 1. Create the new_data DataFrame
    new_data = pd.DataFrame(user_inputs)
    
    st.subheader("Original Data (new_data)")
    st.write(new_data)

    # 2. Logic to align with training columns (X.columns)
    # Note: In a real app, you should load X.columns from a saved file
    # For this example, we show how it would look:
    st.info("The data is now stored in 'new_data' and ready for One-Hot Encoding.")
    
    # To use this with your model:
    # new_data_processed = pd.get_dummies(new_data)
    # new_data_aligned = new_data_processed.reindex(columns=X_columns, fill_value=False)
