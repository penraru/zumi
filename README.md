# So you have a new Zumi!

The first thing you need to do is connect her to your WiFi network.

1. Connect the power port to your computer using a microUSB cable.<BR>
[TODO] needs photo

2. Use another microUSB cable to connect the USB port on the Raspberry Pi to your computer.<BR>
[TODO] needs photo

#### For Mac Users:
1. Goto System Preferences → Network → RNDIS/Gadget (should be in yellow light).<BR>
[TODO] needs photo

2. Configure IPv4 should be set to Manually.<BR>
[TODO] needs photo

3. Set IP Address and Router to 192.168.7.1 + Subnet mask to 255.255.255.0. Press Apply.<BR>
[TODO] needs photo

4. Open Terminal and "ssh pi@192.168.7.2"

5. "sudo raspi-config" --> "Network Options"

#### For Windows Users:
1. Open up Network and Sharing Center and click on Change Adapter Settings

2. There will be a list of adapters. Find the RNDIS adapter and right-click to select Properties.

3. Select the Internet Protocol Version 4 (TCP/IPv4) from the connection list and click Properties.

4. “Use the following IP address:”
- IP Address: 192.168.7.1  Subnet Mask: 255.255.255.0  Router: 192.168.7.1

5. If there is a problem, try to unplug and replug the connection. Windows will identify the network.

6. Open up command box and use “ipconfig /all” to check the connection

7. “ssh pi@192.168.7.2”


# Then you can see what she sees by clicking here!
http://zumi.local:5555/notebooks/recipe/ZumiCam.ipynb <BR>
