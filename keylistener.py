from Xlib.display import Display
from Xlib import X
from Xlib.ext import record
from Xlib.protocol import rq
import time

disp = None

keysym_map = {
    32: "SPACE",
    39: "'",
    44: ",",
    45: "-",
    46: ".",
    47: "/",
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    59: ";",
    61: "=",
    91: "[",
    92: "\\",
    93: "]",
    96: "`",
    97 :"a",
    98 :"b",
    99 :"c",
    100: "d",
    101: "e",
    102: "f",
    103: "g",
    104: "h",
    105: "i",
    106: "j",
    107: "k",
    108: "l",
    109: "m",
    110: "n",
    111: "o",
    112: "p",
    113: "q",
    114: "r",
    115: "s",
    116: "t",
    117: "u",
    118: "v",
    119: "w",
    120: "x",
    121: "y",
    122: "z",
    65293: "ENTER",
    65307: "ESC",
    65360: "HOME",
    65361: "ARROW_LEFT",
    65362: "ARROW_UP",
    65363: "ARROW_RIGHT",
    65505: "L_SHIFT",
    65506: "R_SHIFT",
    65507: "L_CTRL",
    65508: "R_CTRL",
    65513: "L_ALT",
    65514: "R_ALT",
    65515: "SUPER_KEY",
    65288: "BACKSPACE",
    65364: "ARROW_DOWN",
    65365: "PG_UP",
    65366: "PG_DOWN",
    65367: "END",
    65377: "PRTSCRN",
    65535: "DELETE",
    65383: "PRINT?",
    65509: "CAPS_LOCK",
    65289: "TAB",
    65470: "F1",
    65471: "F2",
    65472: "F3",
    65473: "F4",
    65474: "F5",
    65475: "F6",
    65476: "F7",
    65477: "F8",
    65478: "F9",
    65479: "F10",
    65480: "F11",
    65481: "F12"

}

class KeyListener(object):
    def __init__(self):
        """Really simple implementation of a keylistener

        Simply define your keyevents by creating your keylistener obj,
        and then calling addKeyListener("keycombination", callable)

        Keycombinations are separated by plus signs:
        examples:

        >>> keylistener = KeyListener()
        >>> keylistener.addKeyListener("L_CTRL+L_SHIFT+y", callable)
        >>> keylistener.addKeyListener("b+a+u+L_CTRL", callable)
        >>> keylistener.addKeyListener("a", callable)

        ex:

        >>> keylistener = KeyListener()
        >>> def sayhi():
                print "hi!"
        >>> keylistener.addKeyListener("L_CTRL+a", sayhi)

        from this moment on, python will execute sayhi every time you press
        left ctrl and a at the same time.

        Keycodes can be found in the keysym map above.
        """
        self.pressed = set()
        self.listeners = {}

    def press(self, character):
        """"must be called whenever a key press event has occurred
        You'll have to combine this with release, otherwise
        keylistener won't do anything
        """
        self.pressed.add(character)
        action = self.listeners.get(tuple(self.pressed), False)
        print "current action: " + str(tuple(self.pressed))
        if action:
            action()

    def release(self, character):
        """must be called whenever a key release event has occurred."""
        if character in self.pressed:
            self.pressed.remove(character)

    def addKeyListener(self, hotkeys, callable):
        keys = tuple(hotkeys.split("+"))
        print "Added new keylistener for : " + str(keys)
        self.listeners[keys] = callable

keylistener = KeyListener()

def keysym_to_character(sym):
    if sym in keysym_map:
        return keysym_map[sym]
    else:
        return sym

def handler(reply):
    """ This function is called when a xlib event is fired """
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, disp.display, None, None)

        keycode = event.detail
        keysym = disp.keycode_to_keysym(event.detail, 0)

        if keysym in keysym_map:
            character = keysym_to_character(keysym)
            print character
            if event.type == X.KeyPress:
                keylistener.press(character)
            elif event.type == X.KeyRelease:
                keylistener.release(character)

def start():
    # get current display
    disp = Display()
    root = disp.screen().root

    # Monitor keypress and button press
    ctx = disp.record_create_context(
                0,
                [record.AllClients],
                [{
                        'core_requests': (0, 0),
                        'core_replies': (0, 0),
                        'ext_requests': (0, 0, 0, 0),
                        'ext_replies': (0, 0, 0, 0),
                        'delivered_events': (0, 0),
                        'device_events': (X.KeyReleaseMask, X.ButtonReleaseMask),
                        'errors': (0, 0),
                        'client_started': False,
                        'client_died': False,
                }])

    disp.record_enable_context(ctx, handler)
    disp.record_free_context(ctx)

    while True:
        time.sleep(.1)
        # Infinite wait, doesn't do anything as no events are grabbed
        event = root.display.next_event()