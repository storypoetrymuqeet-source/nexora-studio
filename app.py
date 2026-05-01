import streamlit as st
import random

# 1. Page Config
st.set_page_config(page_title="Nexora Studio", layout="centered")

# 2. Simple Style
st.markdown("""
    <style>
    .main { background: #0a0c10; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; background: #ff4b2b; color: white; font-weight: bold; }
    img { border-radius: 15px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Nexora HD Studio")

# 3. Inputs
p = st.text_area("Yahan apni kahani likhein:", placeholder="e.g. Scary woman in dark house...")

# Ratio selection
r = st.selectbox("Size Select Karein:", ["9:16 (Shorts)", "16:9 (YouTube)"])
if "9:16" in r: w, h = 720, 1280
else: w, h = 1024, 576  # 16:9 fix for mobile stability

# 4. Generate
if st.button("🚀 Create Masterpiece"):
    if p:
        with st.spinner("Wait..."):
            seed = random.randint(1, 999999)
            # Flux model use kar rahe hain taake faces kharab na hon
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed={seed}&model=flux"
            
            st.image(url)
            st.markdown(f"### [📥 SAVE IMAGE]({url})")
    else:
        st.error("Pehle kuch likhein!")
