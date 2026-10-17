import pygame
import time
import threading
import sys
from pynput import keyboard
from pystray import Icon, Menu, MenuItem
from PIL import Image

# File paths - update if needed
mp3 = r"C:\Users\x\Documents\ok_garmin.mp3"
shutdown_mp3 = r"C:\Users\x\Documents\Shutdown-Sound.mp3"
icon_path = r"C:\Users\x\Documents\garmin-logo.ico"

pygame.mixer.init()

pressed_keys = set()
already_triggered_exit = False
already_triggered_alt_cedilla = False
voice_playing = False

def voice(sound_path):
    global voice_playing
    if voice_playing:
        return
    voice_playing = True
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    voice_playing = False

def on_press(key):
    global already_triggered_exit, already_triggered_alt_cedilla

    try:
        if key in {keyboard.Key.alt_l, keyboard.Key.alt_r}:
            pressed_keys.add("alt")
        elif key == keyboard.Key.shift:
            pressed_keys.add("shift")
        elif hasattr(key, 'char') and key.char:
            pressed_keys.add(key.char.lower())

        # Alt + ¸ detection (replace '¸' if needed)
        if {"alt", "¸"}.issubset(pressed_keys):
            if not already_triggered_alt_cedilla:
                threading.Thread(target=voice, args=(mp3,), daemon=True).start()
                already_triggered_alt_cedilla = True
        else:
            already_triggered_alt_cedilla = False

        # Shift + Alt + A detection
        if {"alt", "shift", "t"}.issubset(pressed_keys):
            if not already_triggered_exit:
                already_triggered_exit = True
                voice(shutdown_mp3)   # BLOCKING play shutdown sound
                tray_icon.stop()      # stop tray icon
                return False          # stop listener and exit app
        else:
            already_triggered_exit = False

    except Exception:
        pass

def on_release(key):
    try:
        if key in {keyboard.Key.alt_l, keyboard.Key.alt_r}:
            pressed_keys.discard("alt")
        elif key == keyboard.Key.shift:
            pressed_keys.discard("shift")
        elif hasattr(key, 'char') and key.char:
            pressed_keys.discard(key.char.lower())
    except Exception:
        pass

def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def create_image():
    return Image.open(icon_path)

def on_exit(icon, item):
    icon.stop()
    sys.exit()

tray_icon = Icon("OK Garmin")
tray_icon.icon = create_image()
tray_icon.menu = Menu(MenuItem("Exit", on_exit))

listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

tray_icon.run()