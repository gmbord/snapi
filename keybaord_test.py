import keyboard

class Player:
    def __init__(self):
        self.tosses = 0
        self.points = 0
        self.catches = 0
        self.drops = 0

    def get_stats(self):
        return (self.tosses, self.points, self.catches, self.drops)
    
    def add_one(self, var):
        setattr(self, var, getattr(self, var) + 1)

one = Player()
two = Player()
three = Player()
four = Player()


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
    one.add_one("tosses")

    player1 = True
    player2 = False
    player3 = False
    player4 = False


def wfunc():

    print("catch player 1")
    one.add_one("catches")
 

def efunc():
    global player3
    global player4
    
    print("drop player 1")
    one.add_one("drops")
    if player3:
        #player3 last tossed
        three.add_one("points")
    elif player4:
        #player4 last tossed
        four.add_one("points")
    else:
        pass


#player2 team 1
def zfunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossing player 2")
    two.add_one("tosses")

    player1 = False
    player2 = True
    player3 = False
    player4 = False


def xfunc():

    print("catch player 2")
    two.add_one("catches")
 

def cfunc():
    global player3
    global player4
    
    print("drop player 2")
    two.add_one("drops")
    if player3:
        #player3 last tossed
        three.add_one("points")
    elif player4:
        #player4 last tossed
        four.add_one("points")
    else:
        pass


#player3 team 2
def ifunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossing player 3")
    three.add_one("tosses")

    player1 = False
    player2 = False
    player3 = True
    player4 = False


def ofunc():

    print("catch player 3")
    three.add_one("catches")

def pfunc():
    global player1
    global player2
    
    print("drop player 3")
    three.add_one("drops")
    if player1:
        #player1 last tossed
        one.add_one("points")
    elif player2:
        #player2 last tossed
        two.add_one("points")
    else:
        pass


#player4 team 2
def bfunc():
    global player1
    global player2
    global player3
    global player4
    
    print("tossing player 4")
    four.add_one("tosses")
    player1 = False
    player2 = False
    player3 = False
    player4 = True


def nfunc():

    print("catch player 4")
    four.add_one("catches")
 

def mfunc():
    global player1
    global player2
    
    print("drop player 4")
    four.add_one("drops")
    if player1:
        #player1 last tossed
        one.add_one("points")
    elif player2:
        #player2 last tossed
        two.add_one("points")
    else:
        pass


def qwefunc():
    global player1
    global player2
    global player3
    global player4

    if player1:
        #player1point
        one.add_one("points")
    elif player2:
        #player2point
        two.add_one("points")
    elif player3:
        #player3point
        three.add_one("points")
    elif player4:
        #player4point
        four.add_one("points")
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



keyboard.wait("esc")
print(one.get_stats(), "player 1")
print(two.get_stats(), "player 2")
print(three.get_stats(), "player 3")
print(four.get_stats(), "player 4")
