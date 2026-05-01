import streamlit as st

# Page Setup
st.set_page_config(page_title="Nexora Editor Pro", page_icon="➕", layout="wide")

# Styling for a professional look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #4CAF50; color: white; font-weight: bold; }
    .stSelectbox, .stTextInput, .stTextArea { background-color: #1e2130; }
    </style>
    """, unsafe_allow_html=True)

st.title("Nexora Editor Pro 🎨➕🎬")
st.write("Professional Studio: Images, Gallery Editing, aur Video Magic.")

# Sidebar Menu
st.sidebar.title("Nexora Menu")
choice = st.sidebar.radio("Kia karna chahti hain?", 
    ["All-Size AI Image", "Gallery Photo Edit (+)", "Video Magic (Beta)"])

# 1. AI Image with Ratios
if choice == "All-Size AI Image":
    st.subheader("🖼️ Text to Professional Image")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        ratio = st.selectbox("Select Ratio (Size):", [
            "Square (1:1) - Instagram", 
            "Landscape (16:9) - YouTube", 
            "Portrait (9:16) - TikTok/Reels", 
            "Standard (4:5) - Facebook", 
            "Cinematic (21:9) - Movie"
        ])
        
        # Logic for Width and Height
        if "1:1" in ratio: w, h = 1024, 1024
        elif "16:9" in ratio: w, h = 1280, 720
        elif "9:16" in ratio: w, h = 720, 1280
        elif "4:5" in ratio: w, h = 1024, 1280
        else: w, h = 1600, 680

    with col1:
        prompt = st.text_area("Apna idea likhein (English):", placeholder="e.g. A scary 3D ghost in a dark mansion, cinematic lighting...")
        
    if st.button("Generate Masterpiece"):
        if prompt:
            with st.spinner("Nexora aapki tasveer bana raha hai..."):
                # Pollinations AI link with custom width/height
                url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed=99"
                st.image(url, caption=f"Nexora Result - Size: {ratio}")
                st.markdown(f"### [📥 Download Full Image]({url})")
        else:
            st.warning("Pehle description toh likhein!")

# 2. Gallery Upload Feature
elif choice == "Gallery Photo Edit (+)":
    st.subheader("➕ Gallery se Photo Edit Karein")
    st.write("Apni gallery se photo upload kar ke usay AI se change karein.")
    
    uploaded_file = st.file_uploader("Photo select karein:", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Aapki Asli Photo", width=350)
        instruction = st.text_input("Is photo mein kia tabdeeli karni hai? (e.g. Make it a scary movie poster)")
        
        if st.button("Apply AI Magic"):
            st.info("Azkir, hum aapki photo ko analyze kar rahe hain. Editing API link ho rahi hai!")

# 3. Video Magic Section
else:
    st.subheader("🎬 AI Video Generation")
    v_mode = st.selectbox("Kaunsi video banani hai?", ["Prompt to Video", "Image to Video (Animate)"])
    
    if v_mode == "Prompt to Video":
        v_prompt = st.text_area("Video description likhein:")
        if st.button("Create Video"):
            st.success("Nexora Video Engine start ho raha hai!")
    else:
        st.write("Gallery se image upload karein taake hum use animate kar saken.")
        st.file_uploader("Upload Image for Animation:")
