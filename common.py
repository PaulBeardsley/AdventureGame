import platform
import os

class Loc:
    def __init__(self, name):
        self.name = name
        self.description = "TBC"
        self.extradescription = ""
        self.locked = False
        self.n = False
        self.e = False
        self.s = False
        self.w = False
        self.u = False
        self.d = False
        self.nlocked = False
        self.elocked = False
        self.slocked = False
        self.wlocked = False
        self.ulocked = False
        self.dlocked = False
        self.msgOnFirstEntry = False
        self.firstEntryMsg = False
        self.items = []

    def setFirstEntryMsg(self, msg):
        if(msg):
            self.msgOnFirstEntry = True
            self.firstEntryMsg = msg

    def displayFirstEntryMsg(self):
        if(self.firstEntryMsg and self.msgOnFirstEntry):
            self.msgOnFirstEntry = False
            print(self.firstEntryMsg)
            press_enter()

class Character:
    def __init__(self, where):
        self.where = where
        self.carried = []
        self.held = None
        self.moved = True
        self.lost = True


you = Character(Loc("Zero Room"))

class Item:
    def __init__(self, name, listed = False, portable = False):
        self.name = name
        self.descriptions = []
        self.examine = ""
        self.listed = listed    # Set to False if item mentioned in loc description
        self.portable = portable
        self.conditionalMsg = ""
        self.condition = True
        self.isopen = False
        self.special = 0    # e.g. battery is not charged
        
    def describe(self, *description):
        for d in description:
            self.descriptions.append(d)
        self.examine = description[0]

class Container:
    def __init__(self, name, preposition= "in", listed=False, portable=False, restricted=False, isopen=False):
        self.name = name
        self.listed = listed
        self.portable = portable
        self.isopen = isopen
        self.preposition = preposition
        self.descriptions = []
        self.examine = ""
        self.restricted = restricted
        self.permitted = []     # list of items allowed
        self.contents = []
        self.special = False
        
    def describe(self, *description):
        for d in description:
            self.descriptions.append(d)
        self.examine = description[0]
        

def clr_scr():
    if(platform.system().lower()=="windows"):
        cmdtorun='cls'
    else:
        cmdtorun='clear'
    os.system(cmdtorun)

def press_enter():
    print()
    input("Press Enter to continue...")
    clr_scr()

standardverbdic = {"x": "examine", "exam": "examine",\
"get": "take", "take": "take", "drop": "drop", "pick": "pick",\
"unlo": "unlock", "open": "open", "clos": "close", "put": "put",\
"lift": "move", "move": "move", "push": "move", "pull": "move",\
"hold": "select", "sele": "select", "inse": "insert",
"ente": "enter", "leav": "leave", "exit": "leave"}

def tutorial():
    print("The Lost Cottage is a text adventure game. You are presented with a description of\n\
a location and visible objects. You interact with the game by entering text commands\n\
such as GET BRUSH (if there is a brush present), EXAMINE BRUSH and SWEEP PATH. These\n\
actions may or may not cause things to change and the story to advance.\n\n\
Note that the parser is not case sensitive, and only the first 4 letters of each word\n\
are read. So PHOTOCOPY CERTIFICATE is the same as phot cert.\n\n\
Examine can be shortened to X, and LOOK, to refresh your surroundings, to L.\n\n\
To move about, type GO NORTH, GO EAST, GO UP etc., or simply N, E, U.\n\
Location descriptions will usually give you an idea of which ways you can go.\n\n\
You can enter or leave some locations, e.g. ENTER CAPSULE, LEAVE CUBICLE.\n\n\
To check what you are carrying, enter INVENTORY or just I.\n\
This will also tell you which item (if any) is currently selected.\n\n\
Use SELECT [OBJECT] if you want to be clear which item in your inventory you want to use.\n\
For instance, if you are carrying a sword and a knife, you might want to enter SELECT KNIFE\n\
before entering CUT APPLE to make it clear that you are using the knife, not the sword.\n\
If the SELECTed item is multifunctional, its use will probably be determined by context.\n\
As well as the VERB-NOUN combination you will use throughout the game, you might\n\
occasionally need to use prepositions, such as ON, IN, THROUGH etc. For instance,\n\
LOOK THROUGH WINDOW.\n\n\
You can sometimes combine the SELECT command with prepositions. For example,\n\
SELECT TELESCOPE followed by LOOK THROUGH WINDOW means you are using the telescope to look\n\
through the window, or SELECT BUTTER followed by PUT IN BOWL means you are putting the butter\n\
in the bowl.")