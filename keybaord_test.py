import keyboard

def qfunc():
    print("q")

keyboard.add_hotkey('q', qfunc)

keyboard.wait("esc")
print("end")