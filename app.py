import streamlit as st
import random

st.set_page_config(page_title="Nexora Pro", layout="centered")

# Simple Styling
st.markdown("""
    <style>
    .main { background: #0a0a0a; color: white; }
    .stButton>button { width: 100%; background: #e74c3c; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    img { border-radius: 15px; border: 2px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Nexora HD Studio")

# User Input
p = st.text_area("Scene likhein:", placeholder="e.g. Scary woman, dark village...")

# Ratio selection
r = st.selectbox("Size:", ["9:16 (Shorts)", "16:9 (YouTube)"])
w, h = (720, 1280) if "9:16" in r else (1280, 720)

if st.button("Generate HD Image"):
    if p:
        with st.spinner("Wait... High Quality image ban rahi hai"):
            seed = random.randint(1, 999999)
            # Flux model use kiya hai taake chehray kharab na hon
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width={w}&height={h}&model=flux&seed={seed}&nologo=true"
            
            # Image Display
            st.image(url)
            
            # Simple Link (No raw code display)
            st.markdown(f"### [📥 SAVE IMAGE]({url})")
    else:
        st.error("Pehle prompt likhein!")
