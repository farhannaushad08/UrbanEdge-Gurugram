# 🏙️ UrbanEdge – Gurugram

> An intelligent real estate platform built with Machine Learning and Streamlit that analyzes, predicts, and recommends properties in Gurugram.

---

## 🔍 About the Project

**UrbanEdge – Gurugram** is a complete real estate data solution designed to help users explore, understand, and predict property prices in Gurugram. From detailed visual analytics to machine learning predictions and a recommendation engine — this app brings together data science and real estate in an intuitive interface.

It’s built end-to-end: starting from raw data, extensive preprocessing, model development using `RandomForestRegressor` (with pipelines and encoders), to deployment-ready Streamlit apps.

---

## 🚀 Features at a Glance

| Feature | Description |
|--------|-------------|
| 📊 **Analytics Dashboard** | Interactive visualizations for sector-wise prices, BHK trends, area-price relationships, and more |
| 💰 **Price Predictor** | ML-based price prediction with rent estimation based on features like furnishing, BHK, sector, etc. |
| 🧠 **Property Recommender** | Suggests similar or nearby properties using cosine similarity matrices |
| ☁️ **Word Cloud** | Shows most frequent property features from listings |
| 🗺️ **Geo Map View** | Sector-wise price distribution on an interactive Mapbox map |
| 🔗 **Live Links** | Directs users to 99acres, MagicBricks, and more based on input |

---

## 🧠 Machine Learning Workflow

- ✔️ Data cleaning (duplicates, outliers)
- 🔍 Missing value imputation
- 🏗️ Feature selection and engineering
- 🧱 OneHot & Ordinal Encoding with `ColumnTransformer`
- 🔄 Model built using a `Pipeline` (RandomForestRegressor)
- 💾 Trained model serialized as `pipeline.pkl`

---

## 🗂️ Project Structure
UrbanEdge-Gurugram/
├── Home.py # Streamlit landing page
├── pages/
│ ├── Analytics.py # Data visualizations and insights
│ ├── Predictor.py # ML model and rent estimator
│ └── Recommendation_System.py# Similar/nearby property recommender
├── datasets/ # All processed data and matrices
├── df.pkl # Final cleaned dataset
├── pipeline.pkl # Trained RandomForest pipeline
├── requirements.txt # Python dependencies
├── README.md # Project documentation (this file)



