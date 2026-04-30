import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

# Page Config
st.set_page_config(page_title="Nexora AI Studio", layout="wide")
st.title("🎨 Nexora Flash: Image & Video Studio")

# Model Loading with Memory Optimization
@st.cache_resource
def load_model():
    model_id = "stablediffusionapi/sequential-stable-diffusion"
    # Ye setting mobile par app ko crash hone se bachayegi
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
    )
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
        # Memory bachane ke liye optimized settings
        pipe.enable_attention_slicing()
        pipe.enable_sequential_cpu_offload()
    return pipe

try:
    pipe = load_model()
    st.success("System Ready! ✅")
except Exception as e:
    st.info("System initializing... Please wait a moment.")

# Input Area
prompt = st.text_input("Yahan apni image ka idea likhein (English mein):")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Tasveer ban rahi hai..."):
            # Image generation
            image = pipe(prompt).images[0]
            st.image(image, caption="Nexora AI Result")
            st.success("Image Tayyar Hai!")
    else:
        st.warning("Meharbani karke pehle kuch likhein.")

st.sidebar.markdown("### Version 1.1 (Market Ready)")
st.sidebar.info("Ye tool Image aur Video dono ke liye design kiya gaya hai.")
