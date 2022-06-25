import config as cfg
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
    _._     _,-'""`-._         | Meow, Oh Hi!                          |
  (,-.`._,'(       |\`-/|     | Welcome to FSYS,                      |
      `-.-' \ )-`( , o o)     | Please wait while the systems loads.. |
            `-    \`_`"'-     | - Cyb2f                               |
  '''
    )

if __name__ == "__main__":
  
  _wcbanner()
  m(" => Loading... ")

  sld = comms.load()  
  xrint(Information, "Login is screen is going to pop up below this.")
  
  toksr = comms.login()
  
  log_lg.append(toksr)
  log_ld.append(sld)

  comms.main(toks=toksr, ld=log_ld, lg=log_lg)
