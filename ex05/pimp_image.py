import numpy as np
from numpy import array
from PIL import Image


def ft_invert(array) -> array:
    """applies a filter to an image

    Args:
        array (array):the a array of the image to apply the filter

    Returns:
        array: an image with the filter
    """
    Image.fromarray(255-array).show()
    return 255 - array


def ft_red(array) -> array:
    """applies a filter to an image

    Args:
        array (array):the a array of the image to apply the filter

    Returns:
        array: an image with the filter
    """
    filtered_image = array.copy()
    filtered_image[:, :, 1] = 0
    filtered_image[:, :, 2] = 0
    Image.fromarray(filtered_image).show()
    return filtered_image


def ft_green(array) -> array:
    """applies a filter to an image

    Args:
        array (array):the a array of the image to apply the filter

    Returns:
        array: an image with the filter
    """
    filtered_image = array.copy()
    filtered_image[:, :, 0] = 0
    filtered_image[:, :, 2] = 0
    Image.fromarray(filtered_image).show()
    return filtered_image


def ft_blue(array) -> array:
    """applies a filter to an image

    Args:
        array (array):the a array of the image to apply the filter

    Returns:
        array: an image with the filter
    """
    filtered_image = array.copy()
    filtered_image[:, :, 0] = 0
    filtered_image[:, :, 1] = 0
    Image.fromarray(filtered_image).show()
    return filtered_image


def ft_grey(array) -> array:
    """applies a filter to an image

    Args:
        array (array):the a array of the image to apply the filter

    Returns:
        array: an image with the filter
    """
    gray_image = (0.2989 * array[:, :, 0] +
                  0.5870 * array[:, :, 1] +
                  0.1140 * array[:, :, 2]).astype(np.uint8)
    Image.fromarray(gray_image).show()
    return gray_image
