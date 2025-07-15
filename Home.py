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

# ---- Enhanced Feature Section (Cards with Clickable Links) ----
st.markdown("## 🚀 Features")

# Custom CSS for card styling
st.markdown("""
<style>
.feature-card {
    background-color: #f9f9f9;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: 0.3s;
    text-align: center;
    border: 2px solid transparent;
}
.feature-card:hover {
    border: 2px solid #0e6ba8;
    background-color: #eef6fa;
    cursor: pointer;
}
a.card-link {
    color: inherit;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a class="card-link" href="/Analytics" target="_self">
        <div class="feature-card">
            <h4>📈 Smart Analytics</h4>
            <p>Explore price heatmaps, BHK comparisons, and price distributions across Gurugram.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a class="card-link" href="/Predictor" target="_self">
        <div class="feature-card">
            <h4>🧠 Price Prediction</h4>
            <p>Enter your property details and get accurate price estimates powered by AI.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a class="card-link" href="/Recommendation_System" target="_self">
        <div class="feature-card">
            <h4>🏡 Personalized Recommendation</h4>
            <p>Discover similar or nearby properties based on features and location proximity.</p>
        </div>
    </a>
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
