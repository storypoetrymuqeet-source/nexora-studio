import streamlit as st
import random

# Simple Layout
st.set_page_config(page_title="Nexora Studio", layout="centered")

st.title("🎬 Nexora Simple Studio")

# Input
p = st.text_input("Enter Prompt:")

# Simple Ratio Selection
r = st.radio("Select Size:", ["Vertical (9:16)", "Horizontal (16:9)"])
w, h = (720, 1280) if "Vertical" in r else (1280, 720)

if st.button("Generate"):
    if p:
        seed = random.randint(1, 1000)
        # Direct stable link
        url = f"https://image.pollinations.ai/prompt/{p.replace(' ', '%20')}?width={w}&height={h}&seed={seed}&nologo=true"
        
        # Displaying as a link first to ensure you can at least save it
        st.markdown(f"### [👉 CLICK HERE TO SEE IMAGE]({url})")
        st.image(url)
    else:
        st.error("Kuch likhein pehle!")
