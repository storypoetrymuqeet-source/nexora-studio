import streamlit as st

# --- NEXORA STUDIO ULTIMATE ---
st.set_page_config(page_title="Nexora Studio", layout="centered", page_icon="🎬")

st.title("🎬 Nexora AI Studio")
st.markdown("---")

prompt = st.text_input("Apni video ya image ka scene likhein:", value="A scary ghost in a dark forest")

if st.button("📽️ Generate Result"):
    if prompt:
        with st.spinner("Nexora Engine kaam kar raha hai..."):
            # Clean URL for better loading
            clean_prompt = prompt.replace(' ', '+')
            image_url = f"https://pollinations.ai/p/{clean_prompt}?width=1024&height=1024&model=flux"
            
            # 1. Image dikhane ki koshish
            st.image(image_url, caption=f"Result: {prompt}")
            
            # 2. Agar image load na ho toh direct link
            st.markdown(f"🔗 [Agar image nazar nahi aa rahi toh yahan click karein]({image_url})")
            st.success("Nexora Studio ne result tayyar kar diya hai!")
    else:
        st.warning("Pehle scene likhein!")

st.markdown("---")
st.caption("Created by Azkir | Nexora AI")
