import streamlit as st
import random

# 1. Simple Interface
st.set_page_config(page_title="Nexora Studio", layout="centered")

st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { width: 100%; background: #ff4b2b; color: white; font-weight: bold; border-radius: 10px; }
    img { border-radius: 15px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Nexora Simple Studio")

# 2. Input
p = st.text_area("Yahan apni baat likhein:", placeholder="e.g. Scary woman...")

# 3. Ratio Selector (Simple)
r = st.selectbox("Size select karein:", ["9:16 (Shorts)", "16:9 (YouTube)", "1:1 (Square)"])

if "9:16" in r: w, h = 720, 1280
elif "16:9" in r: w, h = 1280, 720
else: w, h = 1024, 1024

# 4. Generate
if st.button("Generate Image"):
    if p:
        seed = random.randint(1, 100000)
        # Bilkul purana stable link
        url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed={seed}"
        
        st.image(url)
        
        # Simple Download Button (Fixed)
        st.write(f"**[SAVE IMAGE]({url})**")
    else:
        st.error("Pehle kuch likhein!")
