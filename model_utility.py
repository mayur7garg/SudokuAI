import matplotlib.pyplot as plt

def sudoku_as_images(sudoku_arr, nrows = 1, ncols = 4, figsize = (16, 4), cmap = 'gray'):
    plt.subplots(nrows = nrows, ncols = ncols, figsize = figsize)

    for i in range(len(sudoku_arr)):
        plt.subplot(nrows, ncols, i + 1)
        plt.imshow(sudoku_arr[i], cmap = cmap)

    plt.show()