from parse import *
from action import *
from initialise import *

you.moved = True
#print("loc is", loc.name)
you.held = None



introduction()

while(you.lost):
    if(you.moved):
        clr_scr()
        you.where.displayFirstEntryMsg()
        print(you.where.name)
        print()
        print(you.where.description)
        if(you.where.extradescription != ""):
            print()
            print(you.where.extradescription)
        if(you.where == lounge):    # Special location
            loungeCheck()
            #print(f"{BatteryCharge.pluggedIn} {BatteryCharge.connected} {BatteryCharge.powering} {BatteryCharge.ready}")
        if(len(you.where.items)):
            open_containers = []
            listed_items_present = False
            for c in you.where.items:
                if(c.listed):
                    listed_items_present = True
                if(c in containerList):
                    if(c.isopen == True):
                        open_containers.append(c)
            if(listed_items_present):
                print("\nAlso visible:")
                for n in you.where.items:
                    if(n.listed):
                        print("\t",n.name)
            if(len(open_containers) > 0):
                for d in open_containers:
                    print("\t",d.name)
                    for e in d.contents:
                        if(e.listed == True):
                            print(f"\t\t{e.name}")
            print()
        you.moved = False
    verb = ""
    noun = ""
    extra = ""
    command = input("\n> ").lower()
    command = command.strip()
    if(command == "quit"):
        break
    if(command == ""):
        continue
    #print("command:", command)
    instructions = parse(command)
    #print("instructions:", instructions)
    if(instructions[0] != ""):
        verb = instructions[0]
    if(instructions[1] != ""):
        noun = instructions[1]
    if(instructions[2] != ""):
        extra = instructions[2]
    action(verb, noun, extra)

