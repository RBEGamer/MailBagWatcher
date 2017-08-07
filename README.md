# MailBagWatcher
A powerful mailbag watcher with push notification.
The device will be installed inside of you mailbag and waits for a trigger signal eg opening the maildoor.
If the trigger activated, the power will be enabled to boot up a linux pc (omega2 in my case or RPI,..).
Then you have all the power of the linux environment and after you have finished the tasks (send notifications,..) you can shutdown the system. To shutdown you simply have to set the resetpin of the power circuit to HIGH and the system waits for the next trigger.



# This project was featured by the onion.io newsletter 26.08.2017
# https://onion.io/2bt-youve-got-real-mail-notifications/

# PARTS
* Onion Omega 2 (https://onion.io) or Intel Edison, RPI
* 3 NE555 Timer IC (or 1 RS FlipFlop 74xx107 and 2 nor gates 74x2G02)
* LowVoltage StepUpConverter
* double AA Battery Holder
* 1 (best toggle) reedswitches
* LogicLevel Mosfet or Transistor (>= 400mA)
* 2 Magnets for the reed switches
* 4 pull up resistors 47k-100k
* [optional] 3 push buttons for testing
* [optional] 2 leds for status indication
* wires, headers,..

# TOOLS
* soldering stuff
* hotglue
* [optional] 3D Printer for case


# BUILD HARDWARE
All shown ICs are the NE555 Timer (sorry for the missing caption)

## THE FIRST NOR GATE
To build the nor gate used for inverting the reedswitch state (if you have a toogle reed switch you can skip this step)
A nor gate is really simple to build with the NE555 Timer.
In the chart you can see the logic table

| IN        | OUT           |
| ------------- |:-------------:|
| 0      | 1 |
| 1      | 0      |

Connect `VCC` to pin `8 (vcc)` and `GND` to pin `1 (gnd)` of the Timer IC, this is for all of the Timer ICs we are using the same. So you can build all ic aligned in a collum and connect the same pins.
For the NOR Gate connect pin `2 (trigger)` with pin `6 threshold ` and connect these to `VCC` over a pullup resistor.
Last step connect the pins to `GND` over the (normal open) reedswitch. This reedswitch is your trigger if new mail is avariable.
Pin `3 (output)` is the output to the RS FlipFlop.
![alt text](https://github.com/RBEGamer/MailBagWatcher/blob/master/Documentation/Images/norgate_1.jpg)


## THE SECOND NOR GATE
The second nor gate was a copy of the first nor gate unitl the pull up resistor. The resistor is connected to `GND` instead of `VCC`.
![alt text](https://github.com/RBEGamer/MailBagWatcher/blob/master/Documentation/Images/norgate_2.jpg)


## THE RS FLIP FLOP

![alt text](https://github.com/RBEGamer/MailBagWatcher/blob/master/Documentation/Images/rs_gate.jpg)


## CONNECTING EVERYTHING
![alt text](https://github.com/RBEGamer/MailBagWatcher/blob/master/Documentation/Images/final_front.jpg)
![alt text](https://github.com/RBEGamer/MailBagWatcher/blob/master/Documentation/Images/final_back.jpg)

## [OPTIONAL / IF NEEDED] EXPAND THE WIFI ANTENNA
If you have a metal mailbox youll have to use an external wifiantenna on the omega 2.
The Omega2 has a wifi antenna port on Ebay you will get some adapters for reqular connectors.
If you have a old laptop you often find a good antenna there or you can use a piece of wire of a certain lenght
So the Wifi rund at 2.4Ghz that means you need a odd multible of lambda/4.
Your wire can be for example 3cm or 9.5cm.
Further inforamtion can be found at http://www.dl2jas.com/antennen/antennenimpedanz/antennenimpedanz.html
![alt text](https://github.com/RBEGamer/MailBagWatcher/blob/master/Documentation/Images/omega_extend_wifi.jpg)

# SOFTWARE
At bootup, my mailbagwatcher runs a pythonscript whitch sends a pushnotification over the pushover service, sends a request to my fhem installation and at the end a gpio will set to `1 (HIGH)` to power off the system.
The pushnotification is only an example, you have the complete linux environment for your usage.

## INSTALL PYTHON
Python is not on the omega2 installed by default, so we need to install a python-light version, this will need 8mb from the 14mb of the omega2. To install python you can simply run the commands from `/src/python_omega2_install.sh`. The script will update and install python.

## CREATE SCRIPT AND SET AS STARTUP







# IMAGES

# TODO
Please see `TODO.md`
