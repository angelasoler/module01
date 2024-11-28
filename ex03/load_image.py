import matplotlib.pyplot as plt
from PIL import Image
from numpy import array
from zoom import ft_zoom


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
        return image
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(array(image))
    gray_image = image.convert('L')
    zoom_image = ft_zoom(array(gray_image))
    print(f"New shape after slicing: {zoom_image.shape}")
    print(zoom_image)
    plt.figure()
    plt.imshow(zoom_image, cmap='gray')
    plt.savefig('ret_img.png')
