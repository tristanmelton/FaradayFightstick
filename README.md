### FaradayFightstick
Utilize Hall Effect sensors in an open-source leverless.

Current plan: Use an ATMEGA microcontroller to read the analog out from the hall effect sensor located on the opposite side of the PCB from the switch. Then, the ATMEGA will act as the switch and output high or low to a Brooks board for each button press.

## Current Progress
I will need minimum 15 IO for reading each sensor on it's own, so I need at least 30-total IO. I'm thinking of going for the ATMEGA2560-16AU since it has a ton of available IO and plenty of RAM (256kb). Clock speed is 16-MHz so even in worse case where we only poll a button every 1-MHz or so, that's still 1-us intervals which is faster than the ~8k polling from usual HE sensors.

I need to probe the signals from the brooks board to understand how it's reading button presses. 


## Changelog
# 1/26/2025
I ordered 5x AH1912-FA-7 hall effect sensors to test the output from a random key switch, probably the Gateron Jade. I have not ordered those yet because I am waiting for more money.

Part is here: https://www.amazon.com/GATERON-Magnetic-Pre-lubed-Pre-travel-Mechanical/dp/B0CQXGTJWG

# 1/29/2025
Gateron Jade switches were ordered from Aliexpress because cheap. 

I'm thinking of using the ADS131M08 x2 as the ADCs and interfacing over SPI. My reasoning is that I don't want to have to use the ADC on the ATmega2560 to cycle through every button every time, drastically reducing the response time. This also saves some GPIO on the ATMega2560 and maybe lets me go to a cheaper or smaller chip. I may stay on it though so I can make a webserver to configure the actuation points. 

There's also an Arduino library for interfacing with the ADC chip: https://github.com/tpcorrea/Arduino-ADS131M08
The part is found here: https://www.digikey.com/en/products/detail/texas-instruments/ADS131M08IPBS/11502282

I also realize that the sensor I purchased is a digital switch.... I'll probably get some DRV5053VAQDBZR with the ADCs for a true-analog version. 

Alternate more usable and cheap ADCs:

https://www.mouser.com/ProductDetail/Texas-Instruments/ADS7961SRHBT?qs=DS7Z8uEdLNxNMuexpXCw2g%3D%3D

https://www.mouser.com/ProductDetail/Texas-Instruments/ADC108S022CIMT-NOPB?qs=7X5t%252BdzoRHBC81ZWvn8axQ%3D%3D

# 1/29/2025 PM
I decided to opt for the ADC108S022. I placed two of them and will interface over SPI. I think I may be able to go for a smaller and cheaper main IC rather than the 2560, I'll check how heavy running a webserver off of it is and go from there. Alternatively I could do the programming over USB or something, or maybe a built-in header. I'm not sure on that front yet. 

I've updated the PCB with the aforementioned changes. Technically I think it works as a v1.0 but I'll hold off on calling it that for now.

# 1/30/2025
I swapped the ADC-MCU from USB-micro to USB-C for easier compatibility with other systems. I did some initial PCB layout too - I need to figure out what footprint works with the Gateron Jade Magnetic Pro switches I am getting.

I grabbed the key footprints from here: https://github.com/siderakb/key-switches.pretty 

# 2/3/2025
Swapped over to the ATMEGA32-16U because it has enough pins to do everything I need. I also measured (hopefully accurately) the footprint for the Gateron Jade Magnetic Pro switches and added those into the PCB layout. I ordered a Brooks P5 Mini because there's no public pinout online. Once I get it I'll make a KiCAD footprint for it so people can use it in their designs as well. For now, I added a dummy footprint for the Brooks P5 Pro as a stand-in.

I may order the hall effect sensors soon - the Gaterons came in and from my phone, there was about 2-mT of magnetic differential from pushed to not pushed, which is ~1/4 the sensing range of the hall effect switch. This was with the few-mm standoff from the little plastic pins on the switch, plus through my phone so probably will be stronger than 2-mT on the actual board. I'll probably order in the next day or so. 

I still need to probe my Brooks board and see how the output voltage looks like... I suspect its just pulling a pin to ground which will be easy to replicate but I don't want to assume anything.