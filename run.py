__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import sys
from util.dispatcher import Dispatcher
from util.logger import logger

def run():
    """
    Bootstraps the application.
    """
    dispatcher = Dispatcher()

    cmd = None
    while True:
        cmd = input()
        if cmd:
            if cmd == 'exit':
                break
            else:
                response = dispatcher.dispatch(cmd)

if __name__ == '__main__':
    run()



