import streamlit as st
import random

# 1. Page Config (Mobile Optimization)
st.set_page_config(page_title="Nexora Studio Pro", page_icon="🎬", layout="centered")

# 2. Advanced Premium CSS
st.markdown("""
    <style>
    .main { background: #05070a; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #1a252f, #34495e); 
        color: white; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    
    img { 
        border-radius: 20px; border: 3px solid #1c2833; 
        width: 100%; height: auto !important; object-fit: contain;
    }
    .download-btn {
        display: block; width: 100%; text-align: center; background: #28a745;
        color: white; padding: 15px; border-radius: 10px; font-weight: bold;
        text-decoration: none; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Nexora Nightmare Pro")

# ---TOOL 1: ULTIMATE QUALITY IMAGE GEN---
st.header("⚡ Text-to-HD Image Creator")
p = st.text_area("Describe scene:", placeholder="e.g. Scary ghost in dark house...", key="p1")

# Fixed Ratios mapping for HQ
r = st.selectbox("Select Size:", ["9:16 (TikTok/Shorts)", "16:9 (YouTube Video)", "1:1 (Insta)"])
w, h = (720, 1280) if "9:16" in r else (1280, 720) if "16:9" in r else (1024, 1024)

# FIX: Added High-End Quality Tags specifically for horror
q_tags = ", photorealistic, hyper detailed, sharp focus, 8k resolution, cinematic lighting, masterpiece, nightmare engine"

if st.button("Generate HD Art"):
    if p:
        with st.spinner("💎 Nexora is processing masterpiece..."):
            seed = random.randint(1, 1000000)
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}{q_tags.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed={seed}&model=flux"
            
            st.image(url, caption=f"Ratio: {r}", use_column_width=True)
            st.markdown(f'<a href="{url}" target="_blank" class="download-btn">📥 DOWNLOAD HD IMAGE</a>', unsafe_allow_html=True)

# ---TOOL 2: PRO MOTION DESCRIPTION (Luma Ready)---
st.header("🎬 Luma AI Video Prompt Tool")
st.info("Download the image above, then use this motion description on Luma Labs for perfect video.")
m_desc = st.text_input("Motion to add (e.g. Scary woman slowly turns head, fog moving):")
st.code(m_desc + ", dynamic motion, cinematic slow motion, video loop")
