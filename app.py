import streamlit as st
import random

# 1. Page Config
st.set_page_config(page_title="Nexora Studio", page_icon="🎨", layout="centered")

# 2. Simple & Clean CSS
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #ff4b2b, #ff416c); 
        color: white; font-weight: bold; border: none;
    }
    img { border-radius: 15px; border: 2px solid #30363d; width: 100%; }
    .download-btn {
        display: block; width: 100%; text-align: center; background: #28a745;
        color: white; padding: 12px; border-radius: 10px; font-weight: bold;
        text-decoration: none; margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Nexora AI Studio")

# 3. Input Area
p = st.text_area("What to create?", placeholder="e.g. Scary woman in haunted house...", height=100)

# 4. Ratio Selection (Buttons Style)
r_choice = st.selectbox("Select Size / Ratio:", ["9:16 (Shorts/TikTok)", "16:9 (YouTube Video)", "1:1 (Square)"])

# Pixel Logic
w, h = (720, 1280) if "9:16" in r_choice else (1280, 720) if "16:9" in r_choice else (1024, 1024)

# 5. Generate Button
if st.button("Generate Masterpiece"):
    if p:
        with st.spinner("💎 Processing your image..."):
            seed = random.randint(1, 1000000)
            # Simple Link (Stable Quality)
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed={seed}"
            
            # Show Image
            st.image(url, caption=f"Ratio: {r_choice}")
            
            # 6. Beautiful Download Button (No raw code)
            st.markdown(f'<a href="{url}" target="_blank" class="download-btn">📥 DOWNLOAD HD IMAGE</a>', unsafe_allow_html=True)
    else:
        st.warning("Please describe your scene first!")
