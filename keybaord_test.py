import keyboard

player1 = False
player2 = False
player3 = False
player4 = False

#player1 team 1
def qfunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossingq")
    player1 = True
    player2 = False
    player3 = False
    player4 = False


def wfunc():

    print("catchw")
 

def efunc():
    global player3
    global player4
    
    print("drope")
    if player3:
        #player3 last tossed
        pass
    elif player4:
        #player4 last tossed
        pass
    else:
        pass


#player2 team 1
def zfunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossingz")
    player1 = False
    player2 = True
    player3 = False
    player4 = False


def xfunc():

    print("catchx")
 

def cfunc():
    global player3
    global player4
    
    print("dropc")
    if player3:
        #player3 last tossed
        pass
    elif player4:
        #player4 last tossed
        pass
    else:
        pass


#player3 team 2
def ifunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossingi")
    player1 = False
    player2 = False
    player3 = True
    player4 = False


def ofunc():

    print("catcho")
 

def pfunc():
    global player1
    global player2
    
    print("dropp")
    if player1:
        #player1 last tossed
        pass
    elif player2:
        #player2 last tossed
        pass
    else:
        pass


#player4 team 2
def bfunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossingb")
    player1 = False
    player2 = False
    player3 = False
    player4 = True


def nfunc():

    print("catchn")
 

def mfunc():
    global player1
    global player2
    
    print("dropm")
    if player1:
        #player1 last tossed
        pass
    elif player2:
        #player2 last tossed
        pass
    else:
        pass


def qwefunc():
    global player1
    global player2
    global player3
    global player4

    if player1:
        #player1point
        pass
    elif player2:
        #player2point
        pass
    elif player3:
        #player3point
        pass
    elif player4:
        #player4point
        pass
    else:
        pass


#player1 team 1
keyboard.add_hotkey('q', qfunc)
keyboard.add_hotkey('w', wfunc)
keyboard.add_hotkey('e', efunc)
#player2 team 1
keyboard.add_hotkey('z', zfunc)
keyboard.add_hotkey('x', xfunc)
keyboard.add_hotkey('c', cfunc)


#player3 team 2
keyboard.add_hotkey('i', ifunc)
keyboard.add_hotkey('o', ofunc)
keyboard.add_hotkey('p', pfunc)
#player4 team 2
keyboard.add_hotkey('b', bfunc)
keyboard.add_hotkey('n', nfunc)
keyboard.add_hotkey('m', mfunc)



keyboard.wait()
