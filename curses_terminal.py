import curses
import fc
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def flight_controller():
    fc.connect_and_loop('Flight Controller')

def flight_monitor():
    pass

def vessel_inspector():
    pass

# menu = ['Flight Controller', 'Flight Monitor', 'Vessel Inspector']
menu= [
    {'idx': 0, 'name': 'Flight Controller', 'function': flight_controller},
    {'idx': 1, 'name': 'Flight Monitor', 'function': flight_monitor},
    {'idx': 2, 'name': 'Vessel Inspector', 'function': vessel_inspector}
    ]
        

def print_menu(stdscr, selected_row_idx: int) -> None:
    stdscr.clear()
    stdscr.box()
    h, w = stdscr.getmaxyx()
    for row in menu:
        x = w//2 - len(row['name'])//2
        y = h//2 - len(menu)//2 + row['idx']
        if row['idx'] == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row['name'])
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row['name'])
    stdscr.refresh()

def terminal(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    current_row_idx = 0

    while True:
        print_menu(stdscr, current_row_idx)
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # return function for selected item
            selected_function = [ row['function'] for row in menu if row['idx']==current_row_idx ][0]  
            selected_function()
        elif key == 27:  # ESC
            break

    curses.napms(10)

if __name__ == '__main__':
    curses.wrapper(terminal)  # start terminal

