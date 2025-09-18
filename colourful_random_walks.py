import numpy as np
import matplotlib.pyplot as plt

# first just make some simple random walks
def data_walk_art(width, height, data, walkers = 60): # change number of walkers, etc. as required
    steps_per_walker = len(data) // walkers
    canvas = np.zeros((height, width, 3), dtype=float)

    # compass directions (y, x) y = row index and x = column index. e.g., (1, -1) = move one row down, and one column left
    dirs = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]

    cols = [
    [1.0, 0.0, 0.0],   # red
    [0.0, 0.0, 1.0],   # blue
    [0.0, 1.0, 0.0],   # green
    [1.0, 1.0, 1.0],   # white
    [0.5, 0.0, 0.5],   # purple
    [1.0, 1.0, 0.0],   # yellow
    [1.0, 0.75, 0.8],  # pink
    [1.0, 0.5, 0.0],   # orange
    [0.5, 0.5, 0.5],   # grey
    [0.0, 1.0, 1.0]    # cyan
    ]

    idx = 0
    idx_c = 0
    for w in range(walkers):
        x, y = np.random.randint(0, width), np.random.randint(0, height)
        #color = np.random.rand(3)
        color = np.array(cols[idx_c])
        idx_c = idx_c + 1
        if idx_c >= 10:
            idx_c = 0

        for s in range(steps_per_walker):
            val = data[idx]
            idx = idx + 1

            if 0 <= x < width and 0 <= y < height: # if y and y are smaller than the height but at least zero
                # blend in with intensity based on val
                intensity = (val + 1) / 10.0 # converts 0-9 to 0.1 to 1.0
                canvas[y, x] = canvas[y, x] * (1 - 0.2*intensity) + color * (0.2*intensity) # how intense the colur is, higher values == more intense

            # map value to step direction
            if val < 8:
                dx, dy = dirs[val]
            else:
                dx, dy = np.random.choice([-1,0,1]), np.random.choice([-1,0,1])

            # optional: step length depends on value
            step_len = 1 + val // 5  # 0–4 → 1 step, 5–9 → 2 steps
            x = np.clip(x + dx * step_len, 0, width-1) # compute the step length i.e. direction * step_len, the last two args keep the walker from leaving the canvas
            y = np.clip(y + dy * step_len, 0, height-1)

    return canvas

# Example: 72k data points
width, height = 240, 300  # ~72k pixels
data = np.random.randint(0, 10, size=72000)  # <-- replace with your real data

img = data_walk_art(width, height, data, walkers=60)

plt.imshow(img)
plt.axis("off")
plt.show()














