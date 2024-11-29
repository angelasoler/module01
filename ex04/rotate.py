import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from load_image import ft_load


def ft_rotate(img: array):
    """
        rotates an image
    """
    trans_lst = [[img[j][i]
                  for j in range(len(img))] for i in range(len(img[0]))]
    trans_img = array(trans_lst)
    print(f"New shape after Transpose: {trans_img.shape}")
    print(trans_img.astype(np.uint8))
    plt.figure()
    plt.imshow(trans_img, cmap='gray')
    plt.savefig('ret_img.png')


def ft_zoom(img: array) -> array:
    """
        make a zoom on a part of an image
    """
    try:
        zoom_image = np.mean(img[100:500, 450:850], axis=2)
        print(f"The shape of image is: {zoom_image.shape}")
        print(zoom_image.astype(np.uint8))
        return zoom_image
    except Exception:
        print("Erro: Zooming fail")


if __name__ == "__main__":
    image = ft_load("../ex03/animal.jpeg")
    zoom_image = ft_zoom(image)
    ft_rotate(zoom_image)
