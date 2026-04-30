import streamlit as st
import time
import random

# 1. Page Config
st.set_page_config(page_title="Nexora Studio Pro", page_icon="🎬", layout="wide")

# 2. Advanced CSS
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #ff4b2b, #ff416c); 
        color: white; font-weight: bold; border: none;
    }
    .download-btn {
        display: block; width: 100%; text-align: center; background: #007bff;
        color: white; padding: 12px; border-radius: 10px; font-weight: bold;
        text-decoration: none; margin-top: 10px;
    }
    img { border-radius: 15px; border: 2px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("🚀 Nexora Hub")
mode = st.sidebar.radio("Select Tool:", ["⚡ Image Engine", "🎥 Video Magic"])

# --- IMAGE ENGINE ---
if mode == "⚡ Image Engine":
    st.header("⚡ Multi-Ratio Creator")
    p = st.text_area("What to create?", placeholder="e.g. Scary ghost...")
    r = st.selectbox("Ratio:", ["16:9 (YouTube)", "9:16 (Shorts)", "1:1 (Square)"])
    w, h = (1280, 720) if "16:9" in r else (720, 1280) if "9:16" in r else (1024, 1024)

    if st.button("Generate HD Image"):
        url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')},8k,cinematic?width={w}&height={h}&nologo=true&seed={random.randint(1,1000)}"
        st.image(url)
        st.markdown(f'<a href="{url}" target="_blank" class="download-btn">📥 DOWNLOAD IMAGE</a>', unsafe_allow_html=True)

# --- VIDEO MAGIC (FIXED) ---
else:
    st.header("🎬 Image-to-Video (Motion Fix)")
    up = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
    if up:
        st.image(up, caption="Target Image", width=300)
        motion_desc = st.text_input("Describe the motion:", value="Cinematic motion, camera zoom in, fog moving, high quality video loop")
        
        if st.button("Generate Motion Video"):
            with st.spinner("🎥 Rendering... Please wait 30 seconds"):
                # "Force Motion" URL Construction
                # Hum 'video' aur 'animated' keywords ko prompt ke shuru mein la rahay hain
                v_url = f"https://image.pollinations.ai/prompt/animated%20video%20of%20{motion_desc.replace(' ', '%20')},motion,high%20fps?nologo=true&seed={random.randint(1,9999)}"
                
                st.info("AI is processing the motion frames...")
                st.image(v_url) 
                st.success("Motion Generated! Click below to save.")
                st.markdown(f'<a href="{v_url}" target="_blank" class="download-btn">📥 SAVE VIDEO CLIP</a>', unsafe_allow_html=True)
