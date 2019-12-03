import click
import yaml
import datetime
import sys
from lastnote_selenium import LastNote

import time

@click.group()
def cmd():
    pass

@cmd.command(help='Room reservation.')
@click.option('--event', required=True, type=str)
@click.option('--start', required=True, type=str)
@click.option('--term', required=True, type=int)
@click.option('--room', required=True, type=int)
def room_reserve(start, term, room, event):
    f = open("settings.yaml", "r")
    settings =   yaml.load(f, Loader=yaml.SafeLoader)
    
    lastnote = LastNote(settings)
    lastnote.login("nishi", "nishI")
    lastnote.room_reserve(datetime.datetime.strptime(start, "%Y%m%d%H%M"), term, room, event)
    lastnote.quit()

def main():
    cmd()

if __name__ == '__main__':
    main()
