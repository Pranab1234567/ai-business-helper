
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="AI Business Helper", page_icon="💼", layout="wide")

# ---------------------------------------
# CUSTOM CSS FIXED (Guaranteed to show)
# ---------------------------------------
st.markdown("""
<style>

html, body {
    margin: 0;
    padding: 0;
}

section[data-testid="stSidebar"] {
    background-color: white;
}

/* NAVBAR */
#custom-navbar {
    background-color: #ffffff;
    padding: 15px 25px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.12);
}
.nav-item {
    display: inline-block;
    margin-right: 28px;
    font-size: 17px;
    font-weight: 600;
    color: #333;
}
.nav-item:hover {
    color: #ff4b4b;
    cursor: pointer;
}

/* CARD BLOCK */
.block {
    background: #fff;
    border-radius: 18px;
    padding: 25px;
    margin-top: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    animation: fadeIn 0.8s ease-in-out;
}

/* FADE ANIMATION */
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(20px);}
    100% {opacity: 1; transform: translateY(0);}
}

/* FOOTER */
.footer {
    text-align: center;
    font-size: 15px;
    padding: 10px;
    color: #666;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ----------------------
# NAVBAR (Now Works)
# ----------------------
st.markdown("""
<div id="custom-navbar">
    <span class="nav-item">Home</span>
    <span class="nav-item">About</span>
    <span class="nav-item">Contact</span>
    <span class="nav-item">Pricing</span>
    <span class="nav-item">Login</span>
</div>
""", unsafe_allow_html=True)


# TITLE
st.title("💼 AI Business Helper — For Local Shops")
st.write("A simple AI toolkit: Sentiment analysis, pricing, forecasting and suggestions.")

# =====================================================================
# 1) SENTIMENT ANALYSIS
# =====================================================================

from transformers import pipeline

st.header("🙍 Customer Review Sentiment")

# Load HuggingFace sentiment model
sentiment_analyzer = pipeline("sentiment-analysis")

review = st.text_area("Paste a customer review here:")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        result = sentiment_analyzer(review)[0]
        label = result["label"]
        score = result["score"]

        if label == "NEGATIVE":
            st.error(f"Sentiment: {label} 😡 ({score:.2f})")
        elif label == "POSITIVE":
            st.success(f"Sentiment: {label} 😊 ({score:.2f})")
        else:
            st.info(f"Sentiment: {label} 😐 ({score:.2f})")







# =====================================================================
# 2) PRICE SUGGESTION
# =====================================================================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.header("💰 Suggested Price for a Product")

c1, c2, c3 = st.columns(3)

brand = c1.number_input("Brand Quality (1-5)", 1, 5, 3)
popularity = c2.slider("Popularity (1-100)", 1, 100, 50)
age = c3.number_input("Age (months)", 1, 60, 6)

if st.button("Suggest Price"):
    price = brand * 100 + popularity * 2 - age
    st.info(f"Suggested Price: ₹{price:.2f}")

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 3) SALES FORECAST
# =====================================================================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.header("📈 Sales Forecast (next 6 months)")

if st.button("Forecast Sales"):
    months = []
    sales = []
    base = 200
    now = datetime.now()

    for i in range(6):
        months.append(now + timedelta(days=30*(i+1)))
        sales.append(base + i*4)

    df = pd.DataFrame({"month": months, "predicted_sales": sales})
    st.table(df)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 4) FAQ CHATBOT
# =====================================================================
st.markdown("<div class='block'>", unsafe_allow_html=True)

st.header("🤖 Quick FAQ Helper")

question = st.text_input("Ask a business-related question:")

if st.button("Ask"):
    st.write("To increase sales: Improve customer service, offer combos, and promote online.")

st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
Made with ❤️ in Odisha by <b>Pranab</b>
</div>
""", unsafe_allow_html=True)
