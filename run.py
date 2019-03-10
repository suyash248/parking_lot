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

    input_file_path = sys.argv[1] if len(sys.argv) > 1 else None
    if input_file_path:
        try:
            with open(input_file_path, "r") as f:
                for cmd in f:
                    response = dispatcher.dispatch(cmd)
        except FileNotFoundError:
            logger.error("No such file: {}".format(input_file_path))

    else:
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



