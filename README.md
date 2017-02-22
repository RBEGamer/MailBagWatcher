# MailBagWatcher
A powerful mailbag watcher with push notification


# PARTS
* Onion Omega 2 (https://onion.io)
* 3 NE555 Timer IC (or 1 RS FlipFlop 74xx107 and 2 nor gates 74x2G02)
* LowVoltage StepUpConverter
* double AA Battery Holder
* 2 (best toggle) reedswitches
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
The second nor gate was a copy of the first nor gate unitl the pull up resistor. The resistor is connected to `GND` instead of `VCC` and 

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

# IMAGES

# TODO
