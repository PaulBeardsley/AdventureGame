from initialise import *

def parse(command):
    verb = ""
    noun = ""
    middle = ""  # For prepositions and adjectives between the verb and the noun

    comlist = command.split(sep=" ")    # break down command string into separate words

    if(len(comlist) > 0):               # not a blank command
        verb = comlist[0][0:4]
        if(len(comlist) == 1):          # single word command
            if(verb in direction):      # word is e.g. e, east, u, up
                noun = verb[0]
                verb = "go"             # "e" or "go east" returns "go e"
            elif(verb in system):
                noun = verb[0]
                verb = "sys"            # "restore" returns "sys r"
            else:
                pass
        else:
            if(len(comlist) > 1):       # command is 2 or more words
                noun = comlist[-1][0:4]
                if((verb in travel) and (noun in direction)):
                    verb = "go"
                    noun = noun[0]
                elif(verb in examine):
                    verb = "x"
                else:
                    pass


            if(len(comlist) > 2):
                for word in comlist[1:-1]:
                    if(word[0:4] in adjectives):
                        middle = word[0:4]
                    elif(word[0:4] in prepositions):
                        middle = word[0:2]  # remove dist'n between in&into, on&onto etc
                        break
                if(verb == "pick" and middle == "up"):  # Special case to deal with "pick up"
                    verb = "take"
                    middle = ""
    return([verb, noun, middle])

