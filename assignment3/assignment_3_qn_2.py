import numpy as np
import cv2
from assignment_3_qn_1 import DFT_2D_FROM_1D

class IDFT_2D_FROM_1D:
    def __init__(self):
        print("[Class Info] IDFT_2D_FROM_1D class info")
    def idft_2d(self, dft_2d, filter_size):
        """

        :param dft_2d:
        :return:
        """
        inverse_transform = np.empty((filter_size, filter_size), dtype=np.complex128)
        for row in range(filter_size):
            inverse_transform[row, 0:filter_size] = np.fft.ifft(np.fft.fftshift(dft_2d[row, 0:filter_size]))
        final_inverse_transform = np.empty(dft_2d.shape, dtype=np.complex128)
        for col in range(filter_size):
            final_inverse_transform[0:filter_size, col] = np.fft.ifft(np.fft.fftshift(inverse_transform[0:filter_size, col]))
        # np.fft.ifft2(dft_2d)
        return final_inverse_transform


