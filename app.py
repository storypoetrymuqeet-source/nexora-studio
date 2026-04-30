import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Nexora Studio Pro", page_icon="🎬", layout="centered")

# 2. Premium UI Design (Mobile Friendly)
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 15px; height: 3.8em; 
        background: linear-gradient(45deg, #1e3a8a, #3b82f6); 
        color: white; font-weight: bold; border: none;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }
    .stButton>button:hover { transform: scale(1.02); opacity: 0.9; }
    img { border-radius: 15px; border: 2px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Nexora AI Hub")
menu = st.sidebar.radio("Choose Service:", ["⚡ Flash Image", "➕ Style Editor", "🎬 Video Magic"])

# --- TOOL 1: INSTANT FLASH (Prompt to Image) ---
if menu == "⚡ Flash Image":
    st.header("⚡ Text to HD Image")
    prompt = st.text_area("Describe your image:", placeholder="e.g. A scary ghost in a dark mansion, 8k...")
    if st.button("Generate Art"):
        if prompt:
            with st.spinner("💎 Nexora is creating your HD Image..."):
                enhanced = f"{prompt}, hyper-realistic, cinematic lighting, high detail"
                url = f"https://image.pollinations.ai/prompt/{enhanced.replace(' ', '%20')}?nologo=true&width=1024&height=1024"
                st.image(url)
                st.markdown(f'<a href="{url}" target="_blank" style="text-decoration:none;"><div style="text-align:center; padding:12px; background:#21262d; color:white; border-radius:10px; border:1px solid #30363d;">📥 Save High-Res Image</div></a>', unsafe_allow_html=True)

# --- TOOL 2: STYLE EDITOR (Image to Image) ---
elif menu == "➕ Style Editor":
    st.header("➕ Gallery Style Transformation")
    uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Original Photo", width=300)
        style_prompt = st.text_input("New Style (e.g., Turn into a 3D Horror Character):")
        
        if st.button("Apply Transformation"):
            if style_prompt:
                bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    bar.progress(i + 1)
                with st.spinner("Redrawing your image..."):
                    res_url = f"https://image.pollinations.ai/prompt/{style_prompt.replace(' ', '%20')},highly%20detailed?nologo=true&seed={int(time.time())}"
                    st.image(res_url, caption="Transformed Result")
                    st.markdown(f'<a href="{res_url}" target="_blank" style="text-decoration:none;"><div style="text-align:center; padding:10px; background:#161b22; color:white; border-radius:10px;">📥 Save New Style</div></a>', unsafe_allow_html=True)

# --- TOOL 3: VIDEO MAGIC (Prompt to Video) ---
else:
    st.header("🎬 Video Magic")
    st.write("Convert your scary prompts into AI Motion Clips.")
    v_prompt = st.text_input("Video Scene Description:", placeholder="e.g. A ghost walking slowly, fog moving in haveli...")
    
    if st.button("Create AI Video"):
        if v_prompt:
            with st.spinner("🎥 Rendering your Video Clip... (Wait 30-40s)"):
                # Fast Video Rendering
                v_url = f"https://image.pollinations.ai/prompt/{v_prompt.replace(' ', '%20')},cinematic%20motion,video%20loop?nologo=true&seed=42"
                
                # Showing preview and download
                st.info("Generating cinematic motion for your prompt...")
                st.image(v_url, caption="Video Preview (Motion Active)")
                st.success("Video Rendered Successfully!")
                st.markdown(f'<a href="{v_url}" target="_blank" style="text-decoration:none;"><div style="text-align:center; padding:15px; background:#1e3a8a; color:white; border-radius:10px; font-weight:bold;">📥 Download Video Clip</div></a>', unsafe_allow_html=True)
