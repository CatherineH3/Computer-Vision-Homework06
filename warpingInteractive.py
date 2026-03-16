# Special Studies: Computer Vision (CSE 40535)
# University of Notre Dame
# ______________________________________________________________________
# Adam Czajka, Toan Q. Nguyen, Siamul Khan, Walter Scheirer 2016 -- 2025

import numpy as np
import math
import cv2
from ROIPoly import roiPoly

roi = roiPoly(sort=False)

# Get selected image from roi poly object
I = cv2.cvtColor(np.array(roi.origImage), cv2.COLOR_RGB2BGR)
rows, cols, channels = I.shape

# Get transformation matrix using points from roi
src = np.float32(roi.points)
dst = np.float32([[0, 0], [cols-1, 0], [cols-1, rows-1], [0, rows-1]])
# dst = np.float32([[cols-1, 0], [0, 0], [0, rows-1], [cols-1, rows-1]]) # dst matrix if sort is enabled

H_mat = cv2.getPerspectiveTransform(src, dst)

# Having matrix H we may do our transformation for each pixel:
I_transformed = np.zeros(I.shape).astype(np.uint8)


### Original Version of the code for safekeeping------------------------------------------------------
#count = 0
#for y_source in range(0, rows):
#    for x_source in range(0, cols):
#        
#        sourcePX = np.float32([[x_source], [y_source], [1]])
#
#         *** The following line requires modification if you want to implement the #"inverse warping":
#        destPX = H_mat @ sourcePX
#        
#        x_dest = int(destPX[0,0]/destPX[2,0])
#        y_dest = int(destPX[1,0]/destPX[2,0])
#
#        if x_dest > 0 and y_dest > 0 and x_dest < cols and y_dest < rows:
#            count = count + 1

#            *** The following line requires modification if you want to implement the "inverse warping":
#            I_transformed[y_dest, x_dest, :] = I[y_source, x_source, :]


### First attempt- I mostly am swapping the sources and destinations:-----------------------------------
inv_H = np.linalg.inv(H_mat)

count = 0
for y_dest in range(0, rows):
    for x_dest in range(0, cols):
        
#        sourcePX = np.float32([[x_source], [y_source], [1]])
#        *** The following line requires modification if you want to implement the #"inverse warping":
#        destPX = H_mat @ sourcePX
         sourcePX = inv_H @ np.array([[x_dest], [y_dest], [1]])
        
         x_source = int(sourcePX[0,0]/sourcePX[2,0])
         y_source = int(sourcePX[1,0]/sourcePX[2,0])

         if x_source > 0 and y_source > 0 and x_source < cols and y_source < rows:
             count = count + 1

#            *** The following line requires modification if you want to implement the "inverse warping":
             I_transformed[y_dest, x_dest, :] = I[y_source, x_source, :]


### Alternate method to Add inverse Warping (works well and more concise)---------------

#xx, yy = np.meshgrid(np.arange(cols), np.arange(rows))
#dest_coords = np.stack([xx.ravel(), yy.ravel()], axis=-1).astype(np.float32)
#source_coords = cv2.perspectiveTransform(dest_coords[None, :, :], np.linalg.inv(H_mat))[0]
#I_transformed[yy.ravel(), xx.ravel()] = I[np.clip(source_coords[:,1],0,rows-1).astype(int), np.clip(source_coords[:,0],0,cols-1).astype(int)]
#count = rows * cols  # all pixels are now filled

### End of edited section---------------------------------------------------------------

I_correct_xformed = cv2.warpPerspective(I, H_mat, (cols, rows), flags=cv2.INTER_NEAREST)

# New stuff for scaling
# Set max total width and height for display
max_total_width = 1200   # width for both images together
max_total_height = 600   # max height

# Get original sizes
h1, w1 = I_transformed.shape[:2]
h2, w2 = I_correct_xformed.shape[:2]

# Compute scale to fit both width and height
scale_w = max_total_width / (w1 + w2)
scale_h = max_total_height / max(h1, h2)
scale = min(scale_w, scale_h, 1.0)  # do not upscale

# Resize images
I_transformed_small = cv2.resize(I_transformed, (int(w1*scale), int(h1*scale)))
I_correct_small = cv2.resize(I_correct_xformed, (int(w2*scale), int(h2*scale)))

# Concatenate and display
display_img = np.concatenate([I_transformed_small, I_correct_small], axis=1)
cv2.imshow('Warped Images (left is yours, right is correct)', display_img)


# Old
#cv2.imshow('Warped Images (left is yours, right is the correct one from library implementation)', np.concatenate([I_transformed, I_correct_xformed], axis=1))
print('This version of warping calculated new values for ', 100*count/(rows*cols), '% of destination pixels.')
cv2.waitKey(0)
cv2.destroyAllWindows()