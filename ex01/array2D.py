import numpy as np
import sys


def validate_args(lst) -> np.array:
    """validate slice_me funct arguments

    Args:
        lst (list): de argument to be validated

    Returns:
        np.array: the array from lst if validations passed, if not exit
    """
    try:
        assert isinstance(lst, list), "family param most be list type"
        array = np.array(lst)
        assert len(array.shape) == 2, "Invalid array shape"
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
    return array


def slice_me(family: list, start: int, end: int) -> list:
    """ truncates the input 2D array by slicing rows based
    on the given indices (start and end) and recalculates
    the shape after slicing

    Args:
        family (list): 2D list
        start (int): index
        end (int): index

    Returns:
        list: the list resulting from the trunc
    """
    array = validate_args(family)

    print(f"My shape is : {array.shape}")
    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
