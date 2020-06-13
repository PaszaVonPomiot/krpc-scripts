import curses
import fc
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def flight_controller(stdscr):
    terminal(stdscr, flight_controller_menu)
    pass
    # fc.connect_and_loop('Flight Controller')

def flight_monitor():
    pass

def vessel_inspector():
    pass


def flight_script_1():  # import this
    pass


main_menu= [
    {'idx': 0, 'function': flight_controller},
    {'idx': 1, 'function': flight_monitor},
    {'idx': 2, 'function': vessel_inspector}
    ]

flight_controller_menu = [
    {'idx': 0, 'function': flight_script_1},
    {'idx': 1, 'function': flight_script_1},
    {'idx': 2, 'function': flight_script_1}
]        



def print_menu(stdscr, menu, selected_row_idx: int) -> None:
    stdscr.clear()
    stdscr.box()
    h, w = stdscr.getmaxyx()
    for row in menu:
        name = row['function'].__name__.replace('_', ' ').capitalize()
        x = w//2 - len(name)//2
        y = h//2 - len(menu)//2 + row['idx']
        if row['idx'] == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, name)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, name)
    stdscr.refresh()



def terminal(stdscr, menu):
    ''' Main terminal screen flow '''

    def menu_loop():
        current_row_idx = 0
        while True:
            print_menu(stdscr, menu, current_row_idx)
            key = stdscr.getch()
            stdscr.clear()
            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # return function for selected item
                selected_function = [ row['function'] for row in menu if row['idx']==current_row_idx ][0]  
                selected_function(stdscr)
            elif key == 27:  # ESC
                break

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    menu_loop()

if __name__ == '__main__':
    curses.wrapper(terminal, main_menu)  # start terminal(stdscr, main_menu)

