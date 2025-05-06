### FaradayFightstick
Utilize Hall Effect sensors in an open-source leverless.

Use an ATMEGA microcontroller to read the analog out from the hall effect sensor located on the opposite side of the PCB from the switch. Then, the ATMEGA will act as the switch and output high or low to a Brooks board for each button press.

There are board versions for a RP2040, Brooks P5 Mini and Brooks Gen-5X Mini. I have tested the RP2040 and P5 Mini versions and they both work on PC.
## Setup
The board is relatively simple to set up - the most difficult part was soldering the USB-C for the ATMEGA32u4. I have no reflow oven so I used my conventional oven with solder paste, which works but is a little difficult to get the timing right to not melt the plastic in the connector.

Once all components are soldered, burn the Arduino bootloader with the "Arduino as ISP" option with an Arduino Uno or equivalent, or another bootloader burner, connected to the ICSP headers on the ATMEGA32u4 which are broken out for convenience, set to an Arduino Micro as the target. Then, plug in the USB-C and upload the ADC.ino sketch.

Once uploaded, unplug and hold LP while plugging back in and run the configurator python script (to be wrapped into an exe later). It should automatically detect the controller. If not, select the COM port corresponding to your board (should say COMXX: Arduino Micro), and click Connect. The progress bar will fill as the default values are read from memory. Set the values using the sliders and click "Submit New Thresholds". Wait for the progress bar to fill and then you can unplug.

Unplug from the ATMEGA side and plug the controller into your computer. If using the RP2040 board, upload the GP2040-CE firmware. Once done, you should be good to go!

There is compatibility for a MagicBoots with the RP2040 board but I have not tested it nor the P5 mini or Gen-5X versions as I don't own a PS5. Always open to donations :)
## TODO
- [ ] Test the P5 Mini version on a PS5.
- [x] Add an "unpressed" level so users have an idea of what range of value to put in
- [x] Add a diode on the voltage input from each USB socket to prevent backflow of current to the host PC and damaging it

## Changelog
# v1.1 (5/5/2025)
- Added boards for P5 mini and Gen-5X mini
- Added current-blocking diodes to prevent blowing up your USB if plugged into both USB ports at the same time
- Updated ADC firmware to support additional commands:
  - GETALLVAL;: get all current button values.
  - GETALLTRIG;: get all trigger threshold levels.
  - GETTRIG;XX: get a singular trigger threshold from memory.  XX indicates the memory offset to read from.
  - LP;X, MP;X, HP;X, SHP;X,...: Sets the trigger threshold value to X in absolute units.
- Updated interface software to use sliders from 100 to 0 to set the sensitivity. 100 is max sensitivity, 0 is no sensitivity.
- Software will try and auto-detect the controller when plugged in. 
# v1.0 (3/6/2025)
The leverless is working! I wrote a quick interface with Python to read and write button trigger thresholds to the EEPROM. The system works as an official "1.0"!
