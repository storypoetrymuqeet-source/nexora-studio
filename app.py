import streamlit as st
import requests
import io
from PIL import Image

# --- NEXORA STUDIO FINAL FIX ---
st.set_page_config(page_title="Nexora Studio", layout="centered")
st.title("🎬 Nexora AI Studio")

HF_TOKEN = "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"

# Yahan sirf scene likhna hai
prompt = st.text_input("Apni video ka scene likhein:", value="A scary haunted house")

if st.button("Generate Result"):
    if prompt:
        # URL ko check karein, ye bilkul sahi hai
        API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}

        with st.spinner("Nexora Engine kaam kar raha hai..."):
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, caption="Nexora Result")
                    st.success("Mubarak ho! Result aa gaya.")
                else:
                    st.error(f"Error Code: {response.status_code}")
                    st.write("Masla: Model abhi busy hai, 10 seconds baad dobara check karein.")
            except:
                st.error("Internet ka masla hai.")

