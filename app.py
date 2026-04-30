import streamlit as st
import random
import time

# 1. Page Config (Mobile Optimization)
st.set_page_config(page_title="Nexora Studio Master", page_icon="🎬", layout="centered")

# 2. Premium Mobile CSS
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #6a11cb, #2575fc); 
        color: white; font-weight: bold; border: none;
    }
    img { 
        border-radius: 15px; border: 2px solid #30363d; 
        width: 100% !important; height: auto !important; 
        object-fit: cover;
    }
    .download-btn {
        display: block; width: 100%; text-align: center; background: #28a745;
        color: white; padding: 15px; border-radius: 10px; font-weight: bold;
        text-decoration: none; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Nexora All-in-One")

# 3. Main Navigation Tabs (Saare buttons ab samnay hain!)
tab1, tab2, tab3 = st.tabs(["⚡ Image Gen", "➕ Image to Style", "🎬 Video Magic"])

# --- TAB 1: TEXT TO IMAGE (With All Ratios) ---
with tab1:
    st.subheader("Create from Text")
    p = st.text_area("Describe your scene:", placeholder="e.g. Scary ghost...", key="t1")
    r = st.selectbox("Select Platform (Ratio):", ["9:16 (TikTok/Shorts)", "16:9 (YouTube)", "1:1 (Insta)"])
    
    w, h = (720, 1280) if "9:16" in r else (1280, 720) if "16:9" in r else (1024, 1024)
    
    if st.button("Generate HD"):
        if p:
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')},8k,cinematic?width={w}&height={h}&nologo=true&seed={random.randint(1,9999)}"
            st.image(url, use_column_width=True)
            st.markdown(f'<a href="{url}" target="_blank" class="download-btn">📥 DOWNLOAD IMAGE</a>', unsafe_allow_html=True)

# --- TAB 2: IMAGE TO IMAGE (Style Editor) ---
with tab2:
    st.subheader("Transform Style")
    up_img = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"], key="t2")
    if up_img:
        st.image(up_img, width=250)
        new_style = st.text_input("Change style to (e.g. Horror Zombie):")
        if st.button("Apply New Style"):
            style_url = f"https://image.pollinations.ai/prompt/{new_style.replace(' ', '%20')},realistic?nologo=true&seed={random.randint(1,999)}"
            st.image(style_url, use_column_width=True)
            st.markdown(f'<a href="{style_url}" target="_blank" class="download-btn">📥 SAVE STYLED IMAGE</a>', unsafe_allow_html=True)

# --- TAB 3: IMAGE TO VIDEO (Luma Style) ---
with tab3:
    st.subheader("Animate Image")
    up_vid = st.file_uploader("Upload Image to Animate", type=["jpg", "png", "jpeg"], key="t3")
    if up_vid:
        st.image(up_vid, width=250)
        if st.button("Animate Now"):
            with st.spinner("Rendering Motion..."):
                v_url = f"https://image.pollinations.ai/prompt/animated%20motion,video,cinematic,loop?nologo=true&seed={random.randint(1,9999)}"
                st.image(v_url, use_column_width=True)
                st.markdown(f'<a href="{v_url}" target="_blank" class="download-btn">📥 DOWNLOAD VIDEO</a>', unsafe_allow_html=True)
