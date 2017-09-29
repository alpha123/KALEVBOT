import importlib.machinery
import os
import sys

sp = os.path.dirname(os.path.realpath(sys.argv[0]))

loader2 = importlib.machinery.SourceFileLoader('maincore', sp + '/maincore.py')
core = loader2.load_module('maincore')

def run(message, prefix, alias):

    emotes = ''.join([str(x) for x in core.cl.get_all_emojis()])
    core.send(message.channel, emotes)

def help_use():
    return "Get all the emotes the bot can use"

def help_param():
    return None

def help_cmd(prefix):
    return prefix + "emote"

def help_perms():
    return 0

def help_list():
    return "Get all the emotes the bot can use"

def alias():
    return ['emote']