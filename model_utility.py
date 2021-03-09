import numpy as np
import matplotlib.pyplot as plt
from numpy.random import MT19937, RandomState, SeedSequence

def sudoku_as_images(sudoku_arr, nrows = 1, ncols = 4, figsize = (16, 4), cmap = 'gray', annot = True, annot_color = 'red'):
    plt.subplots(nrows = nrows, ncols = ncols, figsize = figsize)

    for i in range(len(sudoku_arr)):
        plt.subplot(nrows, ncols, i + 1)
        plt.axis(False)
        plt.grid(False)
        plt.imshow(sudoku_arr[i], cmap = cmap)

        if annot:
            min_val, max_val = 0, 9
            ind_array = np.arange(min_val, max_val, 1.0)
            x, y = np.meshgrid(ind_array, ind_array)

            for x_val, y_val in zip(x.flatten(), y.flatten()):
                plt.text(x_val, y_val, int(sudoku_arr[i][int(y_val)][int(x_val)] * 9), va='center', ha='center', color = annot_color)

    plt.show()

def shuffle_together(arrays, random_state):
    for arr in arrays:
        rs = np.random.RandomState(random_state)
        rs.shuffle(arr)