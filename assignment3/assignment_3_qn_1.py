import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.gridspec as gridspec

class DFT_2D_FROM_1D:
    def __init__(self):
        print("[INFO] DFT Class initiated:")
    def dft_2d_from_1d(self,input_image, filter_size):
        """
        :param image:
        :param filteer_size:
        :return: fft_transform: in complex form
        """

        if input_image.shape[0] > filter_size:
            fft_transform = np.empty(input_image.shape,dtype=complex)
            n_cols = input_image.shape[1]//filter_size
            for i in range(input_image.shape[0]):
                for j in range(n_cols):
                    fft = np.fft.fft(input_image[i, j*filter_size:j*filter_size + filter_size])
                    #print("[Check] Size of fft row", fft.shape)
                    #fshift = np.fft.fftshift(fft)
                    fshift = fft
                    fft_transform[i,j*filter_size:j*filter_size + filter_size] = fshift
            input_image = fft_transform

            n_rows = input_image.shape[0] // filter_size
            for i in range(input_image.shape[1]):
                for j in range(n_rows):
                    fft = np.fft.fft(input_image[j*filter_size:j*filter_size + filter_size, i])
                    #print("[Check] Size of fft col", fft.shape)
                    fshift = fft
                    #fshift = np.fft.fftshift(fft)
                    fft_transform[j*filter_size:j*filter_size + filter_size, i] = fshift
        else:
            fft_transform = np.empty(input_image.shape, dtype=np.complex128)
            for i in range(input_image.shape[0]):
                fft = np.fft.fft(input_image[i,:])
                #print("[Check] Size of fft row",fft.shape)
                fshift = fft
                #fshift = np.fft.fftshift(fft)
                fft_transform[i:] = fshift
            input_image = fft_transform
            for i in range(input_image.shape[1]):
                fft = np.fft.fft(input_image[:,i])
                #print("[Check] Size of fft column",fft.shape)
                fshift = fft
                #fshift = np.fft.fftshift(fft)
                fft_transform[:,i] = fshift
        return fft_transform


    def plot_magnitude_phase_response(self, image, magnitude_response, phase_response,t1,t2,t3):
        """
        :param image:
        :param magnitude_response:
        :param phase_response:
        :return:
        """
        gs = gridspec.GridSpec(2, 4)
        gs.update(wspace=0.5)
        ax2 = plt.subplot(gs[1, :2], )
        ax3 = plt.subplot(gs[1, 2:])
        ax1 = plt.subplot(gs[0, 1:3])
        plt.subplots_adjust(left=0.3)

        ax1.imshow(image, cmap='gray')
        ax1.set(title=t1)
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax2.imshow(magnitude_response, cmap='gray')
        ax2.set(title=t2)
        ax2.set_xticks([])
        ax2.set_yticks([])
        ax3.imshow(phase_response, cmap='gray')
        ax3.set(title=t3)
        ax3.set_xticks([])
        ax3.set_yticks([])
        plt.show()






