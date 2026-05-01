import streamlit as st
import random
import time

# 1. Page Title
st.set_page_config(page_title="Nexora Studio", layout="centered")
st.title("🎬 Nexora Studio")

# 2. Input Area
p = st.text_input("Yahan scene likhein:", placeholder="e.g. Butterfly and garden...")

# 3. Generate Logic
if st.button("🚀 Generate Image"):
    if p:
        # Har baar naya number aur time taake image refresh ho sake
        unique_id = random.randint(1, 1000000)
        current_time = int(time.time())
        
        # Ye URL har baar server ko 'force' karega nayi image banane par
        url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width=1024&height=1024&nologo=true&seed={unique_id}&v={current_time}&model=flux"
        
        with st.spinner("Nayi tasveer bann rahi hai..."):
            # Image Display
            st.image(url, use_column_width=True)
            
            # Download Link
            st.markdown(f"### [📥 SAVE IMAGE]({url})")
            
            st.success("Agar nayi image chahiye, toh button dobara dabayein!")
    else:
        st.error("Kuch likhein pehle!")
