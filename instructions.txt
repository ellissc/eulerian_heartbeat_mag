1. Crop the video to the target area (in the future, could potentially use a neural net to auto focus)

2. Place video in EVM_Matlab/data

3. In matlab, navigate to the EVM_matlab folder

4. (one time) Install:
    MATLAB support for MinGW-w64 C/C++ Compiler, image proc toolbox and signal proc toolbox

5. In reproduceResults.m:
inFile = fullfile(dataDir,'YOUR_VIDEO.mp4');
fprintf('Processing %s\n', inFile);
amplify_spatial_lpyr_temporal_butter(inFile, resultsDir, 60, 90, 3.6, 6.2, 30, 0.3);
amplify_spatial_lpyr_temporal_iir(inFile, resultsDir, 10, 16, 0.4, 0.05, 0.1);

6. Run make.m, install.m, then reproduceResults.m

7. Processed videos found in EVM_Matlab/ResultsSIGGRAPH2012

8. Move the video to a new folder

9. Run the command "ffmpeg -i YOUR_PROC_VIDEO.mp4 $filename%03d.bmp"

10. pil_python.py script:
    change number_of_frames to amount of frames produced by ffmpeg command
    first part gathers luminence values
    second part:

Average brightness for the film:
'''
plt.plot(x_vals, avgs)
plt.xlabel("Time (s)")
plt.ylabel("Brightness")
plt.title("Average brightness for 30 sec of child eye film")
plt.show()
plt.close()

Only plots when diff between max and min brightness in a certain range
video_lengthwise = []
for x in range(0, width):
    for y in range(0, height):
        holder = []
        for inner_array in video:
            holder.append(inner_array[x,y])
        maximum = np.max(holder)
        minimum = np.min(holder)
        print(abs(maximum - minimum))
        if abs(maximum - minimum) > 220:     #### change to the range you want
            video_lengthwise.append(holder)
'''


Heatmap portion:

hm = np.zeros(shape=(height, width))
for x in range(0, width):
    for y in range(0, height):
        holder = []
        for inner_array in video:
            holder.append(inner_array[y,x])
        hm[y,x] = abs(np.max(holder)-np.min(holder))

sns.heatmap(hm)
plt.title("Max/min difference heatmap own wrist area")
plt.show()
#plt.imshow(hm, cmap='hot', interpolation='nearest')
#plt.show()



#print(len(video_lengthwise))

'''
for i in video_lengthwise:
    plt.plot(x_vals, i)
plt.xlabel("Time (s)")
plt.ylabel("Brightness")
plt.title("Per pixel brightness (|max - min| > 220)")
plt.show()

'''