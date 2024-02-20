import keyboard

def qfunc():
    print("q")

def wfunc():
    print("w press")

def efunc():
    print("e press")
keyboard.add_hotkey('q', qfunc)
keyboard.add_hotkey('w', wfunc)
keyboard.add_hotkey('e', efunc)

keyboard.wait("esc")
print("end")