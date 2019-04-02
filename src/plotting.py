import matplotlib.pyplot as plt
import numpy as np



def plot_histogram(DataV = None, NBins = None):
    """
    ARGS:
        DataV : 1D vector of points
        NBins: Number of bins
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
        1. Make more efficient
    """
    minX = min(DataV)
    maxX = max(DataV)
    #dx = (maxX-minX) / NBins
    #binV = np.zeros(NBins)
    #for i in range(bin
    plt.hist(DataV, bins=NBins, density=True)       ## bins = (N_in_bin) / (dx * N_total)
    plt.ylabel('Probability');
    plt.show()
