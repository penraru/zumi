# How to set up your new Linky using SD card



1. Insert the microSD card into your computer.
2. When the "Linky" drive appears, navigate to the **/boot** folder.

3. Place a file in this directory called wpa_supplicant.conf. Download the file [here.](https://drive.google.com/file/d/1_KYY2QRLB4kZ1Y1tzCxqEQ1NIvIHUdKZ/view?usp=sharing)
When you open wpa_supplicant.conf., it should look like this:

    >network={<br>
    		  ssid="YOUR_NETWORK_NAME"<br>
    		  psk="YOUR_PASSWORD"<br>
    		  key_mgmt=WPA-PSK<br>
      }

      Replace YOUR_NETWORK_NAME with your WiFi network name and YOUR_PASSWORD with your WiFi password. Leave the quotation marks. Please do not edit the quotation marks themselves, as they contain sensitive raspberry-pi specific formatting elements. (The key_mgmt field specifies what kind of security the WiFi network uses.)

5. Move the SDCard to the Pi and connect the power port to a power supply via the USB cable.
[TODO] need photo

6. Test that Linky is connected to your WiFi by typing into the terminal:  
    >ping zumi.local

    If you see "Request timed out", then Linky is not connected. [TODO] link to a connection troubleshooting guide

## We're now going to connect to Linky so that you can use it's Desktop from your computer...
7. Download and install [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/)

8. Open VNC Viewer and enter the following into the field for the VNC server address:

>linky.local

When prompted, the default password you will type in will be “pi”. Give the display a few seconds to load.
