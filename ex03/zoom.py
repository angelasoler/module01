import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from load_image import ft_load


def ft_zoom(img: array):
    """
        make a zoom on a part of an image
    """
    try:
        zoom_image = np.mean(img[100:500, 450:850], axis=2)
        print(f"New shape after slicing: {zoom_image.shape}")
        print(zoom_image.astype(np.uint8))
        plt.figure()
        plt.imshow(zoom_image, cmap='gray')
        plt.savefig('ret_img.png')
    except Exception:
        print("Erro: Zooming fail")


if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(array(image))
    ft_zoom(array(image))
