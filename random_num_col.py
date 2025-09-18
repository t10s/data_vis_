import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

####################################################################################
# 1. first part just playing around with randomly coloured pixels
# 2. second part is randomly coloured darth vader
####################################################################################

# generate a plot with random coloured pixels. 
# first generate an array of random numbers in the required pixel x pixel size and map numbers to each of the unique digits
# create an empty image
# loop through the pixel x pixel grid to get the digit key and the colour value

# generate an array of random nums between 0-9
nums = np.random.randint(0, 10, size=32*32)

# assign a colour to each digit from 0-9
colours = {
    0: (255, 0, 0),     # Red
    1: (0, 255, 0),     # Green
    2: (0, 0, 255),     # Blue
    3: (255, 255, 0),   # Yellow
    4: (255, 0, 255),   # Magenta
    5: (0, 255, 255),   # Cyan
    6: (128, 0, 128),   # Purple
    7: (255, 165, 0),   # Orange
    8: (128, 128, 128), # Gray
    9: (0, 0, 0),       # Black
}
# make the nums into a 32x32 grid
grid = nums.reshape((32, 32))

# create an array
rgb_grid = np.zeros((32, 32, 3), dtype=np.uint8) # created a 32x32 grid with 3 value, and each value an 8-bit int. initialized to starting value 0

# loop through the grid, i.e. pixels and assign a colour
for y in range(32):
    for x in range(32):
        if grid[y, x] % 2 != 0:
            rgb_grid[y, x] = colours[grid[y, x]]
        else:
            rgb_grid[y, x] = [255, 255, 255]

# show image
plt.figure(figsize=(6,6))
plt.imshow(rgb_grid)
plt.axis('off')
plt.show()


# now try a symmetric pattern. create only half the grid, and then flip it
# set grid size - keep 32*32 like above
size = 32

# create half the grid
half_grid = np.random.randint(0, 10, size=(size, size//2))

# mirror the grid
# np.fliplr flips and array left-right
# hstack is a like horizontal bind
full_grid = np.hstack([half_grid, np.fliplr(half_grid)])

# make the colour grid
rgb_half = np.zeros((size, size, 3), dtype=np.uint8)

# loop through the grid, i.e. pixels and assign a colour only for even numbers
#for y in range(size):
#    for x in range(size):
#        if grid[y, x] % 2 != 0:
#            rgb_half[y, x] = colours[full_grid[y, x]]
#        else:
#            rgb_half[y, x] = [255, 255, 255]

# colour all
for y in range(size):
    for x in range(size):
        rgb_half[y, x] = colours[full_grid[y, x]]

# show image
plt.figure(figsize=(6,6))
plt.imshow(rgb_half)
plt.axis('off')
plt.show()

#==============================================================================================#
####################### now try to randomly colour the darth vader image #######################
#==============================================================================================#

# read in the image as img
# change to greyscale
img = img.convert("L")

# convert the image to an array
img_array = np.array(img)

# display the original image
plt.imshow(img_array, cmap="grey")
plt.axis("off")

# resize the image
new_size = (134, 134) # only probe rts
#new_size = (189, 189) # prime and probe rts

img_resized = img.resize(new_size, Image.NEAREST)

img_array_resize = np.array(img_resized)

plt.imshow(img_array_resize, cmap="grey")
plt.axis("off")

# define threshold for black vs. white
threshold = 128
black_pixels = img_array_resize < threshold
white_pixels = img_array_resize > threshold

black_pixels_total = np.sum(black_pixels)
white_pixels_total = np.sum(white_pixels)

# make radom int arrays for the black and white pixels
black_nums = np.random.randint(0, 10, size=black_pixels_total)
white_nums = np.random.randint(0, 10, size=white_pixels_total)

# assign colours
black_colors = {
    0: [255, 0, 0],    # Red
    1: [0, 255, 0],    # Green
    2: [0, 0, 255],    # Blue
    3: [255, 255, 0],  # Yellow
    4: [255, 0, 255],  # Magenta
    5: [0, 255, 255],  # Cyan
    6: [128, 0, 128],  # Purple
    7: [255, 165, 0],  # Orange
    8: [0, 128, 0],    # Dark Green
    9: [128, 128, 128] # Gray
}

white_colors = {
    0: [200, 200, 200],
    1: [200, 200, 200],
    2: [180, 180, 180],
    3: [180, 180, 180],
    4: [160, 160, 160],
    5: [160, 160, 160],
    6: [140, 140, 140],
    7: [140, 140, 140],
    8: [120, 120, 120],
    9: [120, 120, 120]
}

# create the coloured image
rgb_img = np.zeros((img_array_resize.shape[0], img_array_resize.shape[1], 3), dtype=np.uint8)

# counters
black_idx = 0
white_idx = 0

# do the fun stuff
for x in range(img_array_resize.shape[0]):
    for y in range(img_array_resize.shape[1]):
        if black_pixels[x, y]:
            num = black_nums[black_idx]
            rgb_img[x, y] = black_colors[num]
            black_idx = black_idx+1
        else:
            num = white_nums[white_idx]
            rgb_img[x,y]= white_colors[num]
            white_idx = white_idx+1

# show image
plt.figure(figsize=(8,8))
plt.imshow(rgb_img)
plt.axis("off")
