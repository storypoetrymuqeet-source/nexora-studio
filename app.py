import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Page Setup
st.set_page_config(page_title="Nexora Studio", page_icon="🎨")

# Design (Buttons aur Style)
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3em; 
        background-color: #4F8BF9; color: white; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Nexora Studio 🎨")
st.write("Fast & Free AI Image Generator")

# Buttons
col1, col2, col3 = st.columns(3)
btn_aloo = col1.button("🥔 Aloo Selfie")
btn_horror = col2.button("👻 Desi Horror")
btn_pizza = col3.button("🍕 Pizza Friend")

user_input = st.text_input("Ya apna idea likhein:", placeholder="e.g. A cat in space")

# Logic
final_prompt = ""
if btn_aloo: final_prompt = "A funny potato character taking a selfie in a Pakistani market, 3d render"
if btn_horror: final_prompt = "A scary desi ghost in a dark old street, cinematic horror"
if btn_pizza: final_prompt = "A pizza slice with human face talking, cute 3d style"
if user_input: final_prompt = user_input

if final_prompt:
    with st.spinner("Bann raha hai..."):
        # Pollinations AI (Fada Fad Link)
        url = f"https://image.pollinations.ai/prompt/{final_prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="Aapki Tasveer tayyar hai!", use_column_width=True)
        
        # Download Button
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.download_button("📥 Download", buf.getvalue(), "nexora_art.png", "image/png")

