import streamlit as st
import random

# 1. Page Setup
st.set_page_config(page_title="Nexora Stable Studio", page_icon="🎨", layout="centered")

# 2. Clean UI Style
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #007bff, #00d4ff); 
        color: white; font-weight: bold; border: none;
    }
    img { border-radius: 15px; border: 2px solid #30363d; margin-top: 10px; width: 100%; }
    .dl-btn {
        display: block; width: 100%; text-align: center; background: #28a745;
        color: white; padding: 12px; border-radius: 10px; font-weight: bold;
        text-decoration: none; margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Nexora Stable Studio")

# 3. Inputs
p = st.text_area("What to create?", placeholder="Describe your horror scene here...")

col1, col2 = st.columns(2)
with col1:
    r_choice = st.selectbox("Select Ratio:", ["9:16 (Shorts)", "16:9 (YouTube)", "1:1 (Square)"])
    w, h = (720, 1280) if "9:16" in r_choice else (1280, 720) if "16:9" in r_choice else (1024, 1024)

with col2:
    s_choice = st.selectbox("Select Style:", ["Ultra-Realistic", "Cinematic Horror", "3D Animation"])
    # Quality tags for high-end results
    s_tags = ", high quality, 8k, detailed face, sharp focus"

# Generate Action
if st.button("🚀 Generate Masterpiece"):
    if p:
        with st.spinner("💎 Crafting your image..."):
            seed = random.randint(1, 999999)
            # Simplified URL to prevent loading errors
            clean_p = p.replace(' ', '%20')
            clean_s = s_tags.replace(' ', '%20')
            url = f"https://image.pollinations.ai/prompt/{clean_p}{clean_s}?width={w}&height={h}&nologo=true&seed={seed}"
            
            # Display result
            st.image(url, caption=f"Format: {r_choice}")
            
            # 4. FIXED Download Button (No raw code)
            st.markdown(f'<a href="{url}" target="_blank" class="dl-btn">📥 DOWNLOAD HD IMAGE</a>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a description first!")
