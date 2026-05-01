import streamlit as st
import random

# 1. Basic Page Setup
st.set_page_config(page_title="Nexora Studio", layout="centered")

# 2. Simple UI
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: #ff4b2b; color: white; font-weight: bold; border: none;
    }
    img { border-radius: 15px; width: 100%; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Nexora Simple Studio")

# 3. Simple Input
p = st.text_area("Yahan apni baat likhein:", placeholder="e.g. Scary woman in dark house...")

# 4. Generate (Fixed Single Size: 1024x1024)
if st.button("Generate Image"):
    if p:
        with st.spinner("Bann rahi hai..."):
            seed = random.randint(1, 999999)
            # Flux model for high quality like your butterfly/astronaut pics
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width=1024&height=1024&nologo=true&seed={seed}&model=flux"
            
            # Show Image
            st.image(url)
            
            # Simple Text Link
            st.markdown(f"### [📥 SAVE IMAGE]({url})")
    else:
        st.error("Pehle kuch likhein!")

