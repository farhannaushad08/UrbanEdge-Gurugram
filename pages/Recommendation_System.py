import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ---- Page Config ----
st.set_page_config(page_title="UrbanEdge Recommender", layout="wide", page_icon="🏡")


# ---- Load Data ----
location_df = pd.read_csv('datasets/location_distance.csv', index_col=0)
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))


# ---- Function ----
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    return pd.DataFrame({
        '🏢 Property Name': top_properties,
        '📊 Similarity Score': [round(score, 3) for score in top_scores]
    })


# ---- Title ----
st.markdown("<h1 style='text-align:center; color:#0e6ba8;'>🏡 UrbanEdge Property Recommender</h1>",
            unsafe_allow_html=True)
st.markdown("### Discover similar or nearby flats based on features & location")

# ---- Section 1: Nearby Search ----
st.markdown("## 📍 Search Nearby Properties")
col1, col2 = st.columns([2, 1])

with col1:
    selected_location = st.selectbox(
        "Choose a Base Location (e.g., Sector 49, MG Road, DLF Phase 3)",
        sorted(location_df.columns.tolist())
    )

with col2:
    radius = st.number_input(
        "Enter Search Radius in Kilometers",
        min_value=0.0,
        step=0.5,
        value=2.0,
        help="Radius around the selected location to filter nearby properties."
    )

if st.button("🔍 Search Nearby"):
    try:
        result = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
        if result.empty:
            st.warning("No properties found within this radius.")
        else:
            st.success(f"{len(result)} properties found within {radius} KM.")
            st.dataframe(result.apply(lambda x: round(x / 1000, 2)))
    except KeyError:
        st.error("Invalid location selected.")

st.divider()

# ---- Section 2: Similar Apartments ----
st.markdown("## 🧠 Recommend Similar Apartments")

selected_apartment = st.selectbox("Select Apartment", sorted(location_df.index.tolist()))

if st.button("✨ Recommend Similar"):
    try:
        recommendation_df = recommend_properties_with_scores(selected_apartment)
        st.success(f"Showing top {len(recommendation_df)} similar apartments to '{selected_apartment}'.")
        st.dataframe(recommendation_df)
    except Exception as e:
        st.error(f"Error during recommendation: {e}")

# ---- Footer ----
st.markdown("---")

