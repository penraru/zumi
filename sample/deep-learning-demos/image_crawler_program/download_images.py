# import the necessary packages
from imutils import paths
import argparse
import requests
import cv2
import os

"""
##ENTER THE FOLLOWING CODE BLOCK INTO CHROME JAVASCRIPT CONSOLE:
( View>Developer>Javascript Console )##


// pull down jquery into the JavaScript console
var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);


##ENTER THE FOLLOWING NEXT INTO THE CONSOLE. PLACE url.txt INTO OPERATING DIRECTORY##


// grab the URLs
var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });
// write the URls to file (one per line)
var textToSave = urls.toArray().join('\n');
var hiddenElement = document.createElement('a');
hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
hiddenElement.target = '_blank';
hiddenElement.download = 'urls.txt';
hiddenElement.click();


"""

BEGINNING_INDEX = 0 #image name increments from 'BEGINNING_INDEX'

#USAGE: run the following command below:
#python download_images.py --urls urls.txt --output images

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
args = vars(ap.parse_args())

# grab the list of URLs from the input file, then initialize the
# BEGINNING_INDEX number of images downloaded thus far
rows = open(args["urls"]).read().strip().split("\n")


# go through and download from the URLs
for url in rows:
	try:
		# try to download the image
		r = requests.get(url, timeout=60)

		# save the image to disk
		p = os.path.sep.join([args["output"], "{}.jpg".format(
			str(BEGINNING_INDEX).zfill(8))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()

		# update the counter
		print("[INFO] downloaded: {}".format(p))
		BEGINNING_INDEX += 1

# handle if any exceptions are thrown during the download process
	except:
		print("[INFO] error downloading {}...skipping".format(p))

# loop over the image paths we just downloaded again to check cv2 compatability
for imagePath in paths.list_images(args["output"]):
	# initialize if the image should be deleted or not
	delete = False

	# try to load the image
	try:
		image = cv2.imread(imagePath)

		# if the image is `None` then we could not properly load it
		# from disk, so delete it
		if image is None:
			delete = True

	# if OpenCV cannot load the image then the image is likely
	# corrupt so we should delete it
	except:
		print("Except")
		delete = True

	# check to see if the image should be deleted
	if delete:
		print("[INFO] deleting {}".format(imagePath))
		os.remove(imagePath)
