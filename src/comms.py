import sys
from src.tsl import xrint, Danger, Warning, Information, Ok
from rich import pretty
from src.auth import Worker
from src.cmt import _pcmt, _gpcmt
import src.ocec as o


def load():
    pretty.install()
    from rich.console import Console

    p = Console()
    try:
        import src.auth; import src.cmt; import src.comms; import src.conn; import src.fakecore; import src.ocec; import src.tsl;
    except ImportError as e:
        xrint(Danger, "Conflicting module/s (Unknown), caused an exit. Tip: Update or Create issue on repository.")
        xrint(Warning, e)
        exit()
    xrint(Ok, "No conflicting scripts, that's good!", usprt=False)
    return True;


def login():
    print('''
 How to insert account information:

    => YourUsername, YourPassword, YourID 
    Note: Must be a string input type.

    ---- Login ----
    ''')
    usr = input(" => ")

    if usr.strip() == "":
        xrint(Warning, "Input cannot be empty, this caused an exit. Tip: Look at the note")
        exit()
    
    if o.typeval(usr, str)[0] is not True:
        xrint(Danger, "Invalid type of input, caused an exit. Tip: Look at the note")
        exit()

    usr = usr.replace(",", "")
    usr = usr.split()

    def __ver(usr=usr):
        for x in range(len(Worker)):
            if Worker[x]['Username'] == usr[0]:
                return x
        xrint(Danger, "Member name is not found. Cause an exit, What [red][bold]ARE[/][/] you")
        exit()
    
    _s = __ver()

    if Worker[_s]['Password'] != usr[1]:
        xrint(Warning, "Invalid password, if [bold]YOU[/] are not part of this. Go away!")
        exit()
    
    if Worker[_s]['ID'] != usr[2]:
        xrint(Warning, "Invalid ID, you should've know this! Who even are you? Rawr.")
        exit()

    xrint(Ok, "You got in!")
    return True, usr, _s

def main(toks, ld, lg):
    if toks[0] != True:
        xrint(Danger, "Something is wrong with this script token, how do you get in here?")
        exit()
    
    if toks[1][1] != Worker[toks[2]]['Password']:
        xrint(Warning, "Is token corrupted? Something is wrong with python.")
        exit()
    
    if toks[1][2] != Worker[toks[2]]['ID']:
        xrint(Warning, "Is token corrupted? Something is wrong with python.")
        exit()
    
    xrint(Ok, "Token is validated and it's true.")
    
    xrint(Information, "Confirming logs...")

    if ld[0] != True:
        xrint(Danger, "You're a bypasser, aren't you!?")
        exit()

    if lg[0] != toks:
        xrint(Danger, "You're a bypasser, aren't you!?")
        exit()

    xrint(Information, "Logs confirmed...")
    xrint(Ok, "Starting FSYS Interactive SHELL.")
    #time.sleep(2)
    shell(toks[1])

def shell(info):
    from rich.console import Console
    p = Console()
    import os
    import random
    msg_dy = ["This SHELL is still on beta, so EXPECT bugs."]
    ct = ['help', 'rbinfo', 'man', 'exit', 'clear', 'echo', 'dp']

    def _il_proc(cmt):
        
        cmt = cmt.split()

        if cmt == []:
            return False;
        token = len(cmt)

        if cmt[0] != "echo":
            for i in range(token):
                cmt[i] = cmt[i].lower()

        for i in range(token):
            cmt[i].strip()

        def _g():
            for i in range(len(ct)):
                if ct[i] == cmt[0]:
                    return True, i;
            return False, i;
            
        _p = _g()

        for i in _gpcmt():
            if i in ct:
                continue
            print("")
            xrint(Danger, "Program interupted & crashed to prevent faulty scripts to run.")
            xrint(Information, "Create an issue on github!")
            print("\n Details:")
            print(" |-> src ")
            print("  |->> cmt.py\n")
            print(f" Unknown built-in shell command in cmt.py (Module), The unknown command is '{i}'")

            sys.exit(1)


        if cmt[0] not in _gpcmt() and cmt[0] in ct:
            print(" Command available, but the developer has not implement a function yet into the command. SORRY!\n")
            return False;
        if _p[0] != True:
            print(f" Command named '{cmt[0]}' is not available, Use 'help' for commands.\n")
            return False;

        _pcmt(cmt=cmt, token=token, ct=ct)

    os.system('clear')
    
    print(f'''
   _._     _,-'""`-._       | Hey! You're finally here {info[0]} 
 (,-.`._,'(       |\`-/|    | Welcome to FSYS Shell, kind of like roblox C2! 
     `-.-' \ )-`( , o o)    | Use 'help' command to explore more different commands!
           `-    \`_`"'-    | Goodluck and Have fun! Miaw

    Message of the DAY, {msg_dy[random.randint(0, len(msg_dy)-1)]}
    '''
    )

    while True:
        _il = p.input(f" [cyan]{info[0].lower()}[/] @ [green]yorgc[/] # ")
 
        if _il_proc(_il) != True:
            continue