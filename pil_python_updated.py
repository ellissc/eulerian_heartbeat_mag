from PIL import Image
from math import sqrt
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#video to frames
#ffmpeg -i eye_edit_top_left.avi $filename%03d.bmp


video = []
avgs = []
x_vals= []
print("starting")
number_of_frames = 901 #change to the number of frames to analyze
#gathers luminence values
for i in range(1, number_of_frames+1):
    x_vals.append(i/30)
    if len(str(i)) == 1:
        dig = '00'+str(i)
    elif len(str(i)) == 2:
        dig = '0'+str(i)
    else:
        dig = str(i)
    filename = dig+'.bmp'
    #print(filename)
    imag = Image.open(filename)
    width, height = imag.size
    #print(width, height)
    image_array = np.zeros(shape=(height, width))
    imag = imag.convert ('RGB')
    for x in range(0, width):
        #print("x: ",x)
        for y in range(0, height):
            #print("y: ",y)
            pixelRGB = imag.getpixel((x,y))
            R,G,B = pixelRGB 
            brightness = sum([R,G,B])/3
            image_array[y,x] = brightness
    average = np.average(image_array)
    avgs.append(average)
    video.append(image_array)
    print("Frame " + filename + " done")


#plot average luminence for given footage
plt.plot(x_vals, avgs)
plt.xlabel("Time (s)")
plt.ylabel("Brightness")
plt.title("Average brightness for 30 sec of child eye film")
plt.show()
plt.close()

#converts frame by frame to pixel lengthwise values, and filters to a given max-min difference
video_lengthwise = []
for x in range(0, width):
    for y in range(0, height):
        holder = []
        for inner_array in video:
            holder.append(inner_array[y,x])
        maximum = np.max(holder)
        minimum = np.min(holder)
        #print(abs(maximum - minimum))
        if abs(maximum - minimum) <125: 
            video_lengthwise.append(holder)


#creates heatmap
hm = np.zeros(shape=(height, width))
for x in range(0, width):
    for y in range(0, height):
        holder = []
        for inner_array in video:
            holder.append(inner_array[y,x])
        hm[y,x] = abs(np.max(holder)-np.min(holder))

sns.heatmap(hm)
plt.title("Max/min difference heatmap upper eyelid area")
plt.show()
#plt.imshow(hm, cmap='hot', interpolation='nearest')
#plt.show()


#print(len(video_lengthwise))

#plots filtered pixel luminence values
for i in video_lengthwise:
    plt.plot(x_vals, i)
plt.xlabel("Time (s)")
plt.ylabel("Brightness")
plt.title("Per pixel brightness (|max - min| <125)")
plt.show()

