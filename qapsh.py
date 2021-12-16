# qapsh
# -*- coding: utf-8 -*-
"""
NAME: QApEx Interactive Shell
VERSION: 0.0.1
COMMIT: First Commit
AUTHOR: Dmytro Petrashchuk
EMAIL: dpgbox@gmail.com

Prerequisites for script
    1. Install Python 3.7 or later
    2. Install additional packages with "pip install -r requirements.txt"
    3. Use command line parameters
    4. Try -h option to get detailed help on usage
    5. Look into the code to get additional insights
    6. Don't stop yourself to use this script as you want and suggest your changes
"""

import argparse
import requests
from datetime import datetime

# Ignore SSL-warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

"""Place the program description here """
DESCRIPTION = ''' Interactive shell to run commmands against IBM QRadar API and interact with it in CLI.'''

__all__ = ['qapsh']

"""Base constants and paths """

def main():
    pass

if __name__ == '__main__':
    main()