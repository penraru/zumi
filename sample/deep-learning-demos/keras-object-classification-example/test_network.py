# USAGE
# python test_network.py --model apple_not_apple.model

#model 1 is for computer, model 2 is for pi

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image")
args = vars(ap.parse_args())
number = 306
cap = cv2.VideoCapture(0)

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])

# load the image
#image = cv2.imread(args["image"])
while (1):
	ret,image = cap.read()
	orig = image.copy()

	# pre-process the image for classification
	image = cv2.resize(image, (28, 28))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	# classify the input image
	(notApple, apple) = model.predict(image)[0]

	# build the label
	label = "Apple" if apple > notApple else "Not Apple"
	proba = apple if apple > notApple else notApple
	if label is "Apple" and proba > 0.7:
		print("[INFO] SIGNIFICANT RESULT")
		#cv2.imwrite('images/apple/significant_'+str(number)+'.jpg', orig)
		number+=1

	label = "{}: {:.2f}%".format(label, proba * 100)

	# draw the label on the image
	output = imutils.resize(orig, width=400)
	cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

	# show the output image
	cv2.imshow("Output", output)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		cap.release()
		break