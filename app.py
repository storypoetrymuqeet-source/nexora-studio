import streamlit as st
import random

# Simple Setup
st.set_page_config(page_title="Nexora Studio")

st.title("🎬 Nexora Studio")

# Input
p = st.text_input("Yahan scene likhein:")

# Generate
if st.button("Generate Image"):
    if p:
        # Simple Random Seed
        s = random.randint(1, 999999)
        
        # Original Link without extra settings
        url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?seed={s}"
        
        # Display
        st.image(url)
        
        # Save Link
        st.markdown(f"[📥 Save Image]({url})")
