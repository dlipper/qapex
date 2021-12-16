# qapex # -*- coding: utf-8 -*-
"""
NAME: QApEx
VERSION: 0.0.2
COMMIT: GitHub Commit test
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
DESCRIPTION = ''' Simple tool to manipulate IBM QRadar data through API from command line as batch tasks or in interactive pseudo-shell. '''

__all__ = ['qapex']

"""Base constants and paths """


"""The list of command-line arguments """
ARGUMENTS = {
    'v':
    {
        'help': 'verbose',
        'dest': 'verbose',
        'type': 'flag'
    }
}

class QApEx:
    """Main module functional object wrapper.

    <descr>
    Args:
        arg1(type): descr
    Attributes:
        attr1(type): descr
    """

    def __init__(self, args):
        # Init properties
        pass

    def run(self):
        """ Run the main operation 
        Args:
            none
        Result:
            none
        """
        pass

# main function entry point


def main():
    """Parse the comand line arguments."""
    parser = argparse.ArgumentParser(
        description=DESCRIPTION)
    for arg in ARGUMENTS.keys():
        curarg = ARGUMENTS[arg]
        if curarg['type'] == 'mandatory':
            parser.add_argument(
                arg, help=curarg['help'])
        elif curarg['type'] == 'optional':
            parser.add_argument(
                '--'+arg, dest=curarg['dest'], help=curarg['help'])
        elif curarg['type'] == 'flag':
            parser.add_argument(
                '-'+arg, dest=curarg['dest'], action='store_true', help=curarg['help'])
    args = parser.parse_args()
    qr = QApEx(vars(args))
    qr.run()


if __name__ == '__main__':
    main()
