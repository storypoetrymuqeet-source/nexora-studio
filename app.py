import streamlit as st

# 1. Page Config for Premium Look
st.set_page_config(page_title="Nexora Editor Pro", layout="wide")

# 2. Advanced CSS to match your screenshots
st.markdown("""
    <style>
    .main { background: #12171d; color: #ffffff; }
    .stButton>button {
        background: #1e3a45; color: #40e0d0;
        border: 1px solid #40e0d0; border-radius: 8px;
        height: 3em; width: 100%; font-weight: bold;
    }
    .stButton>button:hover { background: #40e0d0; color: #12171d; }
    .upload-box {
        border: 2px dashed #40e0d0; border-radius: 15px;
        padding: 40px; text-align: center; background: #1a222a;
    }
    h1 { color: #40e0d0; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar for Navigation (Like your App Menu)
with st.sidebar:
    st.title("Nexora Menu")
    option = st.radio("Choose Mode:", ["Image Generator", "Photo Editor", "Video Magic"])

# 4. Main App Interface
st.title("N+ Nexora Editor Pro")

if option == "Photo Editor":
    st.subheader("🖼️ Photo Editor Mode")
    
    # Matching your "Add Image" Design
    uploaded_file = st.file_uploader("گلیری سے تصویر اپلوڈ کریں", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Original Image", use_column_width=True)
        
        # Action Buttons like your screenshot
        col1, col2, col3 = st.columns(3)
        with col1: st.button("Filters")
        with col2: st.button("Background Remove")
        with col3: st.button("Style Transfer")
    else:
        st.markdown('<div class="upload-box"><h3>+ Add Image</h3><p>گلیری سے تصویر اپلوڈ کریں</p></div>', unsafe_allow_html=True)

elif option == "Image Generator":
    st.subheader("🎨 AI Image Generator")
    prompt = st.text_input("Describe your magic:")
    if st.button("Start Creation"):
        st.info("Creating your vision...")

elif option == "Video Magic":
    st.subheader("🎬 Video Magic")
    st.markdown('<div class="upload-box"><h3>Start Animation</h3><p>ویڈیو جادو</p></div>', unsafe_allow_html=True)
