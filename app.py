import streamlit as st
import random

# 1. Page Config
st.set_page_config(page_title="Nexora Studio", layout="centered")

st.title("🎬 Nexora Simple Studio")

# 2. Input
p = st.text_input("Yahan scene likhein:")

# 3. Generate
if st.button("Generate Image"):
    if p:
        seed = random.randint(1, 99999)
        # Bilkul chota link (taake broken image na aaye)
        url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width=1024&height=1024&nologo=true&seed={seed}"
        
        # Pehle link dikhayega phir image (taake agar image load na ho toh link se dekh sakein)
        st.markdown(f"### [📥 CLICK HERE TO SAVE]({url})")
        st.image(url)
    else:
        st.error("Kuch likhein!")
