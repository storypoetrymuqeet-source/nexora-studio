import streamlit as st

# 1. Page Settings
st.set_page_config(page_title="Nexora Studio Pro", page_icon="🎨", layout="centered")

# 2. Premium CSS (Fixing Buttons)
st.markdown("""
    <style>
    .main { background: #0d1117; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.5em; 
        background: linear-gradient(45deg, #007bff, #00d4ff); 
        color: white; font-weight: bold; border: none;
    }
    .stButton>button:hover { opacity: 0.8; transform: scale(1.02); }
    img { border-radius: 15px; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

st.title("Nexora Studio Pro 🚀")

# Sidebar for Navigation
menu = st.sidebar.radio("Select Tool:", ["Instant Flash", "Gallery Editor (+)", "Video Magic"])

# --- TOOL 1: INSTANT FLASH (Text to Image) ---
if menu == "Instant Flash":
    st.subheader("⚡ Text to High-Res Image")
    prompt = st.text_area("Enter prompt:", placeholder="e.g. Scary ghost...")
    if st.button("Generate Image"):
        if prompt:
            with st.spinner("Generating..."):
                enhanced = f"{prompt}, hyper-realistic, 8k, masterpiece"
                url = f"https://image.pollinations.ai/prompt/{enhanced.replace(' ', '%20')}?nologo=true&seed=123"
                st.image(url)
                # FIXED SAVE BUTTON
                st.markdown(f'<a href="{url}" target="_blank" style="text-decoration:none;"><div style="text-align:center; padding:10px; background:#21262d; color:white; border-radius:10px; border:1px solid #30363d;">📥 Click Here to Save Image</div></a>', unsafe_allow_html=True)

# --- TOOL 2: GALLERY EDITOR (Image to Image) ---
elif menu == "Gallery Editor (+)":
    st.subheader("➕ Gallery Editor (Image to Image)")
    uploaded_file = st.file_uploader("Upload from Gallery", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Your Uploaded Photo", width=300)
        style = st.selectbox("Choose Style:", ["Horror Style", "Cinematic", "Cartoon"])
        
        if st.button("Apply AI Transformation"):
            st.info(f"Transforming your image into {style}... Please wait.")
            # Yahan hum Image-to-Image logic add karenge jab ye live ho jaye

# --- TOOL 3: VIDEO MAGIC ---
else:
    st.subheader("🎬 Video Magic (Beta)")
    st.write("Convert your ideas into 5-second AI clips.")
    v_prompt = st.text_input("Describe the video scene:")
    if st.button("Create Video"):
        st.warning("Video server is busy. Retrying in 10 seconds...")
