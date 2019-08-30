'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code generate Fourier Transform (Magnitude response and phase response) of an image for different grid size
'''
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import matplotlib.gridspec as gridspec
# for the surface map
from mpl_toolkits.mplot3d import Axes3D
# process for filter size less than image size
def filter_output(input_image,filter_size):
    print("filter size is:{0} and image size:{1}".format(filter_size,input_image.shape[0]))
    row = input_image.shape[0]
    col = row
    if row > filter_size:
        blank_image_magnitude = np.zeros(input_image.shape)
        blank_image_phase = np.zeros(input_image.shape)
        split_size = row//filter_size
        print("split_size",split_size)
        for i in range(split_size):
            for j in range(split_size):
                crop_img = input_image[i*filter_size:i*filter_size + filter_size,j*filter_size:j*filter_size+filter_size]
                f = np.fft.fft2(crop_img, (filter_size, filter_size))
                fshift = np.fft.fftshift(f)
                magnitude_response = 20 * np.log(1+np.abs(fshift))
                blank_image_magnitude[i*filter_size:i*filter_size + filter_size,j*filter_size:j*filter_size+filter_size]=magnitude_response
                phase_response =np.angle(fshift)
                blank_image_phase[i*filter_size:i*filter_size + filter_size,j*filter_size:j*filter_size+filter_size]=phase_response
                #print(magnitude_response[0][0],phase_response[0][0])
        return (blank_image_magnitude,blank_image_phase)
    else:
        f = np.fft.fft2(image, (filter_size, filter_size))
        fshift = np.fft.fftshift(f)
        magnitude_response = 20 * np.log(np.abs(fshift))
        phase_response = np.angle(fshift)
        return (magnitude_response,phase_response)

## reading and displaying image
image = cv2.imread("data/cameraman.tif",0)
print("Image Shape :",image.shape)
#### will be handled by radio button
f_size = 64
###########
##Reference for code
##https://stackoverflow.com/questions/35994306/matplotlib-3-plots-plotted-in-2-rows-with-single-image-centered
gs = gridspec.GridSpec(2, 4)
gs.update(wspace=0.5)
ax2 = plt.subplot(gs[1, :2], )
ax3 = plt.subplot(gs[1, 2:])
ax1 = plt.subplot(gs[0, 1:3])
##########
magnitude_response, phase_response = filter_output(image, f_size)
#fig, ax = plt.subplots(2,2)

#l, = ax.plot(t, s0, lw=2, color='red')
plt.subplots_adjust(left=0.3)

l1 = ax1.imshow(image,cmap='gray')
ax1.set(title='INPUT IMAGE')
ax1.set_xticks([])
ax1.set_yticks([])
l2 = ax2.imshow(magnitude_response,cmap='gray')
ax2.set(title='MAGNITUDE RESPONSE')
ax2.set_xticks([])
ax2.set_yticks([])
l3 = ax3.imshow(phase_response,cmap='gray')
ax3.set(title='PHASE RESPONSE')
ax3.set_xticks([])
ax3.set_yticks([])

###Refernece for radio button code
#https://matplotlib.org/3.1.1/gallery/widgets/radio_buttons.html

axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.07, 0.6, 0.25, 0.25], facecolor=axcolor)
rax.set(title="GRID SIZE")
radio = RadioButtons(rax, ('m=64', 'm=128', 'm=256', 'm=512', 'm=1024'))
def filter(label):
    hzdict = {'m=64': 64, 'm=128': 128, 'm=256': 256, 'm=512':512, 'm=1024':1024}
    f_size_new = hzdict[label]
    magnitude_response, phase_response = filter_output(image, f_size_new)
    #l1.set_data(image)
    l2.set_data(magnitude_response)
    l3.set_data(phase_response)
    plt.draw()


radio.on_clicked(filter)
plt.show()