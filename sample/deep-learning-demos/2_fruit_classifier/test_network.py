# USAGE
# python test_network.py --model <model_name_here>

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import cv2


FRUIT = __NAME_OF_YOUR_FAVORITE_FRUIT__

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
args = vars(ap.parse_args())
number = 0 #UPDATE THIS NUMBER FOR ACTIVE TRAINING
cap = cv2.VideoCapture(0)

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])

while True:
	ret,image = cap.read()
	orig = image.copy()

	# pre-process the image for classification
	image = cv2.resize(image, (28, 28))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	# classify the input image
	(notFruit, fruit) = model.predict(image)[0]

	# build the label
	label = FRUIT if fruit > notFruit else "Not "+FRUIT
	proba = fruit if fruit > notFruit else notFruit



	#active training component
	if label is FRUIT and proba > 0.7:
		print("[INFO] SIGNIFICANT RESULT")
		#cv2.imwrite(<PATH_TO_FRUIT_PICTURES/signifcant_'str(number)+'.jpg', orig)
		#example: cv2.imwrite('images/apple/significant_'+str(number)+'.jpg', orig)
		number+=1

	label = "{}: {:.2f}%".format(label, proba * 100)

	# draw the label on the image
	output = cv2.resize(orig, (0,0), fx=0.5, fy=0.5)
	cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

	# show the output image
	cv2.imshow("Output", output)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		cap.release()
		break
