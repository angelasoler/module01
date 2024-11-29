import matplotlib.pyplot as plt
from numpy import array


def ft_load(path: str) -> array:
    """loads a image on an array and returns it

    Args:
        path (str): path where image is

    Returns:
        np.array: image
    """
    try:
        img = plt.imread(path)
        print(f"The shape of image is: {img.shape}")
        return img
    except Exception as e:
        print(f"Error: {e}")
