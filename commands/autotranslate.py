import importlib.machinery
import os
import sys
from googletrans import Translator
import iso639
import pycountry

sp = os.path.dirname(os.path.realpath(sys.argv[0]))

loader2 = importlib.machinery.SourceFileLoader('maincore', sp + '/maincore.py')
core = loader2.load_module('maincore')

def run(message, prefix, alias):
    cmdlen = len(prefix + alias)
    opstring = message.content[cmdlen:].strip()
    translator = Translator()
    done = translator.translate(opstring)
    try:
        fromlang = pycountry.languages.get(alpha_2=done.src).name
    except:
        fromlang = done.src
    try:
        tolang = pycountry.languages.get(alpha_2=done.dest).name
    except:
        tolang = done.dest
    detect = translator.detect(opstring)
    core.send(message.channel, ":: translating {} -> {} ({}% certainty)::\n{}".format(fromlang, tolang, round(detect.confidence * 100), done.text), "```asciidoc\n", "\n```")

def help_use():
    return "Translate something from an automatically-detect language into English, using Google Translate"

def help_param():
    return "[WORDS**] The word(s) or sentence(s) to translate into English"

def help_cmd(prefix):
    return prefix + "autotranslate [WORDS**]"

def help_perms():
    return 0

def help_list():
    return "Translate something from a language into English"

def alias():
    return ['autotranslate', 'atr']