import gradio as gr

# Ye model bilkul free hai aur koi key nahi maangta
def generate_horror(prompt):
    try:
        # Hugging Face ka direct free server
        client = gr.load("models/black-forest-labs/FLUX.1-schnell")
        return client(prompt)
    except Exception as e:
        return "System thora busy hai, 1 minute baad dobara Submit dabayein."

demo = gr.Interface(
    fn=generate_horror, 
    inputs=gr.Textbox(label="Describe your horror scene"), 
    outputs="image",
    title="Amn-Sky Pro (Free Version)"
)

demo.launch()
