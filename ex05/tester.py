from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red, ft_blue, ft_invert, ft_green, ft_grey
import matplotlib.pyplot as plt
...
array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
