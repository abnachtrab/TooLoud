import numpy as np
import sounddevice as sd
from pynput.keyboard import Key, Controller

keyboard = Controller()
tooloud = False
limit = 300  # 0-150 is normal conversation (I think)


#                     Don't remove these you'll get errors
def get_sound(indata, outdata, frames, time, status):
    global tooloud
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > limit:
        tooloud = True


while True:
    with sd.Stream(callback=get_sound):
        if tooloud:
            keyboard.press(Key.alt)
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
            keyboard.release(Key.alt)
            tooloud = False
        sd.sleep(1000)
