from numpy import array


def ft_zoom(img: array) -> array:
    """
        return a minor part of an image
    """
    return img[100:500, 450:850]
