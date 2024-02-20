import keyboard
import time

team1 = False


def qfunc():
    global team1
    global team2
    
    print("tossingq")
    team1 = True
    print(team1)

def afunc():
    global team1
    global team2
    
    print("tossinga")
    team1 = False
    print(team1)
    
    

# def wfunc():
#     print("w press")

# def efunc():
#     print("e press")

# def qwefunc():
#     print("point Q!")

# def asdfunc():
#     print("point A!")


keyboard.add_hotkey('q', qfunc)
keyboard.add_hotkey('a', afunc)
# keyboard.add_hotkey('e', efunc)

    



# main()
keyboard.wait()
