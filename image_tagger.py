from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser


def prompt_func(data):
    text = data["text"]
    image = data["image"]

    image_part = {
        "type": "image_url",
        "image_url": f"data:image/jpeg;base64,{image}",
    }

    content_parts = []

    text_part = {"type": "text", "text": text}

    content_parts.append(image_part)
    content_parts.append(text_part)

    return [HumanMessage(content=content_parts)]


def invoke_model(image_b64):

    llm = ChatOllama(model="moondream", temperature=0)

    chain = prompt_func | llm | StrOutputParser()

    query_chain = chain.invoke(
        {"text": "Describe this image", "image": image_b64}
    )
    
    return str(query_chain)


def test():
    from PIL import Image
    from utils.image import convert_to_base64
    file_path = "/Users/vishnudev/Pictures/Barcelona Buildings Street.jpg"
    pil_image = Image.open(file_path)
    image_b64 = convert_to_base64(pil_image)
    invoke_model(image_b64)


if __name__ == "__main__":
    test()
    