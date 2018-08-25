# Use Eclipse to install PyDev and write code
[Install Eclipse Python plugin](#install-eclipse-python-plugin)

[Setup Remote Systems Explorer for Raspberry Pi](#setup-remote-systems-explorer-for-raspberry-pi)

[Connecting to Raspberry Pi](#connecting-to-raspberry-pi)

[Running Codes using Ssh Shells](#running-codes-using-ssh-shells)

**Install the following:**

Eclipse IDE for JAVA Developers    [http://www.eclipse.org/downloads/](http://www.eclipse.org/downloads/)

Python (version 2.7 or higher)     [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Install Eclipse Python plugin

1. Open up Eclipse.

2. Goto the toolbar **Help** and press **Install New Software**.

3. Insert the link http://pydev.org/updates under the section **Work with**. Press **Add** to use the PyDev Plug and **Next**.

4. The screen should show Install details with item name "PyDev for Eclipse" and its version. Press **Next**.

5. Installing should take few minutes, showing progress on the bottom right corner of Eclipse.

6. When installation is complete, goto the toolbar **Windows** and press **Preferences**.

7. Select PyDev on the left margin. Goto **Interpreters** then to **Python Interpreter**.

8. Click **New...**

9. Browse your Python **Interpreter Executable** and then **Ok**

10. Continue by clicking **Ok** for the **System Python Path**

11. Press **Ok** once again after you have confirmed that Python Interpreter for PyDev is set up.


## Setup Remote Systems Explorer for Raspberry Pi

1. Goto the toolbar **Help** and press **Install New Software**

2. Change the section **Work with** to **All Available Sites**

3. Use type filter text = **remote**

4. Select **General Purpose Tools** --> **Remote System Explorer End-User Runtime** and **Remote System Explorer User Actions**. Press **Next**.

5. Finish the installation and restart Eclipse.

## Connecting to Raspberry Pi

1. Goto the toolbar **Window** --> **Open Perspective** --> **Other**

2. Select **Remote System Explorer**.

3. Right click on **Local**. Press **New** and **Connection**.
 
4. Select **SSH Only**. Press **Next**

5. Under **Host name:**, enter either the Pi's IP Address or its hostname. Press **Finish**.

6. Connect and remote to the Raspberry Pi by clicking **Sftp Files** and **My Home**. Eclipse will ask for the Pi's username and password.

## Running Codes using Ssh Shells

1. Right click on “Ssh Shells” under your Pi’s hostname/IP Address

2. Press “Launch Shell” and you will be guided to the Pi’s “Remote Shell”

3. Guide yourself to the Linky Directory
```
cd ~
cd Desktop
cd Linky 
```

4. Go into a directory which has a file you wish (doc   lib    recipe    sample   src).
```
e.g. cd recipe  
```

5. In order to run the file, you need the command
```
python “The_name_of_the_file”
```

**_*Make sure your Linky is turned ON (Check for Blue LED Light)_**




