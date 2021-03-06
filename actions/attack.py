import importlib.machinery
import os
import sys

sp = os.path.dirname(os.path.realpath(sys.argv[0]))

loader = importlib.machinery.SourceFileLoader('basic', sp + '/basic.py')
rpg = loader.load_module('basic')
loader2 = importlib.machinery.SourceFileLoader('maincore', sp + '/maincore.py')
core = loader2.load_module('maincore')

def run(message, rpgPrefix, alias):
    targetID = ""
    combine = None
    if len(message.mentions) == 1:
        mentiont = message.mentions[0]
        target = mentiont
        targetID = mentiont.id
    else:
        cmdlen = len(rpgPrefix + alias)
        opstring = message.content[cmdlen:].strip()
        gotuser = core.userget(opstring)
        if gotuser is None:
            combine = "Something failed, user not found"
        else:
            target = gotuser
            targetID = gotuser.id
    if combine != None:
        return "m", [message.channel, combine]
    else:
        playerlist = rpg.get_playerlist()
        selfEntity = playerlist[message.author.id]
        targetEntity = playerlist[targetID]
        status, returnMSG = selfEntity.attack(targetEntity)
        if status:
            outcome = ", here is what happened.\n"
        else:
            outcome = ", something failed.\n"
        return "m", [message.channel, message.author.mention + outcome + "```diff\n" + str(returnMSG) + "\n```"]

def help_use():
    return "Attack a specified player, removing some of their HP. Damage dealt varies on your Attack and their Defense. Attacks have a chance to Miss or Crit.\nMisses are reduced by having higher Speed, crits are incereased by having more Luck\nAfter attacking someone, you cannot attack them again until they attack you back."

def help_param():
    return "<PLAYER*>: The username, ID or mention of the user you want to attack"

def help_cmd(prefix):
    return prefix + "attack <PLAYER*>"

def help_perms():
    return 0

def help_list():
    return "Attack a player"

def alias():
    return ['attack', 'strike', 'a']
