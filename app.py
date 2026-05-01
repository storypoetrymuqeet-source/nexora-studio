import streamlit as st
import random
import time

st.set_page_config(page_title="Nexora Studio")
st.title("🎬 Nexora Studio")

p = st.text_input("Yahan scene likhein:", key="user_prompt")

if st.button("Generate Image"):
    if p:
        # Step 1: Thora intezar taake pichli request khatam ho jaye
        with st.spinner("Server ko check kar rahe hain..."):
            time.sleep(2) 
            
            seed = random.randint(1, 1000000)
            # Link ko thora change kiya hai taake server 'Too many requests' na de
            url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?seed={seed}&nologo=true"
            
            # Step 2: Image dikhana
            st.image(url)
            st.markdown(f"### [📥 SAVE IMAGE]({url})")
    else:
        st.error("Pehle kuch likhein!")
