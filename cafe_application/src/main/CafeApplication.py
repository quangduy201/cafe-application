import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DTO.Account import Account
from GUI.HomeGUI import HomeGUI
from GUI.LoginGUI import LoginGUI


def main():
    # LoginGUI()
    HomeGUI(Account('AC000', 'admin', 'admin', 'DE00', 'ST00', False))

