from src.conn import _get_muser_info, _get_user_info, _get_user_primary_group, _get_roblox_info
from requests.exceptions import *
from src.cmtx import _dp_proc
import os
import src.ocec as o
import src.tsl as t
import random, sys

Tips = ["Use exit instead of CTRL-C because it will make the shell BROKE."]
cmod = ""

def cmit():
    return "\n";

def cmout():
    return "\n"

def _gpcmt():
    return ["help", "exit", "clear", "rbinfo", 'echo', 'dp']


def _pcmt(cmt: list, token: int, ct: list):
    if cmt[0] == "help":
        print(f'''
 Help used to display commands and it's function on the shell.
 For more information about a command use 'man command-name'

 COMMANDS:
     help        | Help used to display commands and it's function.
     man         | Command to see more detailed help of a other command.
     echo        | Echoes word you type.
     clear       | Clear terminal screen to make it look clean.
     rbinfo      | Get roblox informations / infos.
     dp          | Change or switch shell mode to what you prefer on.
     exit        | Exit the shell.

 Tips: {Tips[random.randint(0,len(Tips)-1)]}
        ''')
    elif cmt[0] == "exit":
        if token > 1: # Only has 1 subcommand and ignores the other.
            if o.typeval(cmt[1], str)[0] == True:
                print(f" Exit Code. {cmt[1]}")
                sys.exit(int(cmt[1]))
        sys.exit(0)

    elif cmt[0] == "clear":
        os.system('clear')

    elif cmt[0] == "rbinfo":
        from rich.console import Console
        import requests
        p = Console()
        try:
            _s1 = requests.get("https://www.google.com")
        except ConnectionError:
            p.print(" No Connection at this time.")
            return;
        '''
        => -p       | Choose operating system. (DEFAULT: Windows)
        '''
        if token > 1: # Have 3 subcommand and ignores the other.
            if cmt[1] == "macos":
                p.print(cmout()+" rev -- [blue]setup.roblox.com[/] -- wait")
                _s = _get_roblox_info(platform=cmt[1])
                _sp = 0
                for i in _s[2]:
                    if i == 200:
                        _sp += 1
                p.print(f" reqt -- [blue]setup.roblox.com[/] -- [green]$[/]:{str(_sp)} [red]!![/]:{str(len(_s[2])-_sp)}")
                print(" RESULT ---------------")
                print(" ===> Roblox: ")
                p.print(f"  -> Version: {_s[0]}")
                p.print(f"  -> Studio version: {_s[1]}"+cmit())
                return;
            elif cmt[1].lower() == "windows":
                pass
            else:
                print(f" Roblox does not have version for '{cmt[1].strip()}'"+cmit())
                return;
        p.print(cmout()+" rev -- [blue]setup.roblox.com[/] -- wait")
        
        _s = _get_roblox_info()
        _sp = 0
        for i in _s[3]:
            if i == 200:
                _sp += 1
        p.print(f" reqt -- [blue]setup.roblox.com[/] -- [green]$[/]:{str(_sp)} [red]!![/]:{str(len(_s[3])-_sp)}")
        print(" RESULT ---------------")
        print(" ===> Roblox: ")
        p.print(f"  -> Version: {_s[0]}")
        p.print(f"  -> Studio version: {_s[1]}")
        p.print(f"  -> QT Studio version: {_s[2]}"+cmit())

    elif cmt[0] == "echo":
        if token == 1:
            return;
        txt = ' '.join(cmt[1:])+" "
        print(' '+txt)
    
    elif cmt[0] == "dp":
        
        from rich.console import Console 
        avm = ['rbcore', 'consv', 'pysh']
        notimp = ['consv']
        p = Console()

        def c2list(com: str) -> list:

            com = com.split()
            if com == []:
                return False;
            
            token = len(com)
            return [True, com, token];


        def _it_dp(mode: str):
            global cmod

            print("")

            if mode == "pysh":
                cmod = mode
                print(" Available limited secure modules have been imported, such as: math, time, requests")
                print(" Exit mode using '.quit' and get more commands using '.help'")
                print(" Happy Hacking!\n")
            

            while True:
                
                if cmod == "":
                    print("")
                    break

                _dp = p.input(f" + [yellow]{mode}[/] @> ")
                
                if _dp.strip() == "":
                    continue
                _dp_l = c2list(_dp)

                if _dp_l[0] != True:
                    continue

                mptmp = _dp_proc(_dp_l[1:], mode)
                if  mptmp[0] != True:
                    if mptmp[1] == "":
                        cmod = ""
                    continue

        
        htxt = '''
 dp used to switch mode on the shell and it's function on the shell you switch on.
 For more information about a command use 'man command-name'

 MODES:
     rbcore         | Interact with roblox api.
     consv          | Lively reloaded configuration editor. (NOT IMPLEMENTED YET)
     pysh           | Python Shell Alike.
    
 EXAMPLES:
     - dp rbcore    | Initialize rbcore internal shell.
     - etc..

 Have fun hacking!
        '''
        if token > 1:
            if cmt[1].strip() not in avm:
                print(" Error: Invalid Mode")
                print(htxt)
                return;
            if cmt[1].strip() in notimp:
                print(" Error: Mode not implemented.")
                return;
            
            _it_dp(cmt[1])
            return;
        print(" Error: Insufficient args")
        print(htxt)

