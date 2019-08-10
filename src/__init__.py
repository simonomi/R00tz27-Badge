# This is the file that gets executed on boot. At some point,
#  you should have ran the following command on your board:
#    >>> machine.nvs_setstr("system", "default_app", "r00tz27")
#  then, the src/ folder here goes into /lib/r00tz27 on the board,
#  and r00tz27/__init__.py gets run on startup.

from .main import StateMachine
import micropython

# "If an error occurs in an ISR, MicroPython is unable to produce an error report unless a special
# buffer is created for the purpose. Debugging is simplified if the following code is included
# in any program using interrupts."
micropython.alloc_emergency_exception_buf(100)

if __name__ == "r00tz27":
    state_machine = StateMachine(initial_state="awake")
