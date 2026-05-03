import streamlit as st
import requests

# --- NEXORA VIDEO STUDIO ---
st.set_page_config(page_title="Nexora Video Studio", layout="centered", page_icon="🎬")
st.title("🎬 Nexora AI Video Studio")

# Aapka Token jo hum ne abhi nikala
HF_TOKEN = "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"

prompt = st.text_input("Apni video ka scene likhein:", placeholder="e.g. A haunted house in heavy rain...")

if st.button("📽️ Generate AI Video"):
    if prompt:
        API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}

        with st.spinner("Nexora Engine video bana raha hai... 1-2 minute lag sakte hain..."):
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                if response.status_code == 200:
                    st.video(response.content)
                    st.success("Mubarak ho Azkir! Video tayyar hai.")
                elif response.status_code == 503:
                    st.info("Server load ho raha hai. 30 seconds baad dobara try karein.")
                else:
                    st.error(f"Masla aya hai. Code: {response.status_code}")
            except:
                st.error("Connection error!")
    else:
        st.warning("Pehle scene toh likhein!")
