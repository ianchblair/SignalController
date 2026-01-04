# Definitions for IB Pico projects
# Signals using a 16 output interface

import pindefs_Pico0203 as pins

#Array of the above
#PIN_OPS = [PIN_OP_0, PIN_OP_1, PIN_OP_2, PIN_OP_3, PIN_OP_4, PIN_OP_5, PIN_OP_6, PIN_OP_7,PIN_OP_8, PIN_OP_9, PIN_OP_10, PIN_OP_11, PIN_OP_12, PIN_OP_13, PIN_OP_14, PIN_OP_15]


# These for multiple types of the same signal
#
# Here for "single" aspect signals
# These are represented by one output that is active when the RED aspect is selected for that signal
#

SIG1A1 = dict(_red_aspect_led=pins.PIN_OP_0)
SIG1A2 = dict(_red_aspect_led=pins.PIN_OP_1)
SIG1A3 = dict(_red_aspect_led=pins.PIN_OP_2)
SIG1A4 = dict(_red_aspect_led=pins.PIN_OP_3)
SIG1A5 = dict(_red_aspect_led=pins.PIN_OP_4)
SIG1A6 = dict(_red_aspect_led=pins.PIN_OP_5)
SIG1A7 = dict(_red_aspect_led=pins.PIN_OP_6)
SIG1A8 = dict(_red_aspect_led=pins.PIN_OP_7)
SIG1A9 = dict(_red_aspect_led=pins.PIN_OP_8)
SIG1A10 = dict(_red_aspect_led=pins.PIN_OP_9)
SIG1A11 = dict(_red_aspect_led=pins.PIN_OP_10)
SIG1A12 = dict(_red_aspect_led=pins.PIN_OP_11)
SIG1A13 = dict(_red_aspect_led=pins.PIN_OP_12)
SIG1A14 = dict(_red_aspect_led=pins.PIN_OP_13)
SIG1A15 = dict(_red_aspect_led=pins.PIN_OP_14)
SIG1A16 = dict(_red_aspect_led=pins.PIN_OP_15)



# Here for two aspect signals
SIG2A1 = dict(_red_aspect_led=pins.PIN_OP_0, _green_aspect=pins.PIN_OP_1)
SIG2A2 = dict(_red_aspect_led=pins.PIN_OP_2, _green_aspect=pins.PIN_OP_3)
SIG2A3 = dict(_red_aspect_led=pins.PIN_OP_4, _green_aspect=pins.PIN_OP_5)
SIG2A4 = dict(_red_aspect_led=pins.PIN_OP_6, _green_aspect=pins.PIN_OP_7)
SIG2A5 = dict(_red_aspect_led=pins.PIN_OP_8, _green_aspect=pins.PIN_OP_9)
SIG2A6 = dict(_red_aspect_led=pins.PIN_OP_10, _green_aspect=pins.PIN_OP_11)
SIG2A7 = dict(_red_aspect_led=pins.PIN_OP_12, _green_aspect=pins.PIN_OP_13)
SIG2A8 = dict(_red_aspect_led=pins.PIN_OP_14, _green_aspect=pins.PIN_OP_15)



# Here for two aspects requiring complementary outputs
# These have two outputs, where one is complementary to the other, and a second pair for the complementary output
# (e.g. for DCC ground signals)
# The complementary outputs are in the second block, so, like two aspects, but with different pairings.

    
SIG2C1 = dict(_red_aspect_led=pins.PIN_OP_0,
              _green_aspect_led=pins.PIN_OP_1,
              _not_red_aspect_led=pins.PIN_OP_8,
              _not_green_aspect=pins.PIN_OP_9)
SIG2C2 = dict(_red_aspect_led=pins.PIN_OP_2,
              _green_aspect_led=pins.PIN_OP_3,
              _not_red_aspect_led=pins.PIN_OP_10,
              _not_green_aspect=pins.PIN_OP_11)
SIG2C3 = dict(_red_aspect_led=pins.PIN_OP_4,
              _green_aspect_led=pins.PIN_OP_5,
              _not_red_aspect_led=pins.PIN_OP_12,
              _not_green_aspect=pins.PIN_OP_13)
SIG2C4 = dict(_red_aspect_led=pins.PIN_OP_6,
              _green_aspect_led=pins.PIN_OP_7,
              _not_red_aspect_led=pins.PIN_OP_14,
              _not_green_aspect=pins.PIN_OP_15)



# Here for a block of three aspect signals
SIG3A1 = dict(_red_aspect=pins.PIN_OP_0, _green_aspect=pins.PIN_OP_1, _yellow_aspect=pins.PIN_OP_2)
SIG3A2 = dict(_red_aspect=pins.PIN_OP_3, _green_aspect=pins.PIN_OP_4, _yellow_aspect=pins.PIN_OP_5)
SIG3A3 = dict(_red_aspect=pins.PIN_OP_6, _green_aspect=pins.PIN_OP_7, _yellow_aspect=pins.PIN_OP_8)
SIG3A4 = dict(_red_aspect=pins.PIN_OP_9, _green_aspect=pins.PIN_OP_10, _yellow_aspect=pins.PIN_OP_11)
SIG3A5 = dict(_red_aspect=pins.PIN_OP_12, _green_aspect=pins.PIN_OP_13, _yellow_aspect=pins.PIN_OP_14)


# Here for a block of four aspect signals
SIG4A1 = dict(_red_aspect=pins.PIN_OP_0, _green_aspect=pins.PIN_OP_1,
              _yellow_aspect=pins.PIN_OP_2,_dyellow_aspect=pins.PIN_OP_3)
SIG4A2 = dict(_red_aspect=pins.PIN_OP_4, _green_aspect=pins.PIN_OP_5,
              _yellow_aspect=pins.PIN_OP_6,_dyellow_aspect=pins.PIN_OP_7)
SIG4A3 = dict(_red_aspect=pins.PIN_OP_8, _green_aspect=pins.PIN_OP_9,
              _yellow_aspect=pins.PIN_OP_10,_dyellow_aspect=pins.PIN_OP_11)
SIG4A4 = dict(_red_aspect=pins.PIN_OP_12, _green_aspect=pins.PIN_OP_13,
              _yellow_aspect=pins.PIN_OP_14,_dyellow_aspect=pins.PIN_OP_15)

# Here for a four aspect with feather
SIG4B1 = dict(_red_aspect=pins.PIN_OP_0, _green_aspect=pins.PIN_OP_1,
              _yellow_aspect=pins.PIN_OP_2,_dyellow_aspect=pins.PIN_OP_3,
              _feather=pins.PIN_OP_4)
SIG4B3 = dict(_red_aspect=pins.PIN_OP_8, _green_aspect=pins.PIN_OP_9,
              _yellow_aspect=pins.PIN_OP_10,_dyellow_aspect=pins.PIN_OP_11)
SIG4B4 = dict(_red_aspect=pins.PIN_OP_12, _green_aspect=pins.PIN_OP_13,
              _yellow_aspect=pins.PIN_OP_14,_dyellow_aspect=pins.PIN_OP_15)

# Signal definitions for this board
# Examples:-
#SIGS1A = [SIG1A1, SIG1A2, SIG1A3, SIG1A4, SIG1A5, SIG1A6, SIG1A7, SIG1A8,
#          SIG1A9, SIG1A10,SIG1A11,SIG1A12,SIG1A13,SIG1A14,SIG1A15,SIG1A16]
#
#SIGS2A = [SIG2A1, SIG2A2, SIG2A3, SIG2A4, SIG2A5, SIG2A6, SIG2A7, SIG2A8]
#
#SIGS2C = [SIG2C1, SIG2C2, SIG2C3, SIG2C4]
#
#SIGS3A = [SIG3A1, SIG3A2, SIG3A3, SIG3A4, SIG3A5]
#
#SIGS4A = [SIG4A1, SIG4A2, SIG4A3, SIG4A4]
#
#SIGS4A = [SIG4A1, SIG4A2, SIG4A3, SIG4A4]
#
#SIGS4B = [SIG4A1, SIG4A3, SIG4A4]

# We will go for four four-aspect signals here
SIGSDEF = [SIG4A1, SIG4A2, SIG4A3, SIG4A4]
