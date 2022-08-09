import functools
import itertools
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=10, seed=1)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

print('min:', functools.reduce(min, itertools.chain.from_iterable(pic)))
print('max:', functools.reduce(max, itertools.chain.from_iterable(pic)))

plt.imshow(pic, cmap='gray')
plt.show()
