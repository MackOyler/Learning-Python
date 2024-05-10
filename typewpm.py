import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello,Clarice")
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)