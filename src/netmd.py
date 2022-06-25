from rich.console import Console
from requests.exceptions import *
import requests as rq

p = Console()

def _reg(uri: str, domain: str, scheme: str = "https") -> bool:
    
    try:
        tst = rq.get(uri)
    except ConnectionError:
        p.print(f" [red]err[/] -- [green]{domain}[/] -- [yellow]conerror[/]")
        p.print(f" [blue]deb[/] -- [green]{domain}[/] -- [blue]No Connection.[/]")
        return False;
    except ConnectionRefusedError:
        p.print(f" [red]err[/] -- [green]{domain}[/] -- [yellow]conreferr[/]")
        p.print(f" [blue]deb[/] -- [green]{domain}[/] -- [blue]No Connection. Refused to connect[/]")
        return False;
    except ConnectionResetError:
        p.print(f" [red]err[/] -- [green]{domain}[/] -- [yellow]conreserr[/]")
        p.print(f" [blue]deb[/] -- [green]{domain}[/] -- [blue]No Connection. Connection resetted[/]")
        return False;
    except ConnectionAbortedError:
        p.print(f" [red]err[/] -- [green]{domain}[/] -- [yellow]conaberr[/]")
        p.print(f" [blue]deb[/] -- [green]{domain}[/] -- [blue]No Connection. Connection Aborted[/]")
        return False;
    p.print(f" rev -- {domain}")