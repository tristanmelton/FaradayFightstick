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
