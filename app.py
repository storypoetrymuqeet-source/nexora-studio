import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Nexora Studio Pro", page_icon="🎨", layout="centered")

# 2. Modern UI Design (CSS)
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #ff4b2b, #ff416c); 
        color: white; font-weight: bold; border: none;
    }
    img { border-radius: 15px; border: 2px solid #30363d; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Multi-Ratio Creator 🚀")

# User Inputs
prompt = st.text_area("What to create?", placeholder="e.g. Scary ghost...", height=100)

# 3. FIX: Adding more Ratio Options with Pixels
ratio = st.selectbox("Select Ratio / Platform:", ["16:9 (YouTube)", "9:16 (Shorts/TikTok)", "1:1 (Square)", "4:5 (Instagram Portrait)"])

# Mapping Ratios to Pixels (This is crucial for the AI server to work)
width, height = (1024, 1024)
if ratio == "16:9 (YouTube)": width, height = (1280, 720)
elif ratio == "9:16 (Shorts/TikTok)": width, height = (720, 1280)
elif ratio == "4:5 (Instagram Portrait)": width, height = (1080, 1350)

if st.button("Generate HD Image"):
    if prompt:
        with st.spinner("💎 Nexora is crafting your art..."):
            
            # 4. FIX: Full AI Link Construction with Resolution
            enhanced_prompt = f"{prompt}, hyper-realistic, 8k, cinematic lighting, highly detailed"
            url = f"https://image.pollinations.ai/prompt/{enhanced_prompt.replace(' ', '%20')}?width={width}&height={height}&nologo=true"
            
            # Show Image
            st.image(url, caption=f"Result: {ratio}", use_column_width=True)
            
            # Save Link
            st.markdown(f'<a href="{url}" target="_blank" style="text-decoration:none;"><div style="text-align:center; padding:10px; background:#21262d; color:white; border-radius:10px;">📥 Click Here to Save HD Image</div></a>', unsafe_allow_html=True)

    else:
        st.warning("Please describe what to create!")
