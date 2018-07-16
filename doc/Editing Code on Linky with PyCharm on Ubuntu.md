## Step 1: Download and install PyCharm

## Step 2: Set up an SSH mount point
OS X:
>1. `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
>
>2. `brew cask install osxfuse` 
>
>3. `brew install sshfs`
>
>4. `sudo mkdir /mnt/linky`
>
>5. `sudo sshfs -o allow_other pi@[INSERT IP ADDRESS]:/ /mnt/linky/` (eg. 192.168.1.151)

The password is "pi"

Linux:
>1.`sudo apt-get install sshfs`
>
>2.`sudo mkdir /mnt/linky`
>
>3.`sudo sshfs -o allow_other pi@[INSERT IP ADDRESS]:/ /mnt/linky/` (eg. 192.168.1.151)

The password is "pi"

## Step 3: Open In PyCharm
File > Open /mnt/linky/home/pi/Desktop/Linky

## Step 4: Running Code
`ssh pi@[INSERT IP ADDRESS]`

The password is "pi"

`cd Desktop/Linky/sample/`

`python gyroTurnSpoon.py`

## (Optional) Step 5: Reconnect After a Reboot
`sudo rm -Rf /mnt/linky`

`sudo mkdir /mnt/linky`

`sudo sshfs -o allow_other pi@[INSERT IP ADDRESS]:/ /mnt/linky`

The password is "pi"


