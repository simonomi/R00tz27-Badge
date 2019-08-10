import machine, micropython, time

from .devices import Button, Buzzer, LED, Lights, WiFi
from .states import (
    AwakeState,
    DancePartyState,
    SearchingForOpponentState,
    SimonSaysRoundSyncState,
    SimonSaysChallengeState,
    SimonSaysGuessingState,
    SongSelectionState,
)


class StateMachine:
    """
    The core abstraction of the whole board. At all times, the board is in a "State" that
    defines what the buttons do when pushed, and what the board is doing at that moment.

    Each State class defines an enter() method and an exit() method. When the State Machine
    enters a State, it calls the enter() method on that State. When we change state, it calls
    the exit() method on the old State, and then the enter() method on the new State.

    As the overlord of states and state transitions, all hardware devices are properties of,
    and controlled thru, this State Machine.
    """

    def __init__(self, initial_state="awake"):

        # all possible states of the board.
        # we give each state a reference to this state machine object so
        # it can control the state machine's variables (e.g. remap button handlers) and
        # it can call go_to_state to the next state.

        self.states = {
            "awake": AwakeState(state_machine=self),
            "dance_party": DancePartyState(state_machine=self),
            "searching_for_opponent": SearchingForOpponentState(state_machine=self),
            "simon_says_round_sync": SimonSaysRoundSyncState(state_machine=self),
            "simon_says_challenge": SimonSaysChallengeState(state_machine=self),
            "simon_says_guessing": SimonSaysGuessingState(state_machine=self),
	    "song_selection": SongSelectionState(state_machine=self),
        }

        # initialize hardware devices

        self.wifi = WiFi()
        self.wifi.on()

        BUTTON_PINS = [27, 33, 15, 32]
        self.buttons = [
            Button(pin, trigger=machine.Pin.IRQ_ANYEDGE, debounce=10000, acttime=10000)
            for pin in BUTTON_PINS
        ]

        self.buzzer = Buzzer()
        self.lights = Lights(sync_with_buzzer=self.buzzer)
        self.quiet_lights = Lights()

        # we need to setup timer #0 in extended mode to have more timers
        self.tex = machine.Timer(0)
        self.tex.init(mode=machine.Timer.EXTBASE)

        self.state_change_timer = machine.Timer(1)
        self.timer = machine.Timer(2)

        self.current_state = None
        self.next_state = None
        self.callback_fn = self.callback
        self.go_to_state(initial_state)

    def go_to_state(self, name, **kwargs):
        """
        We handle state transitions asynchronously. Rather than stopping anything running
        we give it 20ms before this timer callback fires and forwards the state. This will
        hopefully easily mitigate some nasty race conditions. This also allows us to call
        state_machine.go_to_state within a State's on_enter method without causing problems
        (as long as on_enter finishes in 20ms!)
        """

        # some cleanup first
        self.timer.deinit()

        self.next_state = (name, kwargs)

        micropython.schedule(self.callback_fn, 0)

    def callback(self, timer):
        name, kwargs = self.next_state
        self._go_to_state(name, **kwargs)

    def _go_to_state(self, name, **kwargs):
        """
        Handle a state transition by calling exit() on the old state and enter() on the new.
        
        This method is usually called by the current state to forward us to the new state.
        The current state can pass named arguments to the enter methods of the new state:
          >>> state_machine.go_to_state("my_new_state", arg1=val1, foo=bar)
        """

        old_state_class_name = (
            self.current_state.__class__.__name__ if self.current_state else None
        )
        new_state_class_name = self.states[name].__class__.__name__
        print(
            "%s\t transition %s -> %s"
            % (time.time(), old_state_class_name, new_state_class_name)
        )

        if self.current_state:
            self.current_state.exit()  # call the exit() method on the old state

        self.current_state = self.states[name]
        self.current_state.__init__(state_machine=self)
        self.current_state.enter(**kwargs)  # call enter() on the new state
