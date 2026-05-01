        import streamlit as st
import random

# 1. Page Config
st.set_page_config(page_title="Nexora Studio", page_icon="🎨", layout="centered")

# 2. Strong CSS for Stability
st.markdown("""
    <style>
    .main { background: #0a0c10; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background-color: #ff4b2b; color: white; font-weight: bold; border: none;
    }
    img { border-radius: 15px; border: 2px solid #1f2937; width: 100%; margin-top: 10px; object-fit: contain; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Nexora Studio HQ")

# 3. Input
p = st.text_area("Write your prompt here...", placeholder="e.g. Scary woman in dark house...", height=100)

# 4. Two Strong Columns
col1, col2 = st.columns(2)
with col1:
    r_choice = st.selectbox("Size / Ratio:", ["9:16 (Shorts)", "16:9 (YouTube)", "1:1 (Square)"])
    
    # Pixel Logic: Lowering 16:9 resolution slightly for stability
    if "9:16" in r_choice: w, h = 720, 1280
    elif "16:9" in r_choice: w, h = 1024, 576  # Changed from 1280, 720 for better load
    else: w, h = 1024, 1024

with col2:
    # Adding model selection back but very simple
    m_choice = st.selectbox("Quality:", ["Realistic (Flux)", "Artistic (Stable)"])
    model_tag = "&model=flux" if "Flux" in m_choice else ""

# Hidden Quality tags for stability
q_tags = ", photo, photorealistic, 8k, detailed, cinematic" if "Flux" in m_choice else ""

# 5. Execution
if st.button("🚀 Generate Masterpiece"):
    if p:
        with st.spinner("💎 Processing your HQ image..."):
            seed = random.randint(1, 999999)
            # URL fix: Simplify and prevent code leak
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}{q_tags.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed={seed}{model_tag}"
            
            # Show Image (Full Width Fix)
            st.image(url, caption=f"Format: {r_choice}", use_column_width=True)
            
            # 6. FIXED Simple Download Link (No code leaks)
            st.success("Image generated! Click below to save.")
            st.markdown(f"### [📥 SAVE HD IMAGE]({url})")
    else:
        st.warning("Please describe your scene first!")

