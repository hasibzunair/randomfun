import cv2
import time

img = cv2.imread("lena.jpg")
(w, h) = 16, 16


def sliding_window(image, step, window):
	x_loc = []
	y_loc = []
	cells = []
	#import pdb; pdb.set_trace()

	for y in range(0, image.shape[0], step):
		for x in range(0, image.shape[1], step):
			
			x_end = x+window[0]
			y_end = y+window[1]
			cells.append(image[y:y_end, x:x_end])
			x_loc.append(x)
			y_loc.append(y)
	return x_loc, y_loc, cells

x_pos, y_pos, cells = sliding_window(img, 8, (w, h))



for (x, y) in zip(x_pos, y_pos):
	# make a copy of image

	# do some stuff
	#cv2.rectangle(clone, (x, y), (x+w, y+h), (0, 255, 0),2)
	
	x1 = str(x) + " " + str(y)
	x2 = str(x+w) + " " + str(y+h)
	#cv2.imshow("slide cells", clone)
	print(x1, x2)	
	#cv2.waitKey(1)
	time.sleep(5)
	#import pdb; pdb.set_trace()	
	#if cv2.waitKey(1) & 0xFF == ord('q'):
	#	break

cv2.destroyAllWindow()
