import gradio as gr
from image_tagger import invoke_model as image_describer
from utils.image import convert_to_base64
from utils.tagger import get_top_tags

def generate_tags(image):
    image_b64 = convert_to_base64(image)
    image_description = image_describer(image_b64)
    print(image_description)
    tags = get_top_tags(image_description)
    return ', '.join(tags)


with gr.Blocks() as demo:
    with gr.Tab("Image Tagger"):
        gr.Interface(generate_tags, gr.Image(type='pil'), "text")

if __name__ == "__main__":
    demo.launch()