# Freeride Game
#### Created by ECE180D Team 4: Yunxuan Helena Zhang, Yonghao Wu, Elijah Ellsberry, Edward Hage  

# Project Overview
### You can find our leaderboard website [here!](https://freeride-leaderboard.herokuapp.com/) (work in progress...)

Freeride is a mountain bike simulation that provides an engaging and interactive gaming experience for bikers and adventurers alike!
The game incorporates computer vision-based pose detection coupled with a custom wireless controller constructed using real mountainbike handlebars in order to create a sense of realistic steering in-game. The game may also be controlled using a traditional keyboard setup. In order to win, the player must navigate down a treacherous mountain terrain through highlighted rings before time runs out! Starting the game is as simple as saying "START" into your computer's microphone at the main menu or clicking the button to start playing!  

# Requirements

* Windows 10 PC with webcam and microphone
* Internet Connection
* Keyboard and Mouse
* Download the 1.0 version of the game by clicking **DOWNLOAD ALL** from [here](https://drive.google.com/drive/folders/1TNyI20opnT0iORDcK3ohroQoQwGf5iiG?usp=sharing)
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

Run the following commands on your host PC:
  
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
    
On your Raspberry PI, open berryIMUKalmanBluetooth.py, replace the MAC address in line 28 with the same MAC address used earlier

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

    
# Game Rules

### Control Method
Each time a player is spawned, the default input method is the IMU controller. If you're using a keyboard, simply press [k] right after spawning. You can also press [k] again to change back to IMU control.

### Solo Mode

* After entering the game scene, click the [Host(Server+Client)] button in the top left corner to spawn your player.
![Host/client Options](/images/ss1.png)
* To win the game, collect all 3 checkpoint rings before the timer runs out. There are also little Christmas-themed objects along the way that you can feel free to explore.
**Important** Remember to [Stop Host/Client] at the end of a round.

### Duo Mode

* As the first player, click the [Host(Server+Client)] button.
* After the first player has established server, the second player can enter the hostname in the input field (saying localhost by default), then click [Client] to connect to the game.
* Now the two players can ride around in the same game!
* The duo mode has no checkpoints. Players can freely explore around the mountain, enjoy the view, while gathering the Christmas-themed collectibles.
* The collectibles are now each worth 100 points; you could work together to gain points before the clock runs out - or you could just play around :D
**Important** Remember to [Stop Host/Client] at the end of a round.

### Voice Commands

*