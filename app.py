import gradio as gr
from diffusers import DiffusionPipeline
import torch

# Ye model fast images ke liye hai
pipe = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7", torch_dtype=torch.float32)

def generate(prompt):
    # Sirf 4 steps mein image banegi (tez!)
    image = pipe(prompt=prompt, num_inference_steps=4, guidance_scale=8).images[0]
    return image

demo = gr.Interface(fn=generate, inputs="text", outputs="image")
demo.launch()
