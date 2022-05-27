import time as ti
from pynput.keyboard import Key, Controller

keyboard = Controller()

ti.sleep(2)
for x in range (1689):
    for y in range (5):

        keyboard.press(Key.right)
        keyboard.release(Key.right)

    keyboard.press(",")
    keyboard.release(",")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


# from pynput import keyboard

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()