import streamlit as st

# --- NEXORA STUDIO NO-TOKEN VERSION ---
st.set_page_config(page_title="Nexora Studio", layout="centered")
st.title("🎬 Nexora AI Studio")

prompt = st.text_input("Apni video ka scene likhein:", value="A scary ghost")

if st.button("Generate Result"):
    if prompt:
        with st.spinner("Nexora Engine image dhoond raha hai..."):
            # Hum seedha URL use kar rahe hain taake 404 ka khatra hi na rahe
            image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}"
            st.image(image_url, caption="Nexora Studio Result")
            st.success("Mubarak ho Azkir! Result aa gaya.")
    else:
        st.warning("Pehle kuch likhein!")
        
