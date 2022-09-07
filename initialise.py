from common import *

def introduction():
    clr_scr()
    print("Instead of staying in the uncomfortable hotel room, you decided to head home\n\
immediately after the conference finished. You reckoned you could do it in less\n\
than three hours. You thought you would be home just after midnight\n\n\
But things got weird.")
    press_enter()
    print("You've driven in a thunderstorm before, and in fog, but both at the same time?\n\
Is that even possible?")
    print()
    print("Your GPS told you the road you were on would join the motorway in a mile, but\n\
instead you found yourself on a dirt track. And then the GPS reported No Signal.\n\n\
You drove for another hour in near zero visibility, eventually stopping at the\n\
side of a country road with a quarter of a tank of diesel remaining. You turned the\n\
engine off but decided to leave your lights on while you checked your bearings and\n\
looked for a safer place to park until the fog clears.")
    press_enter()
    print("But you dozed off. It's daytime, the sky is clear, and the car battery is flat.\n\
You get out of your car and find yourself outside...\n")
    press_enter()
    print()
    print()
    print()
    print("=================")
    print("The Lost Cottage.")
    print("=================")
    print()
    print("If you've never played a text adventure before please enter 'tutorial'.\n\
If you're fairly experienced you might want to enter 'tutorial' anyway as there\n\
may be a few unfamiliar features in this one. Whatever you decide, I hope you enjoy\n\
the game.")
    print()
    print("Paul Beardsley, author of Strange Doorways (available from Amazon) and Doctor Who:")
    print("The Suns of Caresh (writing as Paul Saint)")
    print()
    press_enter()

def ending():
    print("You attempt to start the engine...")
    press_enter()
    print("It starts!")
    press_enter()
    print("You let the engine run for a minute or two, gently pressing down on the accelerator\n\
to ensure it keeps turning over to charge up the battery.\n\
Then you go into gear, release the brake and drive off.")
    press_enter()
    print("You join a main road. There are other cars. They are old... but new. Registration\n\
numbers such as VCH931 with no letter suffix. Pre-1963.\n\
There is no question about it, you are in the past.")
    press_enter()
    print("How are you going to get home when you have no idea how you got here? You don't even\n\
know whereabouts in the country you are, let alone the year.\n\
Up ahead, you see a Shell petrol station. Maybe you can fill up on diesel,\n\
even though your credit card is not valid for this century!")
    press_enter()
    print("But as you indicate to pull in, you see another car pulling out.\n\
You can't believe your eyes, it's a modern car. A hybrid even!\n\
You cancel the signal and go after the other car. You flash your\n\
lights and sound your horn. The other driver notices, and turns\n\
in at the next lay-by. You pull in behind. The driver gets out,\n\
and so do you.")
    press_enter()
    print("To be continued...")

    

# Create locations

bathroom = Loc("The Bathroom")
bedroom = Loc("The Bedroom")
garden = Loc("The Garden")
hall = Loc("The Hall")
incar = Loc("Inside Your Car")
inpantry = Loc("Inside The Walk-In Pantry")
lounge = Loc("The Lounge")
landing = Loc("The Landing")
kitchen = Loc("The Kitchen")
road = Loc("The Road")

default = Loc("Nowhere")

bathroom.description = "There's a distinctly Victorian vibe about this room, with the bath mounted\n\
on claw feet and the toilet cistern placed high up the wall. The door leads south."

bedroom.description = "A room with a double bed. Exit east."

garden.description = "The path through the lawn is almost lost in the unmown grass.\n\
The front door of the cottage is to the north. South leads back to the road."
garden.setFirstEntryMsg("You open the creaking gate and enter the garden.\n\
The sound of birdsong goes quiet, and the birds take flight.")

hall.description = "The wallpaper is very old fashioned.\nThere is an even more old-fashioned electricity meter on the wall.\n\
The front door is to the south, and there are rooms west and north.\n\
A rustic staircase leads up."
hall.setFirstEntryMsg("You push the front door open and walk in.\n\
You feel a little uneasy entering someone else's house uninvited.")

incar.description = "Here in your car you feel safest of all.\n\
But with a flat battery, you're not going anywhere.\n\
There is a release lever under the steering wheel."

inpantry.description = "This is probably the saddest part of the house. Given the absence of a\n\
fridge, this is where all the food would have been stored. You don't know where the\n\
owners are now, but it's clear that they haven't prepared food for a long time."
inpantry.setFirstEntryMsg("You've picked the lock and gained access to the pantry.\n\
But was it worth it? It's a dismal place. You are briefly overwhelmed by the stale\n\
smell. Any food that was once kept in here is rotted or eaten by mice, with the rather\n\
odd exception of a Christmas pudding on one of the upper shelves.")

kitchen.description = "A country kitchen. The sink is very deep. Surprisingly, there is no fridge."
lounge.description = "As old fashioned as Grandma's lounge but without the warmth.\n\
The radio in the corner - or wireless as she would have called it - looks like it\n\
predates the Second World War."
landing.description = "Upstairs. Rooms to the west and north, and a rustic staircase leads down."
landing.setFirstEntryMsg("The thinly carpeted stairs creak under your feet.")

road.description = "An empty country road that stretches into the indefinite distance to the\n\
east and west. A garden gate to the north leads to a cottage."

# Create items

#Item(name, listed = False, portable = False)
battery = Item("Car Battery", True, True)
bed = Item("Large Bed")
#bonnet = Item("Car Bonnet", False)
#boot = Item("Car Boot", False)
charger = Item("Charger", True, True)
cradle = Item("Cradle for the car battery")
doorbell = Item("Doorbell", True)
key = Item("Key", False, True)
knife = Item("Knife", True, True)
lever = Item("Lever")
lock = Item("") # Empty string for name indicates not unique
lockfront = Item("Yale Lock")
lockpantry = Item("Simple Lock")
meter = Item("Electricity Meter")
mobile = Item("Mobile Phone", True, True)
plantpot = Item("Plantpot", True)
pudding = Item("Christmas Pudding", True, True)
radio = Item("Radio Set")
sixpence = Item("Sixpence", True, True)
outcar = Item("Car", True)
outpantry = Item("Pantry", True)
paperclip = Item("Paperclip", False, True)
socket = Item("")   # Empty string for name indicates not unique
socketnew = Item("Wall Socket")
socketold = Item("Wall Socket", True)
table = Item("Kitchen Table", True)
water = Item("Water")

# Transient items
connected = Item("Charger connected to battery", True)
plugged = Item("Charger plugged into wall socket", True)
charging = Item("Battery connected to charger plugged into wall socket", True)

#name, preposition, listed, portable, restricted, isopen
bonnet = Container("The open bonnet", "in", False, False, True)
boot = Container("The open boot", "in", False)
drawer = Container("The kitchen drawer, open", "in", False)
meter = Container("Electricity meter", "in", True, False, True, False)

# For items found in multiple places
lockdic = {garden: lockfront, kitchen: lockpantry, default: lockfront}
socketdic = {lounge: socketnew, kitchen: socketold, default: socketold}
notunique = {lock: lockdic, socket: socketdic}

blank = Item("Placeholder - no noun needed")
invalid = Item("Placeholder - wrong noun")

battery.describe("A standard car battery. Rather heavy to carry around.")
bed.describe("You might almost need a step ladder to get onto the mattress.")
charger.describe("A battery charger. It has all the necessary cables, and a square-pin plug.")
cradle.describe("This is where the battery goes. Preferably a charged battery.")
doorbell.describe("It's round, made of brass.")
key.describe("A Yale front-door key.")
knife.describe("A bread knife. Excellent for cutting bread, not great for combat.")
lockpantry.describe("Probably not that difficult to unlock, although it would be easier if you had the key.")
meter.describe("Positively anachronistic.\n\
There is a coin slot at the top, but it's too small for most coins.\n\
Not that you have any coins on you - you use your credit card for everything these days.")
mobile.describe("It's got a handy torch and a couple of games, but you cannot get a signal.")
paperclip.describe("A standard Gem Number 3.")
plantpot.describe("It's got a dead plant in it. Probably too heavy and bulky to carry.")
pudding.describe("This brings back fond memories of Christmas. It looks home made.")
radio.describe("An old valve set. It's heavy and dusty, and requires mains electricity.")
sixpence.describe("A very small silver coin from the days before decimilisation.")
outcar.describe("A Seat Leon. It has a bonnet and a boot. It takes diesel.")
outpantry.describe("A thick wooden door with a simple lock.")
socketnew.describe("A modern, square 3-pin wall socket.")
socketold.describe("One of those old round-pin sockets that builders stopped installing in the 1950s.")
table.describe("A fine oak table, associated with country houses. It has a single drawer.")

boot.contents.append(charger)
bonnet.contents.append(battery)
bonnet.contents.append(cradle)
bonnet.permitted.append(battery)
drawer.contents.append(knife)
meter.permitted.append(sixpence)

containerList = [bonnet, boot, drawer, meter]

bedroom.items.append(bed)
bathroom.items.append(water)
garden.items.append(doorbell)
garden.items.append(key)
garden.items.append(lockfront)
garden.items.append(plantpot)
hall.items.append(meter)
incar.items.append(lever)
inpantry.items.append(pudding)
kitchen.items.append(drawer)
kitchen.items.append(lockpantry)
kitchen.items.append(outpantry)
kitchen.items.append(socketold)
kitchen.items.append(table)
kitchen.items.append(water)
lounge.items.append(radio)
lounge.items.append(socketnew)
road.items.append(outcar)
road.items.append(bonnet)
road.items.append(boot)

specialMove = {\
road: {"message": "You walk along the road for a minute or two, seeing in broad daylight the open fields\n\
you must have driven past in the fog and darkness last night.\n\
But you see no sign of a filling station, a telephone box, or even houses other\n\
than the cottage where you parked.\n\
Far to the south you see the top of a church steeple, which suggests a village in that\n\
direction. But the road does not lead that way.\n\
You head back the way you came.",\
"arrival": road},\
bathroom: {"message": "You notice a loft hatch overhead. Stepping carefully on the side of the bath,\n\
you climb up through it.\n\
But for some reason that makes absolutely no sense, you find yourself back in the car.",\
"arrival": incar}\
}


lounge.e = hall
hall.w = lounge
hall.u = landing
hall.n = kitchen
inpantry.locked = "locked"
kitchen.s = hall
bathroom.u = specialMove
landing.d = hall
landing.w = bedroom
bedroom.e = landing
landing.n = bathroom
bathroom.s = landing
hall.s = garden
garden.n = hall
garden.s = road
garden.n.locked = "locked"
road.n = garden
road.e = specialMove
road.w = specialMove


you.where = road
you.carried.append(mobile)

# For testing:
#hall.locked = False
#you.where = hall
#you.carried.append(battery)
#you.carried.append(charger)
#you.carried.append(pudding)
#you.carried.append(knife)
#you.carried.append(sixpence)
#bonnet.isopen = True

# Victory conditions

class BatteryCharge:
    pluggedIn = False   # Charger in lounge plugged in
    connected = False   # Battery connected to charger
    powering = False    # Sixpence in meter
    ready = False       # Above three completed
    installed = False   # Battery, charged, in cradle in car
    
def updateCharge():
    if(BatteryCharge.pluggedIn and BatteryCharge.connected and BatteryCharge.powering):
        BatteryCharge.ready = True

def loungeCheck():
    if(BatteryCharge.ready == True):
        print()
        print("The indicator light is showing on the charger.")
        print("You wait, wondering if there will be enough power from a sixpence!")
        press_enter()
        print("After a while the indicator goes off.")
        print("You unplug the charger and disconnect the battery.")
        print("Time to say farewell to the cottage, lost in time.")
        battery.special = True
        battery.portable = True
        charger.portable = True
        battery.name = "Partly charged battery"
        charger.name = "Charger"

bonnet.describe("The car bonnet, closed.",\
"The car bonnet is in the release (or popped) position.",\
"The car bonnet, now open.")
boot.describe("The car boot is closed.", "The car boot is open.")
drawer.describe("A closed drawer.", "An open drawer.")

verbdic = {"ring": "ring", "call": "ring", "dial": "ring", "cut": "cut", "slic": "cut", "swit": "switch",\
"star": "start", "inst": "install", "plug": "plug", "unpl": "unplug", "conn": "connect",\
"drin": "drink", "eat": "eat", "slee": "sleep", "wash": "wash", "driv": "drive"}

verbdic.update(standardverbdic)

noundic = {"batt": battery, "bonn": bonnet, "hood": bonnet, "boot": boot, "trunk": boot,\
"char": charger, "crad": cradle, "door": doorbell, "bell": doorbell, "key": key, "knif": knife,\
"mobi": mobile, "phon": mobile, "torc": mobile, "plan": plantpot, "pot": plantpot,\
"pudd": pudding, "pud": pudding, "chri": pudding, "pape": paperclip, "clip": paperclip,\
"leve": lever,\
"sixp": sixpence, "coin": sixpence, "car": outcar, "auto": outcar, "engi": outcar, "pant": outpantry,\
"lard": outpantry, "tabl": table, "mete": meter, "slot": meter, "bed": bed,\
"draw": drawer, "lock": lock, "sock": socket, "radi": radio, "wire": radio,\
"wate": water, "blan": blank, "inva": invalid}

direction = ["nort", "n", "sout", "s", "east", "e", "west", "w", "up", "u", "down", "d"]
travel = ["go", "walk", "driv", "run", "swim"]
system = ["i", "inv", "inve", "l", "look", "help", "t", "tuto", "save", "rest"]
single = ["sleep", "wash", "drink", "drive"]
examine = ["exam", "x", "look", "l"]
prepositions = ["up", "in", "on", "into", "unde", "thro"]
adjectives = ["roun", "squa"]

    