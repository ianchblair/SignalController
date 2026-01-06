#
# signal_lights.py
#
# Ian Blair
#
# Designed to use MERG CBUS Library (Duncan Greenwood and others)
# Class for coroutine to control signal lights
#

import pindefs_Pico0203 as pins
import rlysigdefs as rsdefs
from machine import Pin,Timer
import uasyncio as asyncio

import aiorepl
import logger



class signal_lights():
        
    def __init__(self):
        super().__init__()
        self.logger = logger.logger()
        self._signal = []
        #self._signal_pins = []
                
    
    def create_signals(self, signals):
        for j in range(len(signals)):
            self._signal.append(signals[j])
            # Each signal definitions is a dictionary ofaspect definitions
            # We extract a list from the dictionary values and use this to set up the outputs
            # Use of exceptions to trap duplicate pin definitions is TBA
            # signals is a list of dictionaries, so a loop won't work
            # unless we extract the pin definitions (values) from the dictionaries
            # and we also convert the iterables to a list
            sigpins = list(signals[j].values())
            for i in range (len(sigpins)):
                Pin(sigpins[i],Pin.OUT)
            
             
    def set_signal(self, signal_id, aspect):
        # signal numbers assumed to start from zero, and hence provide a list index
        # This needs to be checked
        # Indexes above the size of the signal table are ignored (maybe an exception to add?)
        if (signal_id < len(self._signal)):
            sigdef = self._signal[signal_id]
            sigpins = list(sigdef.values())
            for i in range (len(sigpins)):
                sigpins[i].value = _LED_OFF
                
            # Convert aspect to dictionary name
            aspects = list(rsdef.aspects)
            aspect_name = aspects[aspect]

            if (aspect_name in sigdef):
                sigdef[aspect_name].value = _LED_ON
                sigdef.pop(aspect_name)
            
            if (aspect_name == rsdefs.ASPECT_DOUBLE_YELLOW):
                # find entry for yellow and turn this LED too
                d = sigdef.pop(rsdefs.ASPECT_YELLOW)
                d.value = _LED_ON
            

    def clear_signal(self, signal_id):
        if (signal_id < len(self._signal)):
            sigdef = self._signal[signal_id]     
            sigpins = list(sigdef.values())
            for i in range (len(sigpins)):
                sigpins[i].value = _LED_OFF 
           
            #Can have fading and flashing states too - for FFS 


                            
print('*** End of signal lights file ***')
