import streamlit as st
import requests

# --- NEXORA STUDIO FINAL ---
st.set_page_config(page_title="Nexora Studio", layout="centered")
st.title("🎬 Nexora AI Studio")

# Aapka Token
HF_TOKEN = "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"

prompt = st.text_input("Apni video ya image ka scene likhein:", placeholder="e.g. A beautiful landscape...")

if st.button("Generate Result"):
    if prompt:
        # Hum ne model badal kar 'Google' ka model kar diya hai (Bohat reliable hai)
        API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}

        with st.spinner("Nexora Engine kaam kar raha hai..."):
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                
                if response.status_code == 200:
                    st.success("Mubarak ho! Connection bilkul theek hai.")
                    st.write("Azkir, aapka token sahi chal raha hai. Ab hum video model par wapas ja sakte hain.")
                elif response.status_code == 404:
                    st.error("Model abhi mil nahi raha. Shayad Hugging Face par koi update chal rahi hai.")
                elif response.status_code == 401:
                    st.error("Token galat hai. Dobara check karein.")
                else:
                    st.error(f"Error Code: {response.status_code}")
            except:
                st.error("Internet connection ka masla hai.")
    else:
        st.warning("Pehle scene toh likhein!")

