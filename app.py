import streamlit as st
import random
import urllib.parse

# 1. Page Setup
st.set_page_config(page_title="Nexora Studio", layout="centered")

st.title("🎬 Nexora Studio")

# 2. Input Area
p = st.text_input("Yahan scene likhein:", placeholder="e.g. Butterfly and garden...")

# 3. Generate Logic
if st.button("🚀 Generate Image"):
    if p:
        # Har baar naya seed taake purani broken image cache na ho
        seed = random.randint(1, 999999)
        safe_p = urllib.parse.quote(p)
        
        # Link ko short rakha hai taake mobile par masla na kare
        url = f"https://pollinations.ai/p/{safe_p}?width=1024&height=1024&seed={seed}"
        
        st.markdown(f"### [📥 DOWNLOAD IMAGE]({url})")
        
        # Image dikhane ka naya tareeqa
        st.image(url, use_column_width=True)
        
        st.info("Agar tasveer nahi aayi, toh dobara button dabayein.")
    else:
        st.warning("Pehle kuch likhein!")
