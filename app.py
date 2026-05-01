import streamlit as st
import random
import urllib.parse

# 1. Page Config
st.set_page_config(page_title="Nexora Studio", layout="centered")

st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3em; 
        background: #ff4b2b; color: white; font-weight: bold;
    }
    img { border-radius: 15px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Nexora Stable Studio")

# 2. Input Area
p = st.text_area("Yahan scene likhein:", placeholder="e.g. Scary woman in dark room...", height=100)

# 3. Generate Logic
if st.button("🚀 Generate Now"):
    if p:
        with st.spinner("Wait... Tasveer bann rahi hai..."):
            # Clean prompt to avoid link breaking
            safe_prompt = urllib.parse.quote(p)
            seed = random.randint(1, 999999)
            
            # Stable URL without extra complicated tags
            url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&nologo=true&seed={seed}&model=flux"
            
            # Pehle Direct Link dikhayega (Sab se zaroori)
            st.success("✅ Image Link Tayyar Hai!")
            st.markdown(f"### [👉 CLICK HERE TO OPEN IMAGE]({url})")
            
            # Phir Image dikhane ki koshish karega
            st.image(url, caption="Agar yahan nazar na aaye toh upar wale link par click karein")
    else:
        st.warning("Pehle kuch likhein!")
