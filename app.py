import streamlit as st
import requests
import io
from PIL import Image

# --- NEXORA STUDIO SUPER FIXED ---
st.set_page_config(page_title="Nexora Studio", layout="centered")
st.title("🎬 Nexora AI Studio")

HF_TOKEN = "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"

prompt = st.text_input("Apni video ka scene likhein:", placeholder="A scary ghost in a dark room...")

if st.button("Generate Result"):
    if prompt:
        # Ye model 100% online hai aur 404 nahi deta
        API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}

        with st.spinner("Nexora Engine kaam kar raha hai..."):
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                if response.status_code == 200:
                    image_bytes = response.content
                    image = Image.open(io.BytesIO(image_bytes))
                    st.image(image, caption="Nexora Studio Result")
                    st.success("Mubarak ho Azkir! Connection kamyab raha.")
                elif response.status_code == 503:
                    st.info("Model thora busy hai, 20 seconds baad phir button dabayein.")
                else:
                    st.error(f"Error Code: {response.status_code}")
            except:
                st.error("Kuch technical masla hai, dobara try karein.")
    else:
        st.warning("Pehle scene toh likhein!")
