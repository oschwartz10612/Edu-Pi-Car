# Educational Webserver Pi Car Implementation
A getting started guide to build a Raspberry Pi web controlled robot. This is intented as a jumping off point depending on your platform.

## Installation
Update Raspbian Repositories
```bash
sudo apt-get update
```

Install git
```bash
sudo apt-get intall git
```

Install pip
```bash
sudo apt-get install python-pip
```

Use git to clone this repository to your Raspberry Pi robot

```bash
git clone https://github.com/oschwartz10612/Edu-Pi-Car.git
```

Install Flask

```bash
pip install Flask
```

Install Flask Socket.io
```bash
pip install flask-socketio
```
**Before we can install Motion, you need to connect your webcam or pi camera.**

Install Motion
```bash
sudo apt-get update

sudo apt-get install motion
```

Set Motion daemon to 'yes'
```bash
sudo nano /etc/default/motion
```

![img1](/assets/enable-motion-daemon-for-Raspberry-Pi-Surveillance-Camera.gif)

Then save the file by pressing ‘CTRL+X’, then ‘Y’ and then Enter.

Now we need to set the permission for the Target Directory (/var/lib/motion/), in which Motion saves all the Video recordings and picture files. We need to set ‘Motion’ as the owner of this directory by issuing below command:
```bash
sudo chown motion:motion /var/lib/motion/
```

Now we are almost done, only we need to change one config option in Motion configuration file (/etc/motion/motion.conf) which is stream_localhost off. We have to turn off this local host streaming, otherwise we will not be able to access the Video feed on our network and it will be only accessible from the Raspberry Pi itself. To doing so, edit the Motion Configuration file with ‘nano’ editor and turn it off, like shown below:
```bash
sudo nano /etc/motion/motion.conf
```
![img2](/assets/setting-motion-cofig-file-for-Raspberry-Pi-Surveillance-Camera.gif)

Finally, restart the service
```bash
sudo /etc/init.d/motion restart
```
Jump to the "Drive your car!" section to learn how to connect to the Pi and run the server. Do this before you edit your code to make sure everything is working!

You should see an output like the following on your terminal when you press the keys
```bash
192.168.1.201 - - [17/Nov/2018 14:55:46] "POST /socket.io/?EIO=3&transport=polling&t=1542484543891-30&sid=134e5180d7ea4b439297efb9d5c02b51 HTTP/1.1" 200 -
down
192.168.1.201 - - [17/Nov/2018 14:55:46] "POST /socket.io/?EIO=3&transport=polling&t=1542484543961-31&sid=134e5180d7ea4b439297efb9d5c02b51 HTTP/1.1" 200 -
up
192.168.1.201 - - [17/Nov/2018 14:55:46] "POST /socket.io/?EIO=3&transport=polling&t=1542484544016-32&sid=134e5180d7ea4b439297efb9d5c02b51 HTTP/1.1" 200 -
left
192.168.1.201 - - [17/Nov/2018 14:55:46] "POST /socket.io/?EIO=3&transport=polling&t=1542484544027-33&sid=134e5180d7ea4b439297efb9d5c02b51 HTTP/1.1" 200 -
right
192.168.1.201 - - [17/Nov/2018 14:55:47] "POST /socket.io/?EIO=3&transport=polling&t=1542484544154-34&sid=134e5180d7ea4b439297efb9d5c02b51 HTTP/1.1" 200 -
up
```

## Usage

Enter the directory of the code
```bash
cd Edu-Pi-Car/
```
Open the run.py file
```bash
sudo nano run.py
```
Edit the code under the blocks to make your car drive
```python
@socketio.on('left')
def left():
    #code to turn left
    print('left')
```
In the example above, you would replace the "#code to turn left" with your code to make the robot move. Make sure to keep the indent.

## Drive your car!
Enter the directory of the code
```bash
cd Edu-Pi-Car/
```

Find your Pi's IP address
```bash
hostname -I
```

Run the code by entering
```bash
python run.py
```

Go to a computer on the same network and connect to the Raspberry Pi by typing its IP address into the address bar followed by ':5000' For example: http://192.168.1.12:5000

You should then see the a page with the view from the webcam. Press the arrow keys, and if your code works, the car should drive!

## Explanation
The Flask app serves a static HTML file to the client when they connect to the server. Javascript on the client side connects using a socket connection to the server. When the client detects a press of the arrow keys, it sends that data to the server over the socket. The server then runs your code to make the car move.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
