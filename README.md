# Freeride Game
#### Created by ECE180D Team 4: Yunxuan Helena Zhang, Yonghao Wu, Elijah Ellsberry, Edward Hage  

# Project Overview
### You can find our leaderboard website [here!](https://freeride-leaderboard.herokuapp.com/)

Freeride is a mountain bike simulation that provides an engaging and interactive gaming experience for bikers and adventurers alike!
The game incorporates computer vision-based pose detection coupled with a custom wireless controller constructed using real mountainbike handlebars in order to create a sense of realistic steering in-game. The game may also be controlled using a traditional keyboard setup. In order to win, the player must navigate down a treacherous mountain terrain through highlighted rings before time runs out! Starting the game is as simple as saying "START" into your computer's microphone at the main menu or clicking the button to start playing!  

# Requirements

* PC running Windows 10
    * Webcam and Microphone Recommended
* Internet Connection
* Keyboard and Mouse
* Download the zipped version of the latest version of the full game(freeride_OG) or the pro extension(pro_extension) from [here](https://drive.google.com/drive/folders/1TNyI20opnT0iORDcK3ohroQoQwGf5iiG?usp=sharing)
* Miniconda(TO DELETE)
    * you can install it [here](https://docs.conda.io/en/latest/miniconda.html)

### If using custom controller

* Raspberry PI Zero WH
* MicroSD Card
    * Minimum of 4GB to install the requisite Raspbian image
* BerryIMUv3
* 4 Pin JST SH Cable such as [this one](https://www.adafruit.com/product/4397)
* A method of powering the Raspberry Pi
    * External battery bank recommended but you can plug into PC as well
* A set of bike handlebars to make using the controller easier (Recommended)
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

### Cloning the repository

##### On your PC
* Use file explorer or CMD to the location you want the repository to be installed to
    * If using file explorer, you can hold shift and right click in the desired folder and click "Open Command Window Here" or "Open Powershell Window Here"
* Run the command
```
    git clone https://github.com/180D-FW-2021/Team4
```

### Raspberry PI setup

Download the latest version of our Raspbian image [here](https://drive.google.com/file/d/1xR5fUs9Dn2AiZSrX5KjP963uS0IBcHe7/view?usp=sharing)!
Once downloaded, insert your SD card into your PC and use an imaging software of your choice to burn the image to your SD card. Instructions for each are below. We recommend [Raspberry PI Imager](https://downloads.raspberrypi.org/imager/imager_latest.exe) or [BalenaEtcher](https://github.com/balena-io/etcher/releases/download/v1.7.7/balenaEtcher-Portable-1.7.7.exe?d_id=9cccbf8a-2c5a-45c8-905c-2a206ba5e6d4R).

#### Installing image

###### Raspberry PI Imager

* Insert your SD card
* Select Custom Image from the Operating System dropdown box
* Choose the freeride_image from where you downloaded it to
* Select your SD card from the Storage dropdown box
* Click **Write**

###### BalenaEtcher

* Insert your SD card
* Unzip the freeride_image that you downloaded earlier by clicking "extract all" inside the zipped folder
* Choose the unzipped freeride_image image file
* Select the SD card
* Click **Burn** and wait for the progress bar to finish

#### Raspberry PI first-time setup

* Insert your micro SD card back into your Raspberry PI.
* Connect your Raspberry PI to your PC using a Micro USB cable. Make sure you are connecting to the port labeled "USB" **NOT** the one marked "PWR", this is the port closer to the center of the Raspberry PI. 
* The on-board LED will flash green for a moment, wait to proceed until you see the green light mostly stop blinking.
* Open the controls folder found inside Team4.
* Double click on **first_time_setup.bat**. Note that if using the same controller with multiple PCs, you must run this script each time you change to a different one.
* When prompted for a password, type the word "free"
* Once the terminal window closes, disconnect your Raspberry PI from its power.

### Windows setup

Make sure that you run the following commands in the directory where you want to save the project

Run the following commands on your host PC:
```
    cd Team4
    cd controller
    conda create -n yourenvnamehere python=3.9
    conda activate yourenvnamehere
    pip install mediapipe==0.8.4
``` 
Using SSH on your Raspberry PI, run the following:
```
    git clone https://github.com/180D-FW-2021/Team4
    cd Team4
    cd controller
```

Run the following:
```
    sudo pip install smbus2==0.4.0
```
On your PC, run the following command:
```
    python receiver.py
```    
Back on the Raspberry PI, run the following:
```
    sudo python berryIMUKalmanBluetooth.py
```
You should begin to see output like the following:  

![Output of receiver.py](/images/output.png)

You may now launch the game and begin playing by double clicking on Freeride.exe

    
# Game Rules

### Control Method
Each time a player is spawned, the default input method is the IMU controller. If you're using a keyboard, simply press [k] right after spawning. You can also press [k] again to change back to IMU control.

### Solo Mode

* After entering the game scene, click the [Host(Server+Client)] button in the top left corner to spawn your player.
![Host/client Options](/images/ss1.png)
* To win the game, collect all 3 checkpoint rings before the timer runs out. There are also little Christmas-themed objects along the way that you can feel free to explore.
* If you're successful, you may press [TAB] to open up the leaderboard menu. Type your name in the box, click send, and click done! Your run should now be integrated into the [leaderboard site](https://freeride-leaderboard.herokuapp.com)

**Important:** Remember to [Stop Host/Client] at the end of a round.

### Duo Mode

* As the first player, click the [Host(Server+Client)] button.
* After the first player has established server, the second player can enter the hostname in the input field (saying localhost by default), then click [Client] to connect to the game.
* The Host address can be found using command "ipconfig /all". Look for the IPv4 Address.
* Now the two players can ride around in the same game!
* The duo mode has no checkpoints. Players can freely explore around the mountain, enjoy the view, while gathering the Christmas-themed collectibles.
* The collectibles are now each worth 100 points; you could work together to gain points before the clock runs out - or you could just play around :D

**Important:** Remember to [Stop Host/Client] at the end of a round.

### Voice Commands

* "Solo": to start solo mode
* "Duo": to start duo mode
* "stop": to pause the game and open the pause menu
* "go back": to close the pause menu and resume the game
* "Reset": to go back to main menu
* "Restart": to restart current level
