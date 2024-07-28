from sshkeyboard import listen_keyboard

def press(key):
    print(f"{key} pressed")

listen_keyboard(on_press=press)
