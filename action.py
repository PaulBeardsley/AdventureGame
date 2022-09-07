from common import *
from initialise import *
from parse import *

def action(verbtext, nountext, extratext):
    # check for direction
    box = None  # Convenience variable for storing container where noun is located
    if(verbtext == "go"):
        if(nountext in ["n", "e", "s", "w", "u", "d"]):
            destination = { "n": you.where.n, "e": you.where.e, "s": you.where.s,\
            "w": you.where.w, "u": you.where.u, "d": you.where.d}
            if(destination[nountext] == specialMove):
                print(specialMove[you.where]["message"])
                press_enter()
                targetRoom = specialMove[you.where]["arrival"]
            else:
                targetRoom = destination[nountext]
            if(targetRoom):
                if(targetRoom.locked):
                    print("That way is", targetRoom.locked)
                else:
                    you.where = targetRoom
                    you.moved = True
                    #you.where.displayFirstEntryMsg()
            else:
                print("You cannot move in that direction.")
        return
    # check for system verbs
    elif(verbtext == "sys"):
        if(nountext in system):
            if(nountext == "l"):
                you.moved = True
            elif(nountext == "i"):
                if(len(you.carried) == 0):
                    print("You are not carrying anything.")
                else:
                    print("You are carrying:")
                    for item in you.carried:
                        print("\t", item.name, end = " ")
                        if(item == you.held):
                            print("(selected)")
                        else:
                            print("")
            elif(nountext in ["t", "tuto"]):
                tutorial()
            elif(nountext == "h"):
                print("No specific help here; for general help try TUTORIAL.")
            else:
                print("Not implemented yet.")
        else:
            print("Unexpected.", nountext)
        return

    else:
        pass
    
    if(verbtext in verbdic):
        verb = verbdic[verbtext]
    else:
        print("The verb", verbtext, "is not recognised.")
        return
    noun_is_found = False
    if(nountext in noundic):
        noun = noundic[nountext]
    else:
        if(verb in single):
            noun = blank
        else:
            noun = invalid

# Commands where the noun is somewhere other than the loc

    if(verb == "drive" or verb == "start"):
        if(you.where == incar):
            if(BatteryCharge.installed == True and bonnet.isopen == False and boot.isopen == False):
                you.lost = False
                ending()
            else:
                print("You are not yet ready to drive away.")
        else:
            print("I'm not sure what you want to drive.")
        return
    if(verbtext == "ring" and noun != doorbell):
        print("You cannot get a signal on your phone.")
        return
# After this block, there is no need to check if a noun is in the loc or inv
# If item is in a container, the container is passed on to be handled by examine and take
    if(noun.name == ""):
        if(noun in notunique):
            if(you.where in notunique[noun]):
                noun = notunique[noun][you.where]
            else:
                noun = notunique[noun][default]
        else:
            noun = invalid

    if((noun in you.where.items)\
    or (noun in you.carried)\
    or (noun == blank)\
    or verb in ["enter", "leave"]):
        noun_is_found = True
    else:   # Looking in the containers
        for c in containerList:
            if(noun in c.contents):
                box = c
                if(box in you.where.items and box.isopen == True):
                    noun_is_found = True
                break

    if(noun_is_found == True):
        pass
    else:
        print(noun.name, "is not here.")
        return
# From here, verb and noun expected with possible adj/prep

    if(verb == "put"):  # For use with containers
        if(you.held is None):
            print("You need to select an item.")
        else:
            if(noun == cradle): # Special case 1/2 - cradle is synonymous with bonnet
                noun = bonnet
            if(noun in containerList):
                if(extratext == noun.preposition):
                    if(noun.restricted == False or you.held in noun.permitted):
                        you.carried.remove(you.held)
                        noun.contents.append(you.held)
                        if(noun == bonnet and you.held == battery):
                            cradle.listed = False
                        # Feedback needs other prepositions
                        if(noun == bonnet): # Special case 2/2
                            noun = cradle
                            if(BatteryCharge.ready == True):
                                BatteryCharge.installed = True
                                incar.description = "You are behind the steering wheel, with your keys in the ignition."
                        print(f"You place {you.held.name} in the {noun.name}.")
                        you.held = None
                        # Extra action for meter
                        if(noun == meter):
                            meter.contents.remove(sixpence)
                            BatteryCharge.powering = True
                            updateCharge()
                    else:
                        if(noun == bonnet):
                            noun = cradle
                        print(f"{you.held.name} doesn't go in {noun.name}")
                else:
                    print("Try a different preposition (in, on, through, under etc.).")
            else:
                print(f"I'm not sure where you want to put {you.held.name}.")
        return


    if(verb == "examine"):
        if(noun == bed):    # Special case of look
            if(extratext == "un"):
                print("It is dark under the bed.")
                if(you.held == mobile):
                    if(paperclip.listed == True):
                        print("You don't find anything else except dustbunnies.")
                    else:
                        print("Glinting in the light of your phone torch, you find a paperclip!")
                        paperclip.listed = True
                        bedroom.items.append(paperclip)
                return
    
        print(noun.examine)
        return
    if(verb == "take"):
        if(box is not None):
            place = box.contents
            if(noun == battery):
                cradle.listed = True
        else:
            place = you.where.items
    
    
        if(noun in place):
            if(noun.portable):
                you.carried.append(noun)
                you.held = noun
                place.remove(noun)
                print("Now carrying", noun.name)
            else:
                print(noun.name, "cannot be carried.")
        else:
            print("Already carrying", noun.name)
        return
    if(verb == "select"):
        if(noun in you.carried):
            you.held = noun
        else:
            print(noun.name, "not in inventory.")
        return

    if(verb == "drop"):
        if(noun in you.carried):
            you.carried.remove(noun)
            if(you.held == noun):
                you.held = None
            you.where.items.append(noun)
            print(noun.name, "dropped.")
        else:
            print("Not carrying", noun.name)
        return
    if(verb == "enter"):
        
        if((noun == outpantry) and (you.where == kitchen)):
            if(inpantry.locked == "locked"):
                print("You're going to have to unlock it first.")
            else:
                you.where = inpantry
                you.moved = True
        elif((noun == outcar) and (you.where == road)):
             you.where = incar
             you.moved = True
        else:
            you.moved = False
            print("You can't go in there from here.")
        return
    if(verb == "leave"):
        you.moved = True
        if(you.where == inpantry):
            you.where = kitchen
        elif(you.where == incar):
            you.where = road
        else:
            you.moved = False
            print("You can't exit", noundic[nountext].name, "from", you.where.name)
        return



    if(verb == "move"):
        if(noun == plantpot):
            if(key.listed == True):
                print("You don't discover anything else under the pot.")
            else:
                print("You notice a front door key under the pot.")
                key.listed = True
        elif(noun == lever):
            if(bonnet.special == 0):
                bonnet.special = 1
                print("You hear a 'thunk' as the bonnet is released.")
                bonnet.examine = bonnet.descriptions[1]
            else:
                print("The bonnet is already in its released position.")
        else:
            print("That cannot be usefully moved.")
        return
    if(verb == "pick"):
        if(you.where == garden or kitchen):
            if(you.held == paperclip):
                #print("You attempt to pick the lock with the paperclip.")
                if(you.where == garden):
                    print("Frankly I don't see the point.")
                else:
                    if(inpantry.locked == False):
                        print("You've already picked that lock.")
                    else:
                        print("You unbend the paperclip, insert it in the lock and move it about for a bit.\n\
After persisting for a while, you hear a 'ping'.")
                        inpantry.locked = False
            else:
                print("What were you thinking of using?")
        else:
            print("I don't see a lock to pick here.")
        return
    if(verb == "unlock"):
        if(you.where == garden):
            if(key in you.carried):
                print("You unlock the front door.")
                garden.n.locked = False
            else:
                print("You don't have the key for that lock.")
        elif(you.where == kitchen):
            print("You don't have the key for that lock.")
        else:
            print("There is no lock here.")
        return
    if(verb == "wash"):
        if(water in you.where.items):
            print("You freshen up a bit.")
        else:
            print("There is no water here.")
        return
    if(verb == "sleep"):
        #print(noun.name)
        if(bed in you.where.items):
            print("It's tempting, but what if the owners come home?\n\
Besides, the situation is too dreamlike as it is!")
        else:
            print("Not here, and not now.")
        return
    if(verb == "drink"):
        if(noun == water or noun == blank):
            if(water in you.where.items):
                print("You take a long, refreshing drink from the tap.")
                if(you.where == bathroom):
                    print("Given the age of the plumbing, kitchen water might have been a wiser choice.")
            else:
                print("There is no water here.")
        else:
            print(noun.name, "is not something you can drink in this game!")
        return
    if(verb == "eat"):
        if(noun == pudding):
            print("You consider eating the Christmas pudding.\n\
These things are supposed to get better with age. But, given the state of the pantry\n\
in which you found it, you reconsider. You're not going to eat it.")
        else:
            print("Probably best not to eat that.")
        return
    if(verb == "cut"):
        if(noun == pudding):
            if(knife in you.carried):
                print("You cut the Christmas pudding into several pieces. You find a sixpence!")
                you.where.items.append(sixpence)
                if(pudding in you.where.items):
                    you.where.items.remove(pudding)
                elif(pudding in you.carried):
                    you.carried.remove(pudding)
                    if(you.held == pudding):
                        you.held = None
                else:
                    if(pudding in box.contents):
                        box.contents.remove(pudding)
            else:
                print("With what do you want to cut it?")
        else:
            print("I don't think that needs cutting.")
        return
            
    if(verb == "ring"):
        if(noun == doorbell):
            print("You press the bell push, but hear nothing.")
        else:
            if(phone in you.where.items or you.carried):
                print("You cannot get a signal on your phone.")
        return

    if(verb == "open"):
        if(noun == drawer):
            if(drawer.isopen == True):
                print("The drawer is already open.")
            else:
                drawer.examine = drawer.descriptions[1]
                #drawer.listed = True
                drawer.isopen = True
                print("The drawer slides open.")
        elif(noun == boot):
            if(boot.isopen == True):
                print("The boot is already open.")
            else:
                #boot.listed = True
                boot.isopen = True
                boot.examine = boot.descriptions[1]
                print("You open the boot.")
        elif(noun == bonnet):
            if(bonnet.isopen == True):
                print("The bonnet is already open.")
            elif(bonnet.special == 0):
                print("You need to release it first.")
            else:
                #bonnet.listed = True
                bonnet.isopen = True
                bonnet.examine = bonnet.descriptions[2]
                print("You open the bonnet.")
        elif(noun == doorbell):
            if garden.n.locked == "locked":
                print("The front door needs unlocking.")
            else:
                print("It's unlocked, just go through.")
        else:
            print("That cannot be opened.")
        return
    if(verb == "close"):
        if(noun == drawer):
            if(drawer.isopen == False):
                print("It won't close any further.")
            else:
                drawer.listed = False
                drawer.isopen = False
                drawer.examine = drawer.descriptions[0]
                print("The drawer slides shut.")
        elif(noun == boot):
            if(boot.isopen == False):
                print("The boot is already closed.")
            else:
                boot.listed = False
                boot.isopen = False
                print("You slam the boot shut.")
                boot.examine = boot.descriptions[0]
        elif(noun == bonnet):
            if(bonnet.special > 0):
                print("You close the bonnet.")
                bonnet.examine = bonnet.descriptions[0]
                bonnet.listed = False
                bonnet.isopen = False
                bonnet.special = 0
            else:
                print("It's already closed.")
        else:
            print("That cannot be closed.")
        return
    if(verb == "switch"):
        if(noun == radio):
            if(radio.special > 0):
                print("It's not plugged in.")
            else:
                if(meter.special > 0):
                    print("Don't waste the electricity you're getting for sixpence!")
                else:
                    print("There is no power on.")
        else:
            print("I don't think that's switchonable.")
        return
    if(verb == "unplug"):
        if(noun == radio):
            print("You unplug the radio, freeing up the wall socket.\n\
This one must have been installed more recently than the one in the kitchen.\n\
It's a square pin wall socket!")
            radio.special = 1   # Means the radio is unplugged
            socketnew.listed = True
        elif(noun == charger):
            if(BatteryCharge.ready == True):
                print("Charger unplugged.")
            else:
                print("I can't think of a better thing to keep plugged in than the charger.")
        else:
            print("I don't think you can unplug that.")
        return
        
    # The next block is grouped as any action can start the charging.
    if(verb == "plug"):
        if(you.where == kitchen):
            print("Nothing you have fits in that old wall socket!")
        elif(you.where == lounge):
            if(radio.special == 0): # Radio still plugged in
                print("I see no available socket.") 
            else:
                if(noun == radio):
                    print("There's no point in plugging that back in.")
                elif(noun == charger):
                    print("Plug it in, plug it in!")
                    socketnew.special = 1
                    BatteryCharge.pluggedIn = True
                    updateCharge()
                    charger.portable = False
                    charger.name = "Charger, plugged into wall."
                    if(charger in you.carried):
                        you.carried.remove(charger)
                        you.where.items.append(charger)
                        if(you.held == charger):
                            you.held = None
                else:
                    print("You don't have any other pluginable items.")
                    
        else:
            print("No sockets here I'm afraid.")
        return
            
    if(verb == "connect"):
        if(noun == charger or battery):
            if(BatteryCharge.pluggedIn == False):
                print("No point in connecting the battery to the charger until the charger is plugged in.")
            elif(BatteryCharge.ready):
                print("No more coins, no more power!")
            else:
                if(you.where != lounge):
                    print("Both items need to be here.")
                else:
                    if(battery in you.carried):
                        you.carried.remove(battery)
                        you.where.items.append(battery)
                        if(you.held == battery):
                            you.held = None
                    if(battery in you.where.items):
                        print("You connect the battery to the charger.")
                        BatteryCharge.connected = True
                        updateCharge()
                        battery.portable = False
                        battery.name = "Battery, connected to charger."
                    else:
                        print("The battery is not here.")
        return
    

    print("I cannot do that.")
    return