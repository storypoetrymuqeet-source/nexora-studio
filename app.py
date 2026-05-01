import streamlit as st
import random

# 1. Page Config (Ultra HD Optimized)
st.set_page_config(page_title="Nexora Nightmare Pro", page_icon="🎬", layout="centered")

# 2. Advanced Premium CSS
st.markdown("""
    <style>
    .main { background: #05070a; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 15px; height: 3.8em; 
        background: linear-gradient(45deg, #2c3e50, #bdc3c7); 
        color: white; font-weight: bold; border: none; transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 6px 20px rgba(0,0,0,0.5); }
    
    /* Input Styling */
    .stTextArea textarea, .stSelectbox select {
        border-radius: 12px; background: #1a252f; border: 1px solid #34495e; color: white;
    }
    
    /* Image Display Fix (No Triangles) */
    img { 
        border-radius: 20px; border: 2px solid #30363d; 
        box-shadow: 0px 10px 30px rgba(0,0,0,0.7);
        width: 100% !important; height: auto !important;
        object-fit: contain;
    }
    
    /* HD Download Button */
    .download-btn {
        display: block; width: 100%; text-align: center; background: #28a745;
        color: white; padding: 15px; border-radius: 12px; font-weight: bold;
        text-decoration: none; margin-top: 20px; font-size: 1.1em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Nexora Nightmare Pro")

# --- MAIN TOOL: ULTIMATE QUALITY GENERATOR ---
st.write("### 🖋️ Describe Scene:")
p = st.text_area("", placeholder="e.g. Scary woman in dark house...", key="p1p", height=100)

col1, col2 = st.columns(2)
with col1:
    st.write("### 📱 Platform (Ratio)")
    r_choice = st.selectbox("", [
        "9:16 (TikTok/Shorts)", 
        "16:9 (YouTube Video)", 
        "1:1 (Insta Square)"
    ])
    w, h = (720, 1280) if "9:16" in r_choice else (1280, 720) if "16:9" in r_choice else (1024, 1024)

# 3. FIX: Adding Image Style Selector with Pro-Level Prompts
with col2:
    st.write("### ✨ Art Style")
    s_choice = st.selectbox("", [
        "Ultra-Realistic Horror", 
        "Cinematic Dark Fantasy", 
        "Pixar-style 3D Render", 
        "Gothic oil painting"
    ])
    
    # Advanced Style Prompt Engineering
    style_tags = ""
    if "Realistic" in s_choice:
        style_tags = ", photo, highly detailed face, realistic eyes, cinematic lighting, photorealistic, sharp focus, master piece, depth of field"
    elif "Cinematic" in s_choice:
        style_tags = ", epic composition, Unreal Engine 5 render, volumetric fog, dramatic lighting, detailed texture, fantasy art"
    elif "Pixar" in s_choice:
        style_tags = ", cute character design, smooth lighting, stylized render, joyful, animation masterpiece, detailed eyes"
    elif "Gothic" in s_choice:
        style_tags = ", oil painting, brush strokes, dark color palette, dramatic shadows, mysterious, traditional art, high detail"

# Action
if st.button("🚀 GENERATE MASTERPIECE"):
    if p:
        with st.spinner("💎 Nexora is crafting HQ art..."):
            # Random seed for unique results
            seed = random.randint(1, 999999)
            # Full Quality Link
            final_prompt = f"{p}{style_tags}"
            url = f"https://image.pollinations.ai/prompt/{final_prompt.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed={seed}&model=flux"
            
            # Show Image (Full Width Fix)
            st.image(url, caption=f"Ratio: {r_choice} | Style: {s_choice}", use_column_width=True)
            
            # HQ Download Link
            st.markdown(f'<a href="{url}" target="_blank" class="download-btn">📥 DOWNLOAD ULTRA-HD IMAGE</a>', unsafe_allow_html=True)
    else:
        st.error("Describe your scene first!")
