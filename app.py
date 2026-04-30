import streamlit as st
import random

# 1. Page Config (Ultra HD Layout)
st.set_page_config(page_title="Nexora Ultra-HD Studio", page_icon="🎨", layout="centered")

# 2. Premium Professional CSS
st.markdown("""
    <style>
    .main { background: #05070a; color: #ffffff; }
    
    /* Buttons with Glow Effect */
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 4em; 
        background: linear-gradient(90deg, #1e3a8a, #3b82f6); 
        color: white; font-weight: bold; border: none;
        transition: 0.3s; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6); }

    /* Input Styling */
    .stTextArea textarea { border-radius: 12px; background: #111827; border: 1px solid #374151; color: white; }
    
    /* Image Display Fix */
    img { 
        border-radius: 15px; border: 3px solid #1f2937; 
        box-shadow: 0px 20px 40px rgba(0,0,0,0.7);
        width: 100% !important; height: auto !important;
    }
    
    /* HD Download Button */
    .hd-download {
        display: block; width: 100%; text-align: center; 
        background: #10b981; color: white; padding: 15px; 
        border-radius: 12px; font-weight: bold; text-decoration: none; 
        margin-top: 20px; font-size: 1.1em;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #3b82f6;'>💎 Nexora Ultra-HD Creator</h1>", unsafe_allow_html=True)

# 3. Main Interface
st.write("### 🖋️ Describe Your Vision (Scary/Horror/Fantasy)")
p = st.text_area("", placeholder="Enter your detailed prompt here...", height=120)

col1, col2 = st.columns(2)
with col1:
    st.write("### 📱 Platform / Ratio")
    r_choice = st.selectbox("", [
        "9:16 (TikTok/Shorts/Reels)", 
        "16:9 (YouTube/Facebook Video)", 
        "1:1 (Insta Square)", 
        "4:5 (Insta Portrait)"
    ])
    # Exact Resolution Logic for High Quality
    w, h = (720, 1280) if "9:16" in r_choice else (1280, 720) if "16:9" in r_choice else (1080, 1350) if "4:5" in r_choice else (1024, 1024)

with col2:
    st.write("### ✨ Art Style")
    s_choice = st.selectbox("", [
        "Hyper-Realistic Horror (4K)", 
        "Cinematic 3D Animation", 
        "Dark Fantasy Concept Art", 
        "Vintage Gothic Photo"
    ])
    # Pro Prompt Engineering Tags
    style_tags = ", photorealistic, 8k, extreme detail, cinematic lighting, masterpiece, sharp focus, ray tracing"

# Action
if st.button("🚀 GENERATE ULTRA-HD IMAGE"):
    if p:
        with st.spinner("💎 Nexora AI is rendering in 4K..."):
            seed = random.randint(1, 999999)
            # Construction of High-Quality URL
            final_prompt = f"{p}{style_tags}"
            url = f"https://image.pollinations.ai/prompt/{final_prompt.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed={seed}&model=flux"
            
            # Display Image with Column Width Fix
            st.image(url, caption=f"Quality: Ultra HD | Ratio: {r_choice}", use_container_width=True)
            
            # Download Link
            st.markdown(f'<a href="{url}" target="_blank" class="hd-download">📥 DOWNLOAD 4K IMAGE</a>', unsafe_allow_html=True)
            st.success("Quality is ready! Upload this to Luma AI for best video results.")
    else:
        st.error("Please enter a prompt first!")
