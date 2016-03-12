import time
from util.constants import LAST_READ


def write_last_read():
    with open(LAST_READ, 'w') as file:
        file.write(str(int(round(time.time() * 1000))))


def last_read():
    with open(LAST_READ, 'r') as file:
        return int(file.read())
