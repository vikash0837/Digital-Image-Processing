from assignment_3_qn_1 import DFT_2D_FROM_1D
from assignment_3_qn_2 import IDFT_2D_FROM_1D
import numpy as np
import matplotlib.pyplot as plt
import cv2
import imageio
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.gridspec as gridspec

def ifft_from_fft(fft, filter_size):
    obj = DFT_2D_FROM_1D()
    conj_fft = np.conjugate(fft)
    fft_on_conj = obj.dft_2d_from_1d(conj_fft,filter_size)
    ifft = (1/(fft_on_conj.shape[0]*fft_on_conj.shape[1])*np.conjugate(fft_on_conj))
    return ifft


def q3(img, filter_size_dft, filter_size_idft):
    """
    :param img:
    :param filter_size:
    :return:
    """
    print("[INFO] DFT grid:{0} IDFT grid:{1}".format(filter_size_dft,filter_size_idft))
    dft_obj = DFT_2D_FROM_1D()
    fft = dft_obj.dft_2d_from_1d(img,filter_size_dft)
    # idft_obj = IDFT_2D_FROM_1D()
    # ifft = idft_obj.idft_2d(fft,img.shape[0]//2)
    ifft = ifft_from_fft(fft, filter_size_idft)
    magnitude_response = np.abs(ifft)
    phase_response = np.angle(ifft)
    error = np.abs(img - magnitude_response)
    t1 = "SHEPP-LOGAN PHANTOM"
    t2 =  "RECONSTRUCTED SHEPP-LOGAN IMAGE"
    t3 = "ERROR IMAGE"
    #dft_obj.plot_magnitude_phase_response(img, magnitude_response, error, t1, t2, t3)
    return magnitude_response, error
    #dft_obj.plot_magnitude_phase_response(img,magnitude_response,error, t1, t2, t3)


gif = imageio.mimread("data/ImagesForAssignment3/shepplogan.gif")
nums = len(gif)
print("[INFO] Total {} frames in the gif!".format(nums))
# convert form RGB to BGR
imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]
img = imgs[0]
print("[Check] image shape =:",img.shape)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print("[Check] image shape =:",img.shape)
magnitude_response, error = q3(img, img.shape[0], img.shape[0])


###################
t1 = "SHEPP-LOGAN PHANTOM"
t2 = "RECONSTRUCTED SHEPP-LOGAN IMAGE"
t3 = "ERROR IMAGE"
gs = gridspec.GridSpec(2, 4)
gs.update(wspace=0.5)
ax2 = plt.subplot(gs[1, 1:3])
#ax3 = plt.subplot(gs[1, 2:])
ax1 = plt.subplot(gs[0, 1:3])
plt.subplots_adjust(left=0.3)

ax1.imshow(img, cmap='gray')
ax1.set(title=t1)
ax1.set_xticks([])
ax1.set_yticks([])
l2 = ax2.imshow(magnitude_response, cmap='gray')
ax2.set(title=t2)
ax2.set_xticks([])
ax2.set_yticks([])
# l3 = ax3.imshow(error, cmap='gray')
# ax3.set(title=t3)
# ax3.set_xticks([])
# ax3.set_yticks([])


###Refernece for radio button code
#https://matplotlib.org/3.1.1/gallery/widgets/radio_buttons.html

axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.07, 0.6, 0.25, 0.25], facecolor=axcolor)
rax.set(title="GRID SIZE")
radio = RadioButtons(rax, ('P = N = M', 'P = N = 2M', '2P = N = M', 'P = N = M/2'))


def filter(label):
    hzdict = {'P = N = M': (img.shape[0], img.shape[0]), 'P = N = 2M': (2*img.shape[0], 2*img.shape[0]),
              '2P = N = M': (img.shape[0], img.shape[0]//2), 'P = N = M/2': (img.shape[0]//2, img.shape[0]//2)}
    f_size_new = hzdict[label]
    print("[INFO] f_size_new shape =:",f_size_new)
    magnitude_response1, error1 = q3(img, f_size_new[0], f_size_new[1])
    #cv2.imshow("image",magnitude_response1/255)
    #cv2.waitKey(0)
    # magnitude_response, phase_response = filter_output(image, f_size_new)
    # #l1.set_data(image)
    l2.set_data(magnitude_response1)
    #l3.set_data(error1)
    plt.draw()


radio.on_clicked(filter)
plt.show()
