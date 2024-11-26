import sys

def validate_data(heights_lst, weights_lst):
    """validate if data i the right type and comes by pairs

    Args:
        heights_lst (list[int | float]): heights
        weights_lst (list[int | float]): weights
    """
    try:
        if len(heights_lst) != len(weights_lst):
            assert False, "Lists most have the same amount of elements"
        for i in range(0, len(heights_lst)):
            if (
                isinstance(heights_lst[i], int | float) is False or \
                isinstance(weights_lst[i], int | float) is False
            ):
                assert False, "Invalid data type"
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        sys.exit()


def give_bmi(
        height: list[int | float], weight: list[int | float]
    ) -> list[int | float]:
    """calcule BMI's with the data of the params

    Args:
        height (list[int  |  float]): height
        weight (list[int  |  float]): weight

    Returns:
        list[int | float]: BMI's
    """
    validate_data(height, weight)
    ret = [
        weight[i] / height[i]**2
        for i in range(0, len(height))
        ]

    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ret = [item > limit for item in bmi]
    return ret
