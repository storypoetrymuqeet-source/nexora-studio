import streamlit as st

# --- NEXORA STUDIO FINAL ---
st.set_page_config(page_title="Nexora Studio", layout="centered", page_icon="🎬")

st.title("🎬 Nexora AI Studio")
st.markdown("---")

# User Input
prompt = st.text_input("Apni video ya image ka scene likhein:", value="A scary ghost in a dark forest")

if st.button("📽️ Generate Result"):
    if prompt:
        with st.spinner("Nexora Engine kaam kar raha hai..."):
            # Sab se asaan aur mazboot rasta
            image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=123&model=flux"
            
            # Result dikhane ke liye
            st.image(image_url, caption=f"Nexora Result: {prompt}", use_container_width=True)
            st.success("Mubarak ho Azkir! Connection 100% kamyab raha.")
    else:
        st.warning("Pehle scene toh likhein!")

st.markdown("---")
st.caption("Created by Azkir | Powered by Nexora Engine")
