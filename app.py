import streamlit as st
import requests
import io
from PIL import Image

# --- NEXORA STUDIO REFRESHED ---
st.set_page_config(page_title="Nexora Studio", layout="centered")
st.title("🎬 Nexora AI Studio")

# Aapka Confirm Token
HF_TOKEN = "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"

prompt = st.text_input("Apni video ka scene likhein:", placeholder="A scary ghost...")

if st.button("Generate Result"):
    if prompt:
        # Ye model is waqt sab se zyada active hai
        API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}

        with st.spinner("Nexora Engine kaam kar raha hai..."):
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, caption="Nexora Result")
                    st.success("Mubarak ho Azkir! Connection kamyab raha.")
                else:
                    # Yahan humein asli waja pata chale gi
                    st.error(f"Response Code: {response.status_code}")
                    st.write(response.text) 
            except Exception as e:
                st.error(f"Technical Masla: {e}")
    else:
        st.warning("Pehle scene likhein!")
