import streamlit as st
import pickle
import pandas as pd
import numpy as np
import textwrap
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Next Arc",
    layout="wide"
)

st.title("🎬 Next Arc")
st.caption("Find your next anime based on what you already love.")

# ----------------------------
# Load data
# ----------------------------
@st.cache_data
def load_df():
    df = pd.read_csv("final_anime.csv")
    df.reset_index(drop=True, inplace=True)
    return df

@st.cache_resource
def load_vectors():
    with open("vectors.pkl", "rb") as f:
        return pickle.load(f)

df = load_df()
vectors = load_vectors()

# Safety check
assert len(df) == vectors.shape[0], "Dataset and vectors are misaligned!"

name_to_index = dict(zip(df["Name"].values, df.index.values))

# ----------------------------
# Recommendation logic
# ----------------------------
def recommend(anime_name, top_k=5):
    idx = name_to_index[anime_name]

    # Compute similarity only for one item
    sims = cosine_similarity(
        vectors[idx].reshape(1, -1),
        vectors
    ).flatten()

    # Get top-k excluding itself
    top_idx = np.argsort(sims)[-top_k-1:-1][::-1]

    return df.iloc[top_idx][["Name", "Image URL"]]

# ----------------------------
# UI helpers
# ----------------------------
def clamp_title(title, max_chars=40):
    return textwrap.shorten(title, width=max_chars, placeholder="…")

# ----------------------------
# UI
# ----------------------------
selected_anime = st.selectbox(
    "Select an anime you like:",
    df["Name"].values
)

if st.button("Recommend"):
    with st.spinner("Summoning your next arc..."):
        recs = recommend(selected_anime, top_k=5)

    st.subheader("✨ Recommended for you")

    cols = st.columns(5)

    for col, (_, row) in zip(cols, recs.iterrows()):
        with col:
            st.image(row["Image URL"], use_container_width=True)
            st.write(clamp_title(row["Name"]))
