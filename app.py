import streamlit as st
import random
import urllib.parse

# 1. Page Config (Bilkul Sada)
st.set_page_config(page_title="Nexora Studio", layout="centered")

st.title("🎬 Nexora Studio")
st.write("Apni scene niche likhein aur 'Generate' dabayein.")

# 2. Input
p = st.text_area("Scene Description:", placeholder="Write here...", height=100)

# 3. Generate Logic
if st.button("🚀 Generate Image"):
    if p:
        with st.spinner("Processing..."):
            # Clean prompt for stability
            safe_p = urllib.parse.quote(p)
            seed = random.randint(1, 999999)
            
            # Direct High-Quality URL
            url = f"https://image.pollinations.ai/prompt/{safe_p}?width=1024&height=1024&nologo=true&seed={seed}&model=flux"
            
            # Show direct link first (in case image doesn't load)
            st.markdown(f"### [📥 Download Image]({url})")
            
            # Display Image
            st.image(url)
    else:
        st.error("Pehle kuch likhein!")
