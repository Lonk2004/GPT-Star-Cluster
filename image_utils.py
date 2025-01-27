import numpy as np 
from PIL import Image
import base64
from io import BytesIO
def apply_arcsinh_scaling(data, scale_factor=0.01):
    # Normalize the data to [0, 1]
    data = data - np.min(data)  # Shift data to start from 0
    data = data / np.max(data)  # Normalize to [0, 1]

    # Apply arcsinh scaling
    scaled_data = np.arcsinh(scale_factor * data)

    # Normalize again to [0, 255] for image encoding
    scaled_data = scaled_data / np.max(scaled_data)  # Normalize to [0, 1]
    scaled_data = (scaled_data * 255).astype(np.uint8)  # Convert to 8-bit
    return scaled_data

def encode_image_to_base64(data, scale_factor=0.01):
    """
    Apply arcsinh scaling and encode the image as Base64.
    """
    # Apply arcsinh scaling
    scaled_data = apply_arcsinh_scaling(data, scale_factor)

    # Convert scaled data to an image
    image = Image.fromarray(scaled_data)
    image = image.resize((128,128), Image.Resampling.LANCZOS)

    # Save the image to a BytesIO object
    buffered = BytesIO()
    image.save(buffered, format="PNG")

    # Encode the BytesIO object as Base64
    base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return base64_image