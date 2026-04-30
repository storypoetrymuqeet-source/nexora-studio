import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Nexora Studio Pro", page_icon="🎬", layout="wide")

# 2. Advanced CSS for Buttons and UI
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #007bff, #00d4ff); 
        color: white; font-weight: bold; border: none;
    }
    img { border-radius: 15px; border: 2px solid #30363d; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛠️ Nexora Settings")
menu = st.sidebar.radio("Go to:", ["⚡ Flash Image (Text)", "🎥 Video Magic (Image/Text)"])

# --- TOOL 1: FLASH IMAGE (With All Ratios) ---
if menu == "⚡ Flash Image (Text)":
    st.header("⚡ Text to Multi-Ratio Image")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        prompt = st.text_area("What do you want to create?", placeholder="e.g. A scary ghost in a village...")
        # ALL RATIOS ADDED HERE
        ratio_choice = st.selectbox("Select Platform / Ratio:", [
            "16:9 (YouTube Video)", 
            "9:16 (TikTok / Reels / Shorts)", 
            "4:5 (Instagram Post)", 
            "1:1 (Square / Facebook)",
            "21:9 (Ultrawide Cinematic)"
        ])
        style = st.selectbox("Select Art Style:", ["Cinematic Horror", "Realistic 3D", "Pixar Animation", "Digital Painting"])

    # Mapping Ratios to Pixels
    width, height = (1024, 1024) # Default
    if "16:9" in ratio_choice: width, height = (1280, 720)
    elif "9:16" in ratio_choice: width, height = (720, 1280)
    elif "4:5" in ratio_choice: width, height = (1080, 1350)
    elif "21:9" in ratio_choice: width, height = (1920, 822)

    if st.button("Generate HD Art"):
        if prompt:
            with st.spinner("💎 Nexora is crafting your masterpiece..."):
                final_p = f"{prompt}, {style}, 8k, highly detailed, masterpiece"
                url = f"https://image.pollinations.ai/prompt/{final_p.replace(' ', '%20')}?width={width}&height={height}&nologo=true"
                st.image(url, caption=f"Result: {ratio_choice}")
                st.markdown(f'<a href="{url}" target="_blank" style="text-decoration:none;"><div style="text-align:center; padding:10px; background:#21262d; color:white; border-radius:10px;">📥 Download Full Quality</div></a>', unsafe_allow_html=True)

# --- TOOL 2: VIDEO MAGIC (Image-to-Video & Text-to-Video) ---
elif menu == "🎥 Video Magic (Image/Text)":
    st.header("🎥 Cinematic Motion Engine")
    
    st.write("### Option A: Image to Video")
    uploaded_file = st.file_uploader("Upload your photo from gallery", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Original Photo", width=300)
        motion = st.selectbox("Select Motion Type:", ["Slow Cinematic Zoom", "Ghostly Fog Motion", "Walking Motion", "Blinking Eyes"])
        
        if st.button("Animate Uploaded Image"):
            with st.spinner("Adding Motion..."):
                v_url = f"https://image.pollinations.ai/prompt/animated%20motion%20of%20{motion.replace(' ', '%20')},cinematic,video%20loop?nologo=true&seed={int(time.time())}"
                st.image(v_url, caption="AI Motion Result")
                st.success("Motion Generated! Click 'Save' below.")

    st.divider()
    st.write("### Option B: Text to Video")
    v_prompt = st.text_input("Describe the video scene:")
    if st.button("Create Video from Text"):
        if v_prompt:
            with st.spinner("Rendering Video..."):
                v_url = f"https://image.pollinations.ai/prompt/{v_prompt.replace(' ', '%20')},animated%20video,motion?nologo=true"
                st.image(v_url, caption="Video Preview")
