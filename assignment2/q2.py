'''
Created by Vikash Kumar
Email: vikash0837@gmail.com
Below code generate Fourier Transform (Magnitude response and phase response) of a 2D cosine function
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.lines as mlines
a = np.arange(1,257)
b = np.arange(1,257)
k,m = np.meshgrid(a,b)
freq = np.pi/100
theta = np.pi/100
input_data = np.cos(freq*(k*np.cos(theta) + m*np.sin(theta)))
output_data = np.fft.fft2(input_data)
fshift = np.fft.fftshift(output_data)
magnitude_response = 20 * np.log(1+np.abs(fshift))
phase_response = np.angle(fshift)
fig, ax = plt.subplots(1,3)
l1 = ax[0].imshow(input_data,cmap='gray')
ax[0].set(title="PLANE WAVE")
# defining legend style and data
##Reference: https://stackoverflow.com/questions/11983024/matplotlib-legends-not-working
blue_line = mlines.Line2D([], [], color='blue', label='Freq = 0.034')
reds_line = mlines.Line2D([], [], color='red', label='Theta = 0.034')

l = ax[0].legend(handles=[blue_line,reds_line])
l2 = ax[1].imshow(magnitude_response,cmap='gray')
ax[1].set(title="FOURIER MAGNITUDE")
l3 = ax[2].imshow(phase_response,cmap='gray')
ax[2].set(title="FOURIER PHASE")
# plt.show()


### Slider Implitation
#axcolor = 'lightgoldenrodyellow'
axcolor1 = 'red'
axcolor2 = 'blue'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor2)
axtheta = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor1)

sfreq = Slider(axfreq, 'Freq', 0.01, np.pi)
stheta = Slider(axtheta, 'Theta', 0.01, 2.0*np.pi)


def update(val):
    theta = stheta.val
    freq = sfreq.val
    input_data = np.cos(freq * (k * np.cos(theta) + m * np.sin(theta)))
    output_data = np.fft.fft2(input_data)
    fshift = np.fft.fftshift(output_data)
    magnitude_response = 20 * np.log(1 + np.abs(fshift))
    phase_response = np.angle(fshift)
    text1 = "Freq = " + str(round(freq,2))
    text2 = "Theta = " + str(round(theta,2))
    l.get_texts()[0].set_text(text1)
    l.get_texts()[1].set_text(text2)
    l1.set_data(input_data)
    #l1.set_label([freq,theta],['freq','theta'])
    l2.set_data(magnitude_response)
    l3.set_data(phase_response)
    fig.canvas.draw_idle()


sfreq.on_changed(update)
stheta.on_changed(update)
plt.show()