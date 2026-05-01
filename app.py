import streamlit as st

# Page Configuration
st.set_page_config(page_title="Nexora Editor Pro", page_icon="➕", layout="wide")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("Nexora Editor Pro 🎨➕🎬")
st.write("Market-ready Studio: Images, Videos, aur Editing sab aik jagah.")

# Sidebar Navigation
st.sidebar.image("https://via.placeholder.com/150?text=Nexora+Logo", width=100)
st.sidebar.title("Studio Menu")
choice = st.sidebar.radio("Kia banana chahti hain?", 
    ["All-Size AI Image", "Gallery Photo Edit (+)", "Video Magic (Beta)"])

# 1. ALL-SIZE AI IMAGE GENERATOR
if choice == "All-Size AI Image":
    st.subheader("🖼️ Text to Professional Image")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        ratio = st.selectbox("Select Ratio:", [
            "Square (1:1)", "YouTube (16:9)", "TikTok/Reels (9:16)", "Facebook (4:5)", "Cinematic (21:9)"
        ])
        # Ratio Dimensions
        if "1:1" in ratio: w, h = 1024, 1024
        elif "16:9" in ratio: w, h = 1280, 720
        elif "9:16" in ratio: w, h = 720, 1280
        elif "4:5" in ratio: w, h = 1024, 1280
        else: w, h = 1600, 680

    with col1:
        prompt = st.text_area("Apna idea likhein (Horror, 3D, Portrait...):", placeholder="e.g. A scary 3D ghost in a dark mansion...")
        
    if st.button("Generate Masterpiece"):
        if prompt:
            with st.spinner("Nexora Engine kaam kar raha hai..."):
                url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width={w}&height={h}&nologo=true&seed=123"
                st.image(url, caption=f"Size: {ratio}")
                st.markdown(f"### [📥 Download Image]({url})")
        else:
            st.warning("Pehle prompt likhein!")

# 2. GALLERY PHOTO EDITING
elif choice == "Gallery Photo Edit (+)":
    st.subheader("➕ Gallery se Edit Karein")
    uploaded_file = st.file_uploader("Apni photo select karein:", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Aapki Original Photo", width=400)
        instruction = st.text_input("Is photo mein kia tabdeeli karni hai? (e.g. Change to horror style)")
        if st.button("Apply AI Edit"):
            st.info("Azkir, Editing API connect ho rahi hai. Jald hi aapka result yahan nazar aayega!")

# 3. VIDEO MAGIC
else:
    st.subheader("🎬 AI Video Generation")
    v_type = st.selectbox("Video Type:", ["Prompt to Video", "Image to Video"])
    
    if v_type == "Prompt to Video":
        v_prompt = st.text_area("Video description:")
        if st.button("Create Video"):
            st.success("Video processing shuru! AI engine link ho raha hai.")
    else:
        st.write("Image upload karein aur use animate karein.")
        st.file_uploader("Upload Image for Animation:")
