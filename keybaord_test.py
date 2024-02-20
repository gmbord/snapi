import keyboard

def qfunc():
    
    keyboard.add_hotkey('q+w+e', qwefunc)
    print("q")
    keyboard.wait('a', afunc)

def afunc():
    
    keyboard.add_hotkey('a+s+d', asdfunc)
    print("a")
    keyboard.wait('q', qfunc)
    

def wfunc():
    print("w press")

def efunc():
    print("e press")

def qwefunc():
    print("point Q!")

def asdfunc():
    print("point A!")


keyboard.add_hotkey('q', qfunc)
keyboard.add_hotkey('w', wfunc)
keyboard.add_hotkey('e', efunc)


keyboard.wait("esc")
print("end")