# This file contains abstractions for the hardware on the board.

from machine import Pin, PWM, random
import espnow, math, micropython, network, time

from .rtttl import RTTTL
from .songs import random_song, song_num

led_pwms = {
    26: PWM(26, freq=1000, duty=0, timer=3),
    25: PWM(25, freq=1000, duty=0, timer=3),
    4: PWM(4, freq=1000, duty=0, timer=3),
    21: PWM(21, freq=1000, duty=0, timer=3),
}


class Button:
    """
    A button that does something when pushed.
    Usage:
        def callback(pin): print("Pushed: %s" % pin)
        button = Button(pin=27, on_push=callback)
    When pushed: "Pushed: Pin(27) mode=IN, PULL_UP, irq=IRQ_FALLING, debounce=0, actTime=0"
    """

    def __init__(self, pin, handler=None, trigger=Pin.IRQ_FALLING, *args, **kwargs):
        self.callback = handler
        self.pin = Pin(
            pin,
            Pin.IN,
            Pin.PULL_UP,
            handler=self.push_handler,
            trigger=trigger,
            *args,
            **kwargs
        )

    def push_handler(self, pin):
        if not self.callback:
            return

        self.callback(pin)

    def disable(self):
        self.pin.init(handler=None, trigger=Pin.IRQ_DISABLE)

    def update(self, *args, **kwargs):
        self.pin.init(**kwargs)


class Buzzer:
    """
    A buzzer that plays musical notes.
    Usage:
        buzzer = Buzzer()
        buzzer.force()
    """

    NOTES = dict(
        c=261,
        d=294,
        e=329,
        f=349,
        g=391,
        gS=415,
        a=440,
        aS=455,
        b=466,
        cH=523,
        cSH=55,
        dH=587,
        dSH=62,
        eH=659,
        fH=698,
        fSH=74,
        gH=784,
        gSH=83,
        aH=880,
    )

    def __init__(self, pin=12):
        self.pwm = PWM(pin, duty=0)

    def tone(self, freq, duration):
        freq = round(freq)
        duration = round(duration * 0.9)
        pause = round(duration * 0.1)

        if freq > 0:
            self.pwm.init(freq=freq, duty=50)

        time.sleep_ms(duration)
        self.pwm.duty(0)
        time.sleep_ms(pause)

    def random_song(self):
        tune = RTTTL(random_song())
        for freq, duration in tune.notes():
            self.tone(freq, duration)

    def play_song_num(self, num):
        tune = RTTTL(song_num(num))
        for freq, duration in tune.notes():
            self.tone(freq, duration)

    def on(self, note):
        self.pwm.init(freq=Buzzer.NOTES[note], duty=50)

    def off(self):
        self.pwm.duty(0)


class LED:
    """
    A single LED connected to a pin.
    Usage:
        led = LED(pin=26)
        led.on()
    """

    def __init__(self, pin=13, buzzer=None, note=None):
        self.pwm = led_pwms[pin]

        self.buzzer = None
        if buzzer and note:
            self.buzzer = buzzer
            self.note = note

    def on(self):
        self.pwm.duty(100)
        if self.buzzer:
            self.buzzer.on(self.note)

    def off(self):
        self.pwm.duty(0)
        if self.buzzer:
            self.buzzer.off()

    def duty(self, n):
        self.pwm.duty(n)

    def blink(self, duration=0.1, times=1):
        while times:
            times -= 1
            self.on()
            time.sleep(duration)
            self.off()

            if times > 0:
                time.sleep(duration)


class Lights:
    """
    A collection of our four LEDs.
    Usage:
        lights = Lights()
        lights.confetti()
        lights[0].blink()
    """

    LED_TR = 0
    LED_BR = 1
    LED_TL = 2
    LED_BL = 3

    def __init__(self, sync_with_buzzer=None):
        led_pins = [26, 25, 4, 21]  # top right, bottom right, top left, bottom left
        buzzer_notes = ["a", "b", "d", "g"]

        self.leds = [
            LED(pin, buzzer=sync_with_buzzer, note=note)
            for pin, note in zip(led_pins, buzzer_notes)
        ]
        self.buzzer = sync_with_buzzer

    def __getitem__(self, key):
        return self.leds[key]

    def __len__(self):
        return len(self.leds)

    def fade_in(self, led_nums, speed=1):
        leds = [self.leds[i] for i in led_nums]
        # some magic numbers that make the math work
        for i in range(15, 26):
            d = ((int(math.sin(i / 10 * math.pi) * 500 + 500)) / 1024.0) * 100.0
            for led in leds:
                led.duty(d)
            time.sleep_ms(round(50 * (1 / speed)))

    def fade_out(self, led_nums):
        leds = [self.leds[i] for i in led_nums]
        for i in range(26, 36):
            d = ((int(math.sin(i / 10 * math.pi) * 500 + 500)) / 1024.0) * 100.0
            for led in leds:
                led.duty(d)
            time.sleep_ms(20)

    def opponent_found(self):
        self.fade_in([self.LED_BR])
        time.sleep(1)
        self.fade_out([self.LED_BR, self.LED_BL])

    def cycle(self, times=1):
        while times:
            times -= 1

            for led in self.leds:
                led.blink()

            time.sleep(0.1)

            for led in reversed(self.leds):
                led.blink()

            time.sleep(0.1)

    def confetti(self, times=50):
        last_led = None
        while times:
            times -= 1
            # randomly pick an led that is different from the last one that flashed
            all_leds_except_last = [led for led in self.leds if led != last_led]
            last_led = all_leds_except_last[random(0, len(all_leds_except_last) - 1)]
            last_led.blink()

    def all_blink(self, times=5):
        while times:
            times -= 1
            time.sleep(0.3)
            for led in self.leds:
                led.on()
            time.sleep(0.3)
            for led in self.leds:
                led.off()

    def all_off(self):
        for led in self.leds:
            led.off()

    def all_on(self):
        for led in self.leds:
            led.on()

    def chase(self, times=1):
        while times:
            times -= 1
            self[0].blink()
            time.sleep(0.01)
            self[1].blink()
            time.sleep(0.01)
            self[3].blink()
            time.sleep(0.01)
            self[2].blink()
            time.sleep(0.01)


# Unfortunately, this needs to be defined as a global variable to avoid
# random core panics upon some ESP NOW callbacks
espnow_callback_fn = None


class WiFi:
    """
    Wraps board-to-board wireless comms (including ESPNOW) into a nicer API.
    """

    BROADCAST_ADDR = b"\xFF" * 6

    def __init__(self):
        self.wlan = network.WLAN(network.AP_IF)
        self.peer_list = []

        global espnow_callback_fn
        espnow_callback_fn = self.on_espnow_message

        self.msg_callback = None

    def on(self):
        global espnow_callback_fn

        self.wlan.active(True)
        self.wlan.config(channel=1)
        self.wlan.config(protocol=network.MODE_LR)

        espnow.init()
        espnow.set_pmk("0123456789abcdef")
        espnow.set_recv_cb(espnow_callback_fn)
        self.add_espnow_peer(WiFi.BROADCAST_ADDR)

    def off(self):
        espnow.deinit()
        self.wlan.active(False)
        self.peer_list = []

    def send_message(self, mac, body):
        self.log("->msg send %s (from %s)" % (body, mac))

        self.add_espnow_peer(mac)
        text = "r00tz27 %s" % body
        espnow.send(mac, text)

    def broadcast(self, body):
        text = "r00tz27 %s" % body
        espnow.send(WiFi.BROADCAST_ADDR, text)

    def on_espnow_message(self, message):
        self.log("<-on_espnow_message: scheduling callback")
        if not self.msg_callback:
            self.log("<-on_espnow_message: no callback")
            return
        micropython.schedule(self.msg_callback, message)
        self.log("<-on_espnow_message: callback scheduled")

    def add_espnow_peer(self, addr):
        if addr in self.peer_list:
            return

        self.peer_list.append(addr)

        try:
            espnow.add_peer(self.wlan, addr)
        except OSError as err:
            if str(err) == "ESP-Now Peer Exists":
                # this error means the opponent mac is already in the peer list,
                # which is fine, so we can continue
                pass
            else:
                # some other unexpected OSError
                raise

    def register_msg_callback(self, callback):
        self.msg_callback = callback

    def clear_callback(self):
        self.msg_callback = None

    def log(self, s):
        print("%s\t%s" % (time.time(), s))
