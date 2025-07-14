import streamlit as st
import pickle
import pandas as pd
import numpy as np
from urllib.parse import quote_plus

# ---- Page Config ----
st.set_page_config(page_title="UrbanEdge Price Predictor", page_icon="💰", layout="wide")

# ---- Load Data & Model ----
with open('df.pkl', 'rb') as f:
    df = pickle.load(f)

with open('pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# ---- Page Header ----
st.markdown("<h1 style='text-align:center; color:#0e6ba8;'>💰 UrbanEdge Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("### Predict property prices in Gurugram based on custom preferences.")

# ---- Input Form ----
st.markdown("## 🧾 Enter Property Details")

col1, col2 = st.columns(2)

with col1:
    property_type = st.selectbox('🏘 Property Type', ['flat', 'house'])
    sector = st.selectbox('📍 Sector', sorted(df['sector'].unique().tolist()))
    bedrooms = float(st.selectbox('🛏 Bedrooms', sorted(df['bedRoom'].unique().tolist())))
    bathroom = float(st.selectbox('🚿 Bathrooms', sorted(df['bathroom'].unique().tolist())))
    balcony = st.selectbox('🌤️ Balconies', sorted(df['balcony'].unique().tolist()))
    property_age = st.selectbox('🏗 Property Age', sorted(df['agePossession'].unique().tolist()))

with col2:
    built_up_area = float(st.number_input('📐 Built Up Area (sq ft)', min_value=100.0))
    servant_room = st.selectbox('👨‍🍳 Servant Room', ['No', 'Yes'])
    store_room = st.selectbox('📦 Store Room', ['No', 'Yes'])
    furnishing_type = st.selectbox('🪑 Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
    luxury_category = st.selectbox('💎 Luxury Category', sorted(df['luxury_category'].unique().tolist()))
    floor_category = st.selectbox('🏢 Floor Category', sorted(df['floor_category'].unique().tolist()))

# ---- Prediction ----
if st.button("🔍 Predict Price & Rent"):

    # Encode yes/no fields
    servant_room_val = 1 if servant_room == 'Yes' else 0
    store_room_val = 1 if store_room == 'Yes' else 0

    # Create input dataframe
    input_data = pd.DataFrame([[property_type, sector, bedrooms, bathroom, balcony,
                                property_age, built_up_area, servant_room_val, store_room_val,
                                furnishing_type, luxury_category, floor_category]],
                              columns=['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
                                       'agePossession', 'built_up_area', 'servant room', 'store room',
                                       'furnishing_type', 'luxury_category', 'floor_category'])

    st.markdown("### 🧾 Your Input Summary")
    st.dataframe(input_data)

    # ----------- Price Prediction -----------
    base_price = np.expm1(pipeline.predict(input_data)[0])
    low = round(base_price * 0.95, 2)
    high = round(base_price * 1.05, 2)

    st.success(f"💸 **Estimated Price Range:** ₹ {low} Cr – ₹ {high} Cr")

    # ----------- Rent Estimation -----------
    base_rate_per_sqft = 30

    if luxury_category == 'ultra luxury':
        base_rate_per_sqft += 10
    elif luxury_category == 'luxury':
        base_rate_per_sqft += 6
    elif luxury_category == 'semi luxury':
        base_rate_per_sqft += 3

    if furnishing_type == 'furnished':
        base_rate_per_sqft += 5
    elif furnishing_type == 'semi furnished':
        base_rate_per_sqft += 2

    if floor_category == 'highrise':
        base_rate_per_sqft += 2
    elif floor_category == 'midrise':
        base_rate_per_sqft += 1

    if servant_room == 'Yes':
        base_rate_per_sqft += 1
    if store_room == 'Yes':
        base_rate_per_sqft += 1

    estimated_rent = round(base_rate_per_sqft * built_up_area)
    rent_low = round(estimated_rent * 0.95)
    rent_high = round(estimated_rent * 1.05)

    st.info(f"🏠 **Estimated Monthly Rent:** ₹ {rent_low:,} – ₹ {rent_high:,}")

    # ----------- Real Estate Platform Links with Logos -----------
    # ----------- Real Estate Platform Links (Bullet Point Style) -----------
    st.markdown("### 🌐 View Listings on Real Estate Platforms")

    bhk = int(bedrooms)
    clean_sector = sector.strip().lower().replace(" ", "-")
    city = "gurgaon"
    search_query = f"{bhk} BHK flats in {sector} {city}"

    platforms = [
        {
            "name": "99acres",
            "url": f"https://www.99acres.com/{bhk}-bhk-flats-in-{clean_sector}-{city}-ffid"
        },
        {
            "name": "MagicBricks (via Google)",
            "url": f"https://www.google.com/search?q={quote_plus(search_query + ' site:magicbricks.com')}"
        },
        {
            "name": "Housing.com (via Google)",
            "url": f"https://www.google.com/search?q={quote_plus(search_query + ' site:housing.com')}"
        },
        {
            "name": "NoBroker (via Google)",
            "url": f"https://www.google.com/search?q={quote_plus(search_query + ' site:nobroker.in')}"
        },
        {
            "name": "Makaan (via Google)",
            "url": f"https://www.google.com/search?q={quote_plus(search_query + ' site:makaan.com')}"
        },
    ]

    for p in platforms:
        st.markdown(f"- [{p['name']}]({p['url']})", unsafe_allow_html=True)

# ---- Footer ----
st.markdown("---")
