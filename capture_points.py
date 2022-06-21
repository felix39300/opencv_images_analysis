# imports
# Plot
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import math
import random as rand
# Webcam
import cv2

cam_on = True
img_counter = 0

### Capturing dart location using webcam: -------------------------------------------
# Setup webcam to get the data
if (cam_on):
    cap = cv2.VideoCapture(0)
    # Loop until exit or measurements done
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Resize frame
        frame = cv2.resize(frame, (1024, 768), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # adaptive thresholding to use different threshold
        # values on different regions of the frame.
        #filtered = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        prefiltered = cv2.GaussianBlur(frame, (5, 5), 0)
        filtered = cv2.Canny(prefiltered, 100, 200)

        # 1280 × 720
        # Show resulting frame once edge detection is applied
        cv2.imshow('Shooting Board', filtered)

        #	TODO	Notify user to take reference image
        # Escape meas process or take picture using space
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC key pressed => close everything
            break

        elif k % 256 == 32:
            # Space pressed => capture one image
            img_name = "dartCapture_{}.png".format(img_counter)
            cv2.imwrite(img_name, filtered)
            print("{} written!".format(img_name))
            img_counter += 1

    ## IDEA: make computation of dart locations in while loop and save locations
    # 	OR take all pictures and then compute after while loop

    # release the video capture object
    cap.release()
    # Closes all the windows currently opened.
    cv2.destroyAllWindows()

### Collect dart locations
# Get position of the dart
# TODO


# number of darts shot #TODO: get number of darts shot from video
n_meas = 100
# Size of shooting board
x_size = 100
y_size = 100
# hit oundaries for a dart to be considered as a good hit
x_low_bound = 40
x_up_bound = 60
y_low_bound = 40
y_up_bound = 60

# create 2d array to store dart positions
data = np.empty((0, 2))

# generate random fake dart points
for i in range(0, n_meas, 1):
    xrand = rand.randrange(0, x_size, 1)
    yrand = rand.randrange(0, y_size, 1)
    data = np.append(data, np.array([[xrand, yrand]]), axis=0)

### Data analysis----------------------------------------------------------------
# count number of dart within the given boundary
counter = 0
# not working since i and k should be bounded as tuple
for i in data:
    if i[0] in range(x_low_bound, x_up_bound) and i[1] in range(y_low_bound, y_up_bound):
        counter += 1

count_str = str(counter) + " Target hits "

# Plot dart locations and boundaries rectangle
fig, ax = plt.subplots()
ax.plot(data[:, 0], data[:, 1], 'ko')
ax.add_patch(
    Rectangle(((x_low_bound, y_low_bound)), (x_up_bound - x_low_bound), (y_up_bound - y_low_bound), edgecolor='green',
              facecolor='gray', lw=5))
title = 'Dart locations: ' + str(counter) + ' Target hits'
plt.title(title)
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.grid()
plt.show()
