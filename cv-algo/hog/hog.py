import cv2
import numpy as np
import os
from scipy import ndimage
import matplotlib.pyplot as plt
from numpy import arctan2, fliplr, flipud


def gradient(image):
    k_y = np.array([[-1,0,1]])
    k_x = np.array([[-1], [0], [1]])
    gx = ndimage.convolve(image, k_x, mode='constant', cval=1.0)
    gy = ndimage.convolve(image, k_y, mode='constant', cval=1.0)
    
    return gx, gy


def magnitude_and_theta(gx,gy):
    
    magnitude = np.sqrt(gx**2 + gy**2)
    magnitude = magnitude.astype(int)
    theta = (arctan2(gy, gx) * 180 / np.pi) % 360
    theta = theta.astype(int)
    return magnitude, theta


def cell_histogram(cell_direction, cell_magnitude, hist_bins):
    cell_hist = np.zeros(shape=(hist_bins.size))
    cell_size = cell_direction.shape[0]
    
    for row_idx in range(cell_size):
        for col_idx in range(cell_size):
            curr_direction = cell_direction[row_idx, col_idx]
            curr_magnitude = cell_magnitude[row_idx, col_idx]
            diff = np.abs(curr_direction - hist_bins)
            min_idx = np.argmin(diff) #return minimum difference
            min_2nd =  np.argmin(np.partition(diff,1)[1])
            
            if diff[min_idx] == 0:
                cell_hist[min_idx] += curr_magnitude
            
            else:
               #linear interpolation
                diff_1 =  np.abs(curr_direction - hist_bins[min_idx])
                diff_2 =  np.abs(curr_direction - hist_bins[min_2nd])
                cell_hist[min_idx] += (diff_1/(diff_1+diff_2)) * curr_magnitude 
                cell_hist[min_2nd] += (diff_2/(diff_1+diff_2)) * curr_magnitude 
                
    return cell_hist 


def sliding_window(image, step, window):
	x_loc = []
	y_loc = []
	cells = []

	for y in range(0, image.shape[0], step):
		for x in range(0, image.shape[1], step):
			cells.append(image[y:y + window[1], x:x + window[0]])
			x_loc.append(x)
			y_loc.append(y)
	return x_loc, y_loc, cells

# set window size
(w, h) = 8, 8
# read image 
img = cv2.imread('lena.jpg',0)

# calc grad
gx, gy = gradient(img)

# magnitude and dir
m, theta = magnitude_and_theta(gx,gy)

#cell_direction = m[:8, :8]
#cell_magnitude = theta[:8, :8]
hist_bins = np.array([0,20,40,60,80,100,120,140,160])

x_pos, y_pos, cells = sliding_window(m, 8, (w, h))

# put all hists here
concat_hist = []

for (x, y, cell) in zip(x_pos, y_pos, cells):
    cell_dir = cell
    cell_theta = theta[y:y + h, x:x + w]
    print(cell_dir.shape, cell_theta.shape)
    hist = None
    hist = cell_histogram(cell_dir, cell_theta, hist_bins)
    concat_hist.append(hist)

print("Done!")
    