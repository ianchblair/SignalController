#
# module_signal_control.py
#
# Controls outputs for 0in16out Pico02 with mezz08, or Pico03 board using asyncio library
#
# (c) Ian Blair 13 Nov 2025
#
#

import uasyncio as asyncio
from machine import Pin,SPI
import pindefs_Pico0203 as pins
import rlysigdefs as sigs
import signal_lights as sl

import aiorepl
import cbus
import cbusconfig
import cbusdefs
import cbusmodule
import logger
import mcp2515



class mymodule(cbusmodule.cbusmodule):
    def __init__(self):
        super().__init__()
        self.logger = logger.logger()
        self._event_led = Pin(pins.PIN_LED_RED, Pin.OUT)

    def initialise(self):

        # ***
        # *** Module init
        # ***
        # SPI pin configuration from pindefs
        bus = SPI(
            1,
            baudrate=10_000_000,
            polarity=0,
            phase=0,
            bits=8,
            firstbit=SPI.MSB,
            sck=Pin(pins.PIN_CAN_CLK),
            mosi=Pin(pins.PIN_CAN_MOSI),
            miso=Pin(pins.PIN_CAN_MISO),)
        self.cbus = cbus.cbus(
            mcp2515.mcp2515(osc=16_000_000, cs_pin=pins.PIN_CAN_CS0, interrupt_pin=pins.PIN_CAN_INT1, bus=bus),
            cbusconfig.cbusconfig(storage_type=cbusconfig.CONFIG_TYPE_FILES),
        )

        # ** change the module name and ID if desired

        self.module_id = 99
        self.module_name = bytes('SIGS   ', 'ascii')
        self.module_params = [
            20,
            cbusdefs.MANU_MERG,
            0,
            self.module_id,
            self.cbus.config.num_events,
            self.cbus.config.num_evs,
            self.cbus.config.num_nvs,
            1,
            # Parameter below sets PF flags. 6 sets Consumer and Producer node, 
            # but only Consumer node functionality is implemented so far.
            6,
            0,
            cbusdefs.PB_CAN,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
        
        # *** Instantiate and populate signal light classes
        self.sig = sl.signal_lights()
        #
        self.sig.create_signals(sigs.SIGSDEF)

        # change the CBUS switch and LED pin numbers if desired

        self.cbus.set_leds(pins.PIN_LED_GRN,pins.PIN_LED_YEL)
        self.cbus.set_switch(pins.PIN_SW1)
        self.cbus.set_name(self.module_name)
        self.cbus.set_params(self.module_params)
        self.cbus.set_event_handler(self.event_handler)
        self.cbus.set_received_message_handler(self.received_message_handler)
        self.cbus.set_sent_message_handler(self.sent_message_handler)

        self.cbus.begin()

        # ***


        self._event_led.value(0) 
        
        # *** module initialisation complete
        self.logger.log(f'module: name = <{self.cbus.name.decode()}>, mode = {self.cbus.config.mode}, can id = {self.cbus.config.canid}, node number = {self.cbus.config.node_number}')
        self.logger.log(f'free memory = {self.cbus.config.free_memory()} bytes')

        
        # *** end of initialise method
        
          # ***
    # *** CBUS event handler -- called whenever a previously taught event is received
    # *** when teaching, set the value of EV1 to select the signal to control (0-7)
    # *** EV2 contains the required aspect
    # ***

    def event_handler(self, msg: canmessage.canmessage, idx: int) -> None:
        self.logger.log(f'-- event handler: idx = {idx}: {msg}')

        # lookup the value of the 1st two EVs
        # Check that evs are set up needs to be added!
        ev1 = self.cbus.config.read_event_ev(idx, 1)
        ev2 = self.cbus.config.read_event_ev(idx, 2)
        self.logger.log(f'** idx = {idx}, opcode = {msg.data[0]}, polarity = {"OFF" if msg.data[0] & 1 else "ON"}, ev1 = {ev1}, ev2 = {ev2}')

        # switch the signal aspect according to the event opcode, signal ID, and requested aspect
        # On in this context means new aspect (replaces old aspect)
        # Off is ignored in all cases except single aspect
        # We map the signal ID to ev1
        # (global or local TBD)
        # and aspect to ev2
        # (if ev < 8 not needed?)
        if not (msg.data[0] & 1):  # on events are even numbers
            self.logger.log(f'** Signal {ev1} on')
            self.sig.set(ev2)
            self._event_led.value(1) 
        else:                      # off events are odd numbers
            # Off is only used for single outputs.
            # For other cases a new aspect always replaces the old
            self.logger.log(f'** Signal {ev1} off') 
            self.sig.clear(ev2)
            self._event_led.value(0) 
    # ***


        # *** end of initialise method

    # ***
    # *** coroutines that run in parallel
    # ***
    # *** task to blink the onboard LED
    
    async def blink_led_coro(self) -> None:
        self.logger.log('blink_led_coro start')
        try:
            led = Pin('LED', Pin.OUT)
        except TypeError:
            led = Pin(25, Pin.OUT)

        while True:
            led.value(1)
            await asyncio.sleep_ms(20)
            led.value(0)
            await asyncio.sleep_ms(980)

    # *** user module application task - like Arduino loop()
    async def module_main_loop_coro(self) -> None:
        self.logger.log('main loop coroutine start')
        while True:
            await asyncio.sleep_ms(25)

    # ***
    # *** module main entry point - like Arduino setup()
    # ***

    async def run(self) -> None:
        # self.logger.log('run start')

        # start coroutines
        self.tb = asyncio.create_task(self.blink_led_coro())
        self.tm = asyncio.create_task(self.module_main_loop_coro())

        repl = asyncio.create_task(aiorepl.task(globals()))

        self.logger.log('module startup complete')
        await asyncio.gather(repl)


# create the module object and run it
mod = mymodule()
mod.initialise()
asyncio.run(mod.run())

# the asyncio scheduler is now in control
# no code after this line is executed

print('*** application has ended ***')