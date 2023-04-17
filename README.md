# RM_UBN5
Read battery charging level from Riese und Mueller UBN5 (6/7) and send via MQTT  

This is a very simple project for RM bike owners (other brands may actually work, as long as they comply with the basic BT standards).  
I am using this for my RM UBN5. Please note, that this will only work, when your bike is either switched on or charging. I am using this to switch off the charger at a specified charging level.  

What you need:
A linux computer (i.e. Raspbery PI) in the vicinity (same room at least) of your bike. A PI Zero will do.  
Node-Red on the same computer  

how to:
place the python file in your home dir  
Adjust the BT-MAC adress in line 12 to the one of your bike (see comment in file)  
install python dependencies (bleak and asyncio)  
Import the attached sample flow into your node-red

start playing :)
