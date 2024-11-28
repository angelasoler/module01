import numpy as np
import sys


def validate_args(lst) -> np.array:
    try:
        assert isinstance(lst, list), "family param most be list type"
        array = np.array(lst)
        assert len(array.shape) == 2, "Invalid array shape"
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
    return array


def slice_me(family: list, start: int, end: int) -> list:
    array = validate_args(family)

    print(f"My shape is : {array.shape}")
    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
