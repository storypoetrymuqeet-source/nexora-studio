import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Nexora Flash Studio Pro", page_icon="⚡", layout="centered")

# 2. Modern UI CSS (Professional Look)
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stTextArea textarea { background-color: #161b22 !important; color: white !important; border: 1px solid #30363d !important; border-radius: 10px; }
    .stButton>button { 
        background: linear-gradient(45deg, #007bff, #00d4ff); 
        color: white; border: none; border-radius: 12px; height: 3.5em; font-weight: bold; font-size: 1.1em;
    }
    img { border-radius: 20px; box-shadow: 0px 15px 35px rgba(0,0,0,0.7); border: 2px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("Nexora Flash Studio ⚡")
st.write("### AI High-Definition Image Engine")

# 3. Input with "Auto-Enhance" logic
prompt = st.text_area("What are you imagining?", placeholder="Example: A scary ghost in an old haveli...")

if st.button("Generate HD Image"):
    if prompt:
        with st.spinner("💎 Nexora is enhancing and generating your art..."):
            # Background mein quality keywords add kar diye hain
            enhanced_prompt = f"{prompt}, hyper-realistic, 8k resolution, cinematic lighting, masterpiece, sharp focus"
            
            # Professional URL construction
            url = f"https://image.pollinations.ai/prompt/{enhanced_prompt.replace(' ', '%20')}?nologo=true&width=1024&height=1024&seed=786"
            
            st.divider()
            st.image(url, caption="Nexora High-Definition Result")
            
            # Simple Download Button
            st.markdown(f'<a href="{url}" target="_blank"><button style="width:100%; border-radius:10px; padding:10px; background:#21262d; color:white; border:1px solid #30363d; cursor:pointer;">📥 Save Image</button></a>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a description first!")

st.divider()
st.caption("Nexora Studio | Quality Optimized v2.0")
