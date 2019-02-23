import cv2
import time

img = cv2.imread("lena.jpg")
(w, h) = 16, 16


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



x_pos, y_pos, cells = sliding_window(img, 8, (w, h))

for (x, y) in zip(x_pos, y_pos):
	# make a copy of image
	clone = img.copy()
	
	# do some stuff
	cv2.rectangle(clone, (x, y), (x+w, y+h), (0, 255, 0),2)
	
	cv2.imshow("slide cells", clone)
	#print(x, y)	
	cv2.waitKey(1)
	time.sleep(0.025)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindow()

