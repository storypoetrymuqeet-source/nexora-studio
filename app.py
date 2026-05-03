import streamlit as st
import requests
import io
from PIL import Image

# --- NEXORA STUDIO 100% FIXED ---
st.set_page_config(page_title="Nexora Studio", layout="centered")
st.title("🎬 Nexora AI Studio")

# Aapka Token
HF_TOKEN = "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"

prompt = st.text_input("Apni video ya image ka scene likhein:", value="A scary ghost in a forest")

if st.button("Generate Result"):
    if prompt:
        # Yeh model Hugging Face ka sab se basic aur hamesha chalne wala model hai
        API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}

        with st.spinner("Nexora Engine image bana raha hai..."):
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, caption="Nexora Result")
                    st.success("Mubarak ho! Result aa gaya.")
                elif response.status_code == 404:
                    st.error("Abhi bhi 404 aa raha hai? Shayad Token ka masla hai.")
                else:
                    st.error(f"Error Code: {response.status_code}")
            except:
                st.error("Connection masla!")
    else:
        st.warning("Pehle scene toh likhein!")
