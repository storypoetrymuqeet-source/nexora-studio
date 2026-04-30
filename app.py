import streamlit as st

# Page ki settings
st.set_page_config(page_title="Nexora Flash Studio", page_icon="🎨")

st.title("Nexora Flash Studio 🎨")
st.write("Apni soch ko tasveer mein badlein!")

# Image generation function (No Token Needed!)
def generate_image(prompt):
    # Pollinations AI link jo direct image banata hai
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
    return url

# User input
prompt = st.text_input("Yahan description likhein (English mein):", placeholder="e.g. A cute 3D Pixar style cat")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Nexora aapki image bana raha hai..."):
            image_url = generate_image(prompt)
            st.image(image_url, caption=f"Result for: {prompt}", use_container_width=True)
            st.success("Aapki image taiyar hai!")
    else:
        st.warning("Pehle kuch likhen toh sahi!")
