#
# crossing_lights.py
#
# Ian Nlair
#
# Designed to use MERG CBUS Library (Duncan Greenwood and others)
# Class for coroutine to control warning lights
#

import pindefs_Pico0203 as pindefs
import rlysigdefs as rsdefs
from machine import Pin,Timer
import uasyncio as asyncio

import aiorepl
import logger


class signal_lights():
    
    def __init__(self):
        super().__init__()
        self.logger = logger.logger()
                
    def _init_signal_head(self, sigpins):
        for i in range (len(sigpins)):
            self._signal_pin[i] = Pin(pins[i],Pin.OUT)
            #try self._signal_pin[i] = Pin(pins[i],Pin.OUT)  
    
    def create_signals(self, signals):
        for j in range(len(signals)):
            signal = signals[j]
            self._init_signal_head(signal)
             
    def set_signal(self, signal, aspect):
        for j in range (len(sigdefs)):
            sigdef = sigdefs[j]
            pins = _saved_pins[signal]
            for i in range (len(pins)):
                #get pin table for this signal
                if (aspect == _RED): self._signal_pin[rsdefs._red_aspect_led].value = _LED_ON
                else: self._signal_pin[rsdefs._red_aspect_led].value = _LED_OFF
                if (aspect == _GREEN): self._signal_pin[rsdefs._green_aspect_led].value = _LED_ON
                else: self._signal_pin[rsdefs._green_aspect_led].value = _LED_OFF            
                if (aspect == _YELLOW): self._signal_pin[rsdefs._yellow_aspect_led].value = _LED_ON
                else: self._signal_pin[rsdefs._yellow_aspect_led].value = _LED_OFF 
                if (aspect == _DOUBLE_YELLOW):
                    self._signal_pin[rsdefs._yellow_aspect_led].value = _LED_ON
                    self._signal_pin[rsdefs._dyellow_aspect_led].value = _LED_ON
                else: self._signal_pin[rsdefs._dyellow_aspect_led].value = _LED_OFF 
                if (aspect == _FEATHER):
                    self._signal_pin[rsdefs._feather_aspect_led].value = _LED_ON
                else: self._signal_pin[rsdefs._feather_aspect_led].value = _LED_OFF             
                #Can have fading and flashing states too - for FFS 

    def clear_signal(self, signal):
        pins = _saved_pins[signal]
        for i in range (len(pins)):
            self._signal_pin[i].value = _LED_OFF

            
            #Can have fading and flashing states too - for FFS 


                            
print('*** End of signal lights file ***')
