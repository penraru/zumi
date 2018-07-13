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

4. With this file in place, Raspbian will move it in /etc/wpa_supplicant/ when the system is booted.

5. The next step is to boot the Pi and test, while the SD card is still in your computer. If you're going to try to connect via SSH, it may need to be enabled.
You can connect to Linky by either using SSH (Secure Shell) or a VNC (Virtual Network Computing) Server.
6. If you have your hostname set to anything other than 'linky', then you should replace the word 'linky' with your custom hostname in these instructions. We will discuss how to change hostnames later in these instructions.

First, ensure that the Linky is connected to the same Wifi Network as you. You can enter the following into your terminal:

>FORMAT: ping [hostname].local  
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

>linky.local

When prompted, the default password you will type in will be “default”. Give the display a few seconds to load.

## CHANGING THE HOSTNAME
In your terminal, type in

>sudo raspi-config

And select option "2 Hostname" using the arrow keys on your keyboard. Use the enter key to select your desired option.

You will be given some hostname guidelines on the following screen. After entering in the new hostname that complies with these guidelines, use the arrow down key to select the "Okay" option. Beware that there will be no warning if you enter a hostname that does not comply with guidelines.

Use the side arrow keys to select the "Finish" option. When asked to reboot you can choose not to reboot. To check that your hostname has been changed, enter the following into the terminal:

 >hostname

 You have changed your hostname!
