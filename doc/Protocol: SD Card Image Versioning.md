
## Linky SD Card Image Versioning Protocol
### Creating Images:

Insert the SD Card you want to clone into your computer

Type `diskutil list`in Terminal and locate your SD Card using the NAME and SIZE columns

Type `sudo dd if=/dev/diskX of=~/Desktop/raspberrypi.dmg` to create a dmg file. The X should be replaced by the disk number of the SD Card that can be located on the far left

Example filename: `linkyh0s0.iso`

In this example, the (h)ardware would be version 0, as would the (s)oftware.

The file should start with `linky` to maintain a consistent and easily identifiable set of images.

The version numbers should correspond to the iteration that they are a part of.

### Storing Images:

When logging a new image, you must create a .txt file detailing the specifics of the image in a format such that the file matches this example:
>ON THIS IMAGE
>- TensorFlow
>- Python 2.7
>- Raspbian Jessie
>- [Insert Specs Here]
>
>Hostname: linky.local
>
>Created during Iteration #0

(Note: The bullet points should be subbed for dashes.)

Once the .txt file has been made, the image and .txt should be compressed together using PiShrink or ZIP.

Finally, the .zip should be uploaded to the `Linky SD Card Images` folder within the `Robocar` folder on the Robolink Google Drive

Found here: https://drive.google.com/open?id=1GmKYLhqcIGYSJdso0mqw9ozfjdf9mTBq

NOTE: If space is an issue, see if someone else can upload it. Until then, keep it safe on your computer or an external drive.
