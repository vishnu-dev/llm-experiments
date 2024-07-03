import base64
from io import BytesIO
from PIL import Image


def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


if __name__ == "__main__":
    file_path = "/Users/vishnudev/Pictures/Plitvice Main Waterfall.png"
    pil_image = Image.open(file_path)
    image_b64 = convert_to_base64(pil_image)
    print(image_b64)