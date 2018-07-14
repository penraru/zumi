# How to set up your new Linky using SD card



1. Insert the miniSD card into your computer.
2. When the "Linky" drive appears, navigate to the **/boot** folder.

3. Create a file in this directory called wpa_supplicant.conf. Open the file and paste the following text:

    >network={
    		ssid="YOUR_NETWORK_NAME"
    		psk="YOUR_PASSWORD"
    		key_mgmt=WPA-PSK
      }

      Replace YOUR_NETWORK_NAME with your WiFi network name and YOUR_PASSWORD with your WiFi pFssword. Keep the quotation marks. (The key_mgmt field specifies what kind of security the WiFi network uses.)

5. Move the SDCard to the Pi and connect the power port to a power supply via the USB cable.
[TODO] need photo 

6. Test that Linky is connected to your WiFi by typing into the terminal:  
>ping linky.local

If you see "Request timed out", then Linky is not connected. [TODO] link to a troubleshooting guide

## We're now going to connect to Linky so that you can use it's Desktop from your computer. 
7 .Download and install VNC viewer

8 Open VNC Viewer and enter the following into the field for the VNC server address:

>linky.local

When prompted, the default password you will type in will be “pi”. Give the display a few seconds to load.

## CHANGING THE HOSTNAME
In your terminal, type in

>sudo raspi-config

And select option "2 Hostname" using the arrow keys on your keyboard. Use the enter key to select your desired option.

You will be given some hostname guidelines on the following screen. After entering in the new hostname that complies with these guidelines, use the arrow down key to select the "Okay" option. Beware that there will be no warning if you enter a hostname that does not comply with guidelines.

Use the side arrow keys to select the "Finish" option. When asked to reboot you can choose not to reboot. To check that your hostname has been changed, enter the following into the terminal:

 >hostname

 You have changed your hostname!
