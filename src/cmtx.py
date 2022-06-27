def _dp_proc(cmtx: list, mode: str):
    import time
    import requests
    import math
    from rich.console import Console  

    p = Console()

    av_rbcore = [""]        
    
    for i in range(cmtx[1]):
        cmtx[0][i].strip

    if mode == "pysh":
        ltemp = 0
        for i in cmtx[0][0:]:
            if i == "exit()":
                p.print(" To [red]EXIT[/] the [red]SHELL[/], [red]QUIT[/] the mode first then [red]EXIT[/] the [red]SHELL[/].")
                return False, True;
            if i == "exit":
                try:
                    if cmtx[0][ltemp+1] == "()":
                        p.print(" To [red]EXIT[/] the [red]SHELL[/], [red]QUIT[/] the mode first then [red]EXIT[/] the [red]SHELL[/].")
                        return False, True;
                except IndexError:
                    pass
            ltemp += 1

        if cmtx[0][0] == ".quit":
            return False, "";
        if cmtx[0][0] == ".help":
            print('''
 -----------------:
 COMMANDS:
     .help          | Display this Help.
     .quit          | Quit this Mode
            ''')
            return False, True

        for i in cmtx[0][0:]:
            if "import" in i:
                p.print(" Importing modules outside of the shell is [red]FORBIDDEN[/]")
                return False, True;
        djoin = ' '.join(cmtx[0][0:])+" "
        try:
            #p.print(" "+str(cmtx))
            eval(djoin)
        except Exception as e:
            p.print(e)
        return False, True;
