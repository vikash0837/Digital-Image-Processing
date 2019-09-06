import cv2
from assignment_3_qn_1 import DFT_2D_FROM_1D
from assignment_3_qn_2 import IDFT_2D_FROM_1D
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

image_a = cv2.imread("data/ImagesForAssignment3/Amitabh.jpg", 0)
image_r = cv2.imread("data/ImagesForAssignment3/Rajinikanth.jpg", 0)
print(" image1 shape:",image_a.shape)
print("image 2 shape:", image_r.shape)


def ifft_from_fft(fft):
    obj = DFT_2D_FROM_1D()
    conj_fft = np.conjugate(fft)
    fft_on_conj = obj.dft_2d_from_1d(conj_fft,conj_fft.shape[0])
    ifft = (1/(fft_on_conj.shape[0]*fft_on_conj.shape[1])*np.conjugate(fft_on_conj))
    return ifft


def plot_magnitude_phase_response(image1, image2, swap1,swap2, t1, t2, t3,t4):
    """
    :param image:
    :param magnitude_response:
    :param phase_response:
    :return:
    """
    gs = gridspec.GridSpec(2, 4)
    gs.update(wspace=0.5)
    ax3 = plt.subplot(gs[1, :2], )
    ax4 = plt.subplot(gs[1, 2:])
    ax1 = plt.subplot(gs[0, :2])
    ax2 = plt.subplot(gs[0, 2:])
    plt.subplots_adjust(left=0.3)

    ax1.imshow(image1, cmap='gray')
    ax1.set(title=t1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.imshow(image2, cmap='gray')
    ax2.set(title=t2)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax3.imshow(swap1, cmap='gray')
    ax3.set(title=t3)
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax4.imshow(swap2, cmap='gray')
    ax4.set(title=t4)
    ax4.set_xticks([])
    ax4.set_yticks([])
    plt.show()


dft_obj = DFT_2D_FROM_1D()
fft_1 = dft_obj.dft_2d_from_1d(image_a, image_a.shape[0])
fft_2 = dft_obj.dft_2d_from_1d(image_r, image_r.shape[0])
magnitude_response_1 = np.abs(fft_1)
magnitude_response_2 = np.abs(fft_2)
phase_response_1 = np.angle(fft_1)
phase_response_2 = np.angle(fft_2)

#idft_obj = IDFT_2D_FROM_1D()
fft_swap_1 = magnitude_response_1 * np.exp(1j*phase_response_2)
#swap1 = idft_obj.idft_2d(fft_swap_1,fft_swap_1.shape[0])
swap1 = ifft_from_fft(fft_swap_1)
fft_swap_2 = magnitude_response_2 * np.exp(1j*phase_response_1)
#swap2 = idft_obj.idft_2d(fft_swap_2,fft_swap_2.shape[0])
swap2 = ifft_from_fft(fft_swap_2)
t1 = "IMAGE 1"
t2 = "IMAGE 2"
t3 = "OUTPUT - SWAP 1"
t4 = "OUTPUT - SWAP 2"
plot_magnitude_phase_response(image_a, image_r, np.abs(swap1),np.abs(swap2), t1, t2, t3, t4)




