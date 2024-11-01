from scipy.signal import convolve2d
import numpy as np

def simple_2d_convolution(input_array, conv_mask):
    """
    Perform 2D convolution on an input array using a convolution mask.

    Parameters:
        input_array (list or np.array): The input numbers array.
        conv_mask (list or np.array): The convolution mask.
    Returns:
        np.array: The convolution result.
    """
    return convolve2d(input_array, conv_mask, mode='full')

input_array2 = np.array([[1,2,3,2], [2,1,1,2], [50,50,55,50],[55,50,50,55]])
conv_mask2 = np.array([[1,1,1], [0, 0, 0], [-1,-1,-1]])
convolution_result2 = simple_2d_convolution(input_array2, conv_mask2)
print("2D Convolution Result:", convolution_result2)
