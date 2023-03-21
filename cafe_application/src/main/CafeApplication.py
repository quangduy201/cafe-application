import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAL.AccountDAL import AccountDAL
from DTO.Account import Account


def main():
    print("Hello world!")
