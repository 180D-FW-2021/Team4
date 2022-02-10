# Freeride Game
#### Created by ECE180D Team 4: Yunxuan Helena Zhang, Yonghao Wu, Elijah Ellsberry, Edward Hage  

# Project Overview

Freeride is a mountain bike simulation that provides an engaging and interactive gaming experience for bikers and adventurers alike!
The game incorporates computer vision-based pose detection coupled with a custom wireless controller constructed using real mountainbike handlebars in order to create a sense of realistic steering in-game. The game may also be controlled using a traditional keyboard setup. In order to win, the player must navigate down a treacherous mountain terrain through highlighted rings before time runs out! Starting the game is as simple as saying "START" into your computer's microphone at the main menu or clicking the button to start playing!  

# Requirements

* Windows 10 PC with webcam and microphone
* Internet Connection
* Keyboard and Mouse
* Download the 1.0 version of the game by clicking **DOWNLOAD ALL** from [here](https://drive.google.com/drive/folders/1UwS_TOVVagyYyLYukNGMaLGsPThrIzT2?usp=sharing)
* A method of using SSH on your Raspberry Pi, instructions can be found 
* Miniconda
    * you can install it [here](https://docs.conda.io/en/latest/miniconda.html)

### If using custom controller

* Raspberry PI Zero WH
* MicroSD Card
    * Minimum of 8GB recommended
* BerryIMUv3
* 4 Pin JST SH Cable such as [this one](https://www.adafruit.com/product/4397)
* A method of powering the Raspberry Pi
    * External battery bank recommended but you can plug into PC as well
* A set of bike handlebars to make using the controller easier
    * We don't currently have instructions to make it but hardware-savvy users can see how the mount is done in the below photo
![Raspberry PI and IMU attached to mountain bike handlebars](/images/controller.png)  

# Controls
### Keyboard and Mouse
* W: Accelerate
* A: Turn left
* S: Reverse
* D: Turn right
* TAB: Open the in-game menu
* K: Toggle input method between wireless controller(setup below) and keyboard controls

# Setup

### Raspberry PI setup

The Raspberry PI setup comes directly from ECE180DA Lab4.  
Placeholder

### Software setup

Make sure that you run the following commands in the directory where you want to save the project

Run the following commands:
  
    git clone https://github.com/180D-FW-2021/Team4
    cd Team4
    cd controller
    conda create -n yourenvnamehere python=3.9
    conda activate yourenvnamehere
    pip install mediapipe==0.8.4
    
Launch a new command prompt window and run the following  

    ipconfig /all
    
In the output of that command you will see a section like the following  

![Bluetooth MAC address from running ipconfig /all in Windows](/images/mac.png)
    
Open receiver.py using the text editor of your choice and edit line 6 to include the MAC address from the previous step in the format "XX:XX:XX:XX:XX:XX"  
Using SSH on your Raspberry PI, run the following:

    git clone https://github.com/180D-FW-2021/Team4
    cd Team4
    cd controller
    
In berryIMUKalmanBluetooth.py, replace the MAC address in line 28 with the same MAC address used earlier

Run the following:

    sudo pip install smbus2==0.4.0
    
On your PC, run the following command:

    python receiver.py
    
Back on the Raspberry PI, run the following:

    sudo python berryIMUKalmanBluetooth.py
    
You should begin to see output like the following:  

![Output of receiver.py](/images/output.png)

Open another terminal window on your PC and navigate back into the Team4 directory as before
Run the following commands:

    conda activate yourenvnamehere
    python PoseModule.py

You may now launch the game and begin playing by double clicking on Freeride.exe

    