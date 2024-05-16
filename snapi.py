import time
time.sleep(15)


import keyboard
import requests
import json
import numpy as np


uri = "https://snapi-web.onrender.com/"
ag =  uri + "api/activeGames"
ug = uri + "api/updateGameExternal"


p1add = np.array([0,0,0,0])
p2add = np.array([0,0,0,0])
p3add = np.array([0,0,0,0])
p4add = np.array([0,0,0,0])


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
    
    print("tossing player 1")
    p1add[0] += 1

    player1 = True
    player2 = False
    player3 = False
    player4 = False
    
    update_game()

def wfunc():

    print("catch player 1")
    p1add[2] += 1

    update_game()
 

def efunc():
    global player3
    global player4
    
    print("drop player 1")
    p1add[3] += 1
    if player3:
        #player3 last tossed
        p3add[1] += 1
    elif player4:
        #player4 last tossed
        p4add[1] += 1
    else:
        pass

    update_game()


#player2 team 1
def zfunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossing player 2")
    p2add[0] += 1

    player1 = False
    player2 = True
    player3 = False
    player4 = False

    update_game()


def xfunc():

    print("catch player 2")
    p2add[2] += 1

    update_game()
 

def cfunc():
    global player3
    global player4
    
    print("drop player 2")
    p2add[3] += 1
    if player3:
        #player3 last tossed
        p3add[1] += 1
    elif player4:
        #player4 last tossed
        p4add[1] += 1
    else:
        pass

    update_game()


#player3 team 2
def ifunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossing player 3")
    p3add[0] += 1

    player1 = False
    player2 = False
    player3 = True
    player4 = False

    update_game()


def ofunc():

    print("catch player 3")
    p3add[2] += 1

    update_game()

def pfunc():
    global player1
    global player2
    
    print("drop player 3")
    p3add[3] += 1
    if player1:
        #player1 last tossed
        p1add[1] += 1
    elif player2:
        #player2 last tossed
        p2add[1] += 1
    else:
        pass

    update_game()


#player4 team 2
def bfunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossing player 4")
    p4add[0] += 1
    player1 = False
    player2 = False
    player3 = False
    player4 = True

    update_game()


def nfunc():

    print("catch player 4")
    p4add[2] += 1

    update_game()
 

def mfunc():
    global player1
    global player2
    
    print("drop player 4")
    p4add[3] += 1
    if player1:
        #player1 last tossed
        p1add[1] += 1
    elif player2:
        #player2 last tossed
        p2add[1] += 1
    else:
        pass

    update_game()


def qwefunc():
    print("POINT SCORED!")
    global player1
    global player2
    global player3
    global player4

    if player1:
        #player1point
        p1add[1] += 1
    elif player2:
        #player2point
        p2add[1] += 1
    elif player3:
        #player3point
        p3add[1] += 1
    elif player4:
        #player4point
        p4add[1] += 1
    else:
        pass

    update_game()

# keyboard.add_hotkey('q+w+e', qwefunc)
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

def update_game():
    global p1add
    global p2add
    global p3add
    global p4add
    
    payload = {}
    headers = {}

    response = requests.request("GET", ag, headers=headers, data=payload)

    data = response.json()
    game = data[0]
    p1stats = np.array(game["p1Stats"])
    p2stats = np.array(game["p2Stats"])
    p3stats = np.array(game["p3Stats"])
    p4stats = np.array(game["p4Stats"])

    updatedp1 = p1stats + p1add
    updatedp2 = p2stats + p2add
    updatedp3 = p3stats + p3add
    updatedp4 = p4stats + p4add

    p1add = np.array([0,0,0,0])
    p2add = np.array([0,0,0,0])
    p3add = np.array([0,0,0,0])
    p4add = np.array([0,0,0,0])

    payload = {'p1Stats': updatedp1.tolist(),
    'p2Stats': updatedp2.tolist(),
    'p3Stats': updatedp3.tolist(),
    'p4Stats': updatedp4.tolist(),}

    response = requests.post(ug, json=payload)
    

keyboard.wait("esc")

