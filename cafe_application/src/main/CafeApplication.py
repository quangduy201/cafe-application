import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from GUI.LoginGUI import LoginGUI
from GUI.HomeGUI import HomeGUI
from DTO.Account import Account

def main():
    # LoginGUI()
    HomeGUI(Account('AC003', 'longbott', '123', 'DE01', 'ST03', False))

