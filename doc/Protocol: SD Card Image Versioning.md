
## Linky SD Card Image Versioning Protocol
If you want to get the latest master image onto your Linky, use the section called **Flashing an SD Card**.

If you want to upload your latest image to the SDCard image repository, use **Storing Images**.

### Storing Images:

First, clone Image from SD Card to Computer:

Insert the SD Card you want to clone into your computer

Type `diskutil list` in Terminal and locate your SD Card using the NAME and SIZE columns (or `df` in Linux)

Type `sudo dd if=/dev/diskX of=~/Desktop/linky-sdcard.iso` to create an iso file. The X should be replaced by the disk number of the SD Card that can be located on the far left (e.g. `/dev/sdb`)

Example filename: `linkyh0s0.iso`

In this example, the (h)ardware would be version 0, as would the (s)oftware.

The file should start with `linky` to maintain a consistent and easily identifiable set of images.

The version numbers should correspond to the iteration that they are a part of.

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

Once the .txt file has been made, the .txt should be given the same name as the .iso.

Finally, both the .iso and .txt should be uploaded to Robolink's `WDMyCloud` shared server within `/Public/Linky Images/`.

If you need an image and are away from the office, please ask for someone to zip and share the image with you over Google Drive, or check with their .txt and update your image accordingly.

### Flashing an SD Card:

Insert the SD Card you want to flash into your computer

Download and open Etcher

Press 'Select Image'

Go to 'WDMyCloud' from the section Shared -> 'Public' -> 'Linky Images'

Select and open the .iso file: 'linkyhOsO.iso'

Select a drive (ex.Apple SDXC Reader Media - 31.91 GB) and press 'Continue'

Press 'Flash' to start flashing your sd card
