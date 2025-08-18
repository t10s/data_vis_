import numpy as np
import matplotlib.pyplot as plt

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
rgb_grid = np.zeros((32, 32, 3), dtype=np.uint8)

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
full_grid = np.hstack([half_grid, np.fliplr(half_grid)])

# make the colour grid
rgb_half = np.zeros((size, size, 3), dtype=np.uint8)

# loop through the grid, i.e. pixels and assign a colour
for y in range(32):
    for x in range(32):
        #if grid[y, x] % 2 != 0:
            rgb_half[y, x] = colours[full_grid[y, x]]
        #else:
            rgb_half[y, x] = [255, 255, 255]

# show image
plt.figure(figsize=(6,6))
plt.imshow(rgb_half)
plt.axis('off')
plt.show()

