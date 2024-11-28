from PIL import Image
from numpy import array
# from zoom import ft_zoom


def ft_load(path: str) -> Image:
    """loads a image on an Image object and returns it

    Args:
        path (str): path where image is

    Returns:
        Image: image
    """
    try:
        with Image.open(path) as image:
            image.load()
        print(f"The shape of image is: {array(image).shape}")
        gray_image = image.convert('L')
        # new_image = ft_zoom(array(gray_image), 400, 400)
        print(f"New shape after slicing: {array(gray_image).shape}")
        gray_image.show()
        return gray_image
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ft_load("animal.jpeg")