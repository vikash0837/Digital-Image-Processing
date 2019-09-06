import numpy as np
import cv2
from assignment_3_qn_1 import DFT_2D_FROM_1D
from assignment_3_qn_2 import IDFT_2D_FROM_1D


def q1():
    class_obj = DFT_2D_FROM_1D()
    image = cv2.imread("data/ImagesForAssignment3/zoneplate.png", 0)
    print("[INFO] Image Shape is =:", image.shape)
    fft = class_obj.dft_2d_from_1d(image, image.shape[0])
    print("[INFO] Computed FFT Shape is =:", fft.shape)
    magnitude_response = 20 * np.log(1 + np.abs(fft))
    phase_response = np.angle(fft)
    title_1 = "ZONE PLATE IMAGE"
    title_2 = "2-D DFT MAGNITUDE"
    title_3 = "2-D DFT PHASE"
    class_obj.plot_magnitude_phase_response(image, magnitude_response, phase_response, title_1, title_2, title_3)

def ifft_from_fft(fft):
    obj = DFT_2D_FROM_1D()
    conj_fft = np.conjugate(fft)
    fft_on_conj = obj.dft_2d_from_1d(conj_fft,conj_fft.shape[0])
    ifft = (1/(fft_on_conj.shape[0]*fft_on_conj.shape[1])*np.conjugate(fft_on_conj))
    return ifft
def q2():
    image = cv2.imread("data/ImagesForAssignment3/Luna.png", 0)
    print("[INFO] original Imaged Shape =:", image.shape)
    # fft = np.fft.fft2(image)
    obj = DFT_2D_FROM_1D()
    #obj2 = IDFT_2D_FROM_1D()
    fft = obj.dft_2d_from_1d(image, 2 * image.shape[0])
    reconstructed_image = ifft_from_fft(fft)
    print("[INFO] Reconstructed Imaged Shape =:", reconstructed_image.shape)
    magnitude_response = np.abs(reconstructed_image)
    #phase_response = np.angle(reconstructed_image)
    if fft.shape[0] > image.shape[0]:
        error = np.abs(image - magnitude_response[0:image.shape[0],0:image.shape[1]])
    else:
        error = np.abs(image - magnitude_response)
    title_1 = "LUNA IMAGE"
    title_2 = "RECONSTRUCTED LUNA IMAGE"
    title_3 = "ERROR IMAGE"
    obj.plot_magnitude_phase_response(image, magnitude_response, error, title_1, title_2, title_3)
q2()
#q1()
