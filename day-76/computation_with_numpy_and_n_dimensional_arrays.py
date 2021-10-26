import numpy as np

import matplotlib.pyplot as plt
from scipy import misc # contains an image of a racoon!
from PIL import Image # for reading image files

"""#### 1-Dimensional Arrays (Vectors)"""

# Create new ndarray from scatch
my_array = np.array([1.1, 9.2, 8.1, 4.7])

# Show rows and columns
my_array.shape

# Accessing elements by index
my_array[2]

# Show dimensions of an array
my_array.ndim

"""#### 2-Dimensional Arrays (Matrices)"""

array_2d = np.array([[1, 2, 3, 9], 
                     [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

# Access the 3rd value in the 2nd row
array_2d[1,2]

# Access all the values in the first row
array_2d[0, :]

"""#### N-Dimensional Arrays (Tensors)

"""

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

print(f'We have {mystery_array.ndim} dimensions')
print(f'The shape is {mystery_array.shape}')

# Axis 0: 3rd element. Axis 1: 2nd Element. Axis 3: 4th Element
mystery_array[2, 1, 3]

# Retrieve all the elements on the 3rd axis that are at
# position 2 on the first axis and position 1 on the second axis.
mystery_array[2, 1, :]

# All the first elements on axis number 3
mystery_array[:, :, 0]

"""# NumPy Mini-Challenges"""

a = np.arange(10,30)
print(a)

# last 3 values
a[-3:]

# interval of values
a[3:6]

# all the values except the first 12
a[12:]

# every second value (all the even numbers)
a[::2]

np.flip(a)

a[::-1]

"""# Linear Algebra with Vectors"""

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

v1 + v2

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]

list1 + list2

v1 * v2

"""# Broadcasting and Scalars

"""

array_2d = np.array([[1, 2, 3, 4], 
                     [5, 6, 7, 8]])

print(f'Dimensions: {array_2d.ndim}')
print(f'Shape: {array_2d.shape}')

array_2d + 10

array_2d * 5

"""# Matrix Multiplication with @ and .matmul()

<img src=https://i.imgur.com/LCdhmi8.png width=350>
"""

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

c = np.matmul(a1, b1)
print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.')
c

a1 @ b1

"""# Manipulating Images as ndarrays

"""

img = misc.face()

plt.imshow(img)

img

type(img)

img.shape

img.ndim

"""
* Divide all the values by 255 to convert them to sRGB, where all the values are between 0 and 1. 
* Next, multiply the sRGB array by the `grey_vals` to convert the image to grey scale. 
* Finally use Matplotlib's [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) together with the colormap parameter set to gray `cmap=gray` to look at the results. """

grey_vals = np.array([0.2126, 0.7152, 0.0722])

sRGB_array = img / 255

img_gray = sRGB_array @ grey_vals
# or use
img_gray = np.matmul(sRGB_array, grey_vals)

plt.imshow(img_gray, cmap='gray')

plt.imshow(img_gray)

"""1) You flip the grayscale image upside down


2) Rotate the colour image


3) Invert (i.e., solarize) the colour image. To do this you need to converting all the pixels to their "opposite" value, so black (0) becomes white (255).

#### Challenge Solutions
"""

a1

np.flip(a1)

plt.imshow(np.flip(img_gray), cmap='gray')

print(a1)
print('a1 array rotated:')
np.rot90(a1)

plt.imshow(np.rot90(img))

solar_img = 255 - img
plt.imshow(solar_img)