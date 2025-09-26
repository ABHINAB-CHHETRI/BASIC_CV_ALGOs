import numpy as np
from PIL import Image
#JUST CHECKING COMMIT
def increase_brightness(image, value):
    try:
        # Convert image pixels to int16 to avoid overflow during addition
        img_int = image.astype(np.int16)

        # Add the brightness value to all pixels
        img_bright = img_int + value

        # Clip the result to [0, 255] to fit into valid pixel value range
        img_bright = np.clip(img_bright, 0, 255)

        # Convert back to uint8
        return img_bright.astype(np.uint8)
    except Exception as e:
        print("Error while increasing brightness:", e)
        return image
    
try:
    # Open the image file
    img = Image.open("input.jpg")
except FileNotFoundError:
    print("Error: input.jpg not found.")
    exit()
except Exception as e:
    print(f"Error opening image: {e}")
    exit()

try:
    # Convert image to numpy array
    img_np = np.array(img)

    # Increase brightness by 50
    bright_img_np = increase_brightness(img_np, 50)

    # Convert back to PIL Image
    bright_img = Image.fromarray(bright_img_np)

    # Save and show the result
    bright_img.save("brightened.jpg")
    bright_img.show()
except Exception as e:
    print("Error during image processing:", e)
