import os
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('-'*60)
        os.system('ping -n 10 {}'.format(ip))
        print('-'*60)
