# How to set up your new Linky using SD card



1. Insert the miniSD card into the computer.
2. Go to the boot folder which should appear in your file explorer. Alternatively you can navigate to the boot directory by entering the following into terminal:

    >cd ~/Volumes/boot

3. Create a file in this directory called wpa_supplicant.conf. The file should contain the following text:

    >network={
    		ssid="YOUR_NETWORK_NAME"
    		psk="YOUR_PASSWORD"
    		key_mgmt=WPA-PSK
      }

      Replace YOUR_NETWORK_NAME with your network name and YOUR_PASSWORD with your network password. Keep the quotation marks. The key_mgmt field specifies what kind of security the wifi network uses.

4. With this file in place, Raspbian will move it in /etc/wpa_supplicant/ when the system is booted.

5. The next step is to boot the Pi and test, while the SD card is still in your computer. If you're going to try to connect via SSH, it may need to be enabled.
You can connect to Linky by either using SSH (Secure Shell) or a VNC (Virtual Network Computing) Server.
6. First, ensure that the Linky is connected to the same Wifi Network as you. To do this, you can enter the following into your terminal:

>ping linky.local

You will see something like this, it’s okay if the numbers here do not match yours:

>PING linky.local (192.168.1.170): 56 data bytes
64 bytes from 192.168.1.170: icmp_seq=0 ttl=64 time=47.833 ms
64 bytes from 192.168.1.170: icmp_seq=1 ttl=64 time=18.792 ms
…

## CONNECTING TO LINKY USING SECURE SHELL
To connect to the Linky using SSH, enter the following into your terminal:

>ssh pi@linky.local

When prompted, the default password you will type in will be “pi”


## CONNECTING TO LINKY USING VIRTUAL NETWORK COMPUTING
Open the VNC Viewer of your choice. To connect to the Linky using VNC, enter the following into the field for the VNC server address:

>Linky.local

When prompted, the default password you will type in will be “default”. Give the display a few seconds to load.
