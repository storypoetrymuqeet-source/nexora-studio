import streamlit as st
import random

st.set_page_config(page_title="Nexora Studio")
st.title("🎬 Nexora Studio")

# Input field
p = st.text_input("Yahan scene likhein:", key="user_prompt")

# Image dikhane ke liye ek khaas khali jagah (placeholder)
container = st.empty()

if st.button("Generate Image"):
    if p:
        # Har baar naya seed
        seed = random.randint(1, 1000000)
        
        # Sab se simple aur original link
        url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?seed={seed}"
        
        with st.spinner("Nayi tasveer bann rahi hai..."):
            # Purani image ko saaf kar ke nayi dikhayega
            container.image(url)
            st.markdown(f"[📥 Save Image]({url})")
    else:
        st.error("Pehle kuch likhein!")
