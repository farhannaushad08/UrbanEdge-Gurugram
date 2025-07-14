import streamlit as st
from PIL import Image

# ---- Page Config (MUST be first) ----
st.set_page_config(
    page_title="UrbanEdge Gurugram",
    page_icon="🏙️",
    layout="wide"
)

# ---- Header with Logo and Name ----
st.markdown("""
    <h1 style='text-align: center; font-size: 48px; color: #0e6ba8;'>🏙️ UrbanEdge Gurugram</h1>
    <p style='text-align: center; font-size: 20px; color: #444;'>Smart Housing Insights for Corporate India</p>
    <hr>
""", unsafe_allow_html=True)


# ---- Hero Section ----
col1, col2 = st.columns([1, 1])
with col1:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c", use_container_width=True)
with col2:
    st.markdown("""
    ## 📊 About UrbanEdge
    UrbanEdge Gurugram is your intelligent home discovery dashboard built for:

    - 🧑‍💼 Corporate buyers and renters in Gurugram  
    - 🧠 Price prediction using machine learning  
    - 📍 Sector-wise analytics and property recommendations  

    Powered by **Streamlit, Scikit-learn, Pandas, and Plotly.**
    """)

# ---- Features ----
st.markdown("## 🚀 Features")
st.markdown("""
<style>
.feature-box {
    background-color: #f2f2f2;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class='feature-box'>
        <h3>📈 Smart Analytics</h3>
        <p>Explore price heatmaps, BHK comparisons, and price distributions across Gurugram.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box'>
        <h3>🧠 Price Prediction</h3>
        <p>Enter your property details and get accurate price estimates powered by AI.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='feature-box'>
        <h3>🏡 Personalized Recommendations</h3>
        <p>Discover similar or nearby properties based on features and location proximity.</p>
    </div>
    """, unsafe_allow_html=True)

# ---- Tech Stack ----
st.markdown("## 🛠 Tech Stack")
st.markdown("""
- **Frontend:** Streamlit (with Plotly, Seaborn, WordCloud)  
- **Modeling:** Scikit-learn (Random Forest)  
- **Processing:** Pandas, NumPy  
- **Recommendation Engine:** Cosine Similarity + Distance Matrix
""")

# ---- About Developer ----
st.markdown("## 👨‍💻 About the Developer")
st.markdown("""
- **Name:** Md. Farhan Naushad  
- **Role:** B.Tech Student | Data & AI Enthusiast  
- **GitHub:** [github.com/farhannaushad08](https://github.com/farhannaushad08)  
- **LinkedIn:** [linkedin.com/in/md-farhan-naushad-b02456253](https://www.linkedin.com/in/md-farhan-naushad-b02456253/)  
- **Email:** [farhannaushad08@gmail.com](mailto:farhannaushad08@gmail.com)
""")

# ---- Contact ----
st.markdown("## 📬 Contact & Feedback")
st.markdown("""
Got suggestions, feedback, or want to collaborate?  
Reach out via **email** or **LinkedIn** — let’s make smart real estate smarter! 🧠
""")

# ---- Footer ----
st.markdown("""---""")
st.markdown("<p style='text-align: center;'>© 2025 UrbanEdge Gurugram by Md. Farhan Naushad</p>", unsafe_allow_html=True)

# ---- Sidebar Reminder ----
st.sidebar.success("Select a page to begin ➜")
