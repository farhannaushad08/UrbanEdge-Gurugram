import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# ---- Page Config ----
st.set_page_config(page_title="UrbanEdge Analytics", layout="wide", page_icon="📊")


# ---- Title ----
st.markdown("<h1 style='text-align:center; color:#0e6ba8;'>📊 UrbanEdge Gurugram: Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("### Get deep insights into Gurugram's housing market with visual storytelling, AI & interactivity.")

# ---- Load Data ----
new_df = pd.read_csv("datasets/data_viz1.csv")
new_df['price'] = pd.to_numeric(new_df['price'], errors='coerce')  # Already in Cr
new_df['price_per_sqft'] = pd.to_numeric(new_df['price_per_sqft'], errors='coerce')
feature_text = pickle.load(open("datasets/feature_text.pkl", "rb"))

# ---- Summary Stats ----
st.markdown("## 📈 Market Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Listings", len(new_df))
with col2:
    st.metric("Avg Price (Cr)", round(new_df["price"].mean(), 2))  # ✅ FIXED: no divide by 1e7
with col3:
    st.metric("Avg Price/Sqft", round(new_df["price_per_sqft"].mean(), 0))
with col4:
    st.metric("Max Area (sqft)", int(new_df["built_up_area"].max()))

st.divider()

# ---- Geomap ----
st.markdown("## 🗺️ Sector-wise Price per Sqft (GeoView)")
group_df = new_df.groupby("sector")[["price", "price_per_sqft", "built_up_area", "latitude", "longitude"]].mean().reset_index()

fig_map = px.scatter_mapbox(
    group_df, lat="latitude", lon="longitude", color="price_per_sqft", size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
    mapbox_style="open-street-map", hover_name="sector", height=600
)
st.plotly_chart(fig_map, use_container_width=True)

# ---- Word Cloud ----
st.markdown("## ☁️ Top Features Word Cloud")
wordcloud = WordCloud(width=800, height=800, background_color="black", stopwords=set(['s']), min_font_size=10).generate(feature_text)
fig_wc, ax_wc = plt.subplots(figsize=(8, 8))
ax_wc.imshow(wordcloud, interpolation="bilinear")
ax_wc.axis("off")
st.pyplot(fig_wc)

# ---- Area vs Price ----
st.markdown("## 📏 Area vs Price")
property_type = st.selectbox("Choose Property Type", ['flat', 'house'])
filtered_df = new_df[new_df['property_type'] == property_type]
fig_area_price = px.scatter(
    filtered_df, x="built_up_area", y="price", color="bedRoom",
    title=f"Area vs Price: {property_type.title()}s", size_max=60
)
st.plotly_chart(fig_area_price, use_container_width=True)

# ---- BHK Pie Chart ----
st.markdown("## 🧱 BHK Distribution by Sector")
sector_options = ['Overall'] + sorted(new_df['sector'].dropna().unique().tolist())
selected_sector = st.selectbox("Select Sector", sector_options)

if selected_sector == 'Overall':
    fig_bhk = px.pie(new_df, names="bedRoom", title="BHK Distribution (Overall)")
else:
    sector_df = new_df[new_df['sector'] == selected_sector]
    fig_bhk = px.pie(sector_df, names="bedRoom", title=f"BHK Distribution – {selected_sector}")
st.plotly_chart(fig_bhk, use_container_width=True)

# ---- Box Plot BHK vs Price ----
st.markdown("## 📦 BHK-wise Price Comparison")
fig_box = px.box(new_df[new_df["bedRoom"] <= 4], x="bedRoom", y="price", title="Price Distribution by BHK (up to 4 BHK)")
st.plotly_chart(fig_box, use_container_width=True)

# ---- KDE Plot ----
st.markdown("## 📉 Price Distribution by Property Type")
fig_kde = plt.figure(figsize=(10, 5))
sns.kdeplot(new_df[new_df["property_type"] == "house"]["price"], label="House", fill=True)
sns.kdeplot(new_df[new_df["property_type"] == "flat"]["price"], label="Flat", fill=True)
plt.xlabel("Price (Cr)")
plt.ylabel("Density")
plt.title("Price Distribution - House vs Flat")
plt.legend()
st.pyplot(fig_kde)

