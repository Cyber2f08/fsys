from rich.console import Console
from rich import print
from rich import pretty

p = Console()
Danger = ("Danger", "red", "!!")
Warning = ("Warning", "yellow", "!")
Information = ("Information", "blue", "?")
Ok = ("OK", "green", "OK")

def xrint(type, text, usprt=False):
    if usprt != False:
        pretty.install()
        p.print(f" [ [{type[1]}]{type[2]}[/] ] => {text} ")
    else:
        p.print(f" [ [{type[1]}]{type[2]}[/] ] => {text} ")