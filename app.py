import streamlit as st
import random

# Page Setup
st.set_page_config(page_title="Nexora Studio", layout="centered")

# Title
st.title("🎬 Nexora Simple Studio")

# Input Area
p = st.text_area("Apni Scene Likhein:", placeholder="e.g. Scary woman in dark house...")

# Generate Button
if st.button("Generate Image"):
    if p:
        with st.spinner("Bann rahi hai..."):
            seed = random.randint(1, 999999)
            # Original Flux model link
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width=1024&height=1024&nologo=true&seed={seed}&model=flux"
            
            # Show Image
            st.image(url)
            
            # Simple SAVE link
            st.markdown(f"### [📥 SAVE IMAGE]({url})")
    else:
        st.error("Pehle kuch likhein!")
