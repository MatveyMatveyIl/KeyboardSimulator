from pynput import keyboard


class Keyboard:
    def __init__(self):
        pass

    def pressed_key(self, key):
        pass


def on_release(key):
    print('key release {}'.format(key))


board = keyboard.Controller()
keyboard.Controller().release(keyboard.Key.space)
