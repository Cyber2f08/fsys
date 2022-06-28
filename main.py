import config as cfg
import gc
gc.disable()
from src.tsl import Information, Ok, xrint
from rich import pretty
from src import comms

# For steps verification. informations...
log_ld = []
log_lg = []
m = print

def _wcbanner():
    print(
  '''
    _._     _,-'""`-._        | Meow, Oh Hi!                          |
  (,-.`._,'(       |\`-/|     | Welcome to FSYS,                      |
      `-.-' \ )-`( , o o)     | Please wait while the systems loads.. |
            `-    \`_`"'-     | - Cyb2f                               |
  '''
    )

if __name__ == "__main__":
  from rich.console import Console  
  import time
  p = Console()
  _wcbanner()
  m(" => Loading... (ver, 0.0.1)")

  stlod = time.perf_counter()
  sld = comms.load()  
  stod = time.perf_counter() - stlod 
  p.print(f" [blue]Done[/] in [green bold]{stod:.2f}s[/]")

  xrint(Information, "Login is screen is going to pop up below this.")
  
  toksr = comms.login()
  
  log_lg.append(toksr)
  log_ld.append(sld)

  comms.main(toks=toksr, ld=log_ld, lg=log_lg)
