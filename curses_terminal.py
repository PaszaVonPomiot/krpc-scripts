import curses

menu = ['Flight Controller', 'Flight Monitor', 'Vessel inspector']

def print_menu(stdscr, selected_row_idx: int) -> None:
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def terminal(stdscr):
    stdscr.box()
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
            # stdscr.addstr(0, 0, "You pressed Down key!")
        elif key == curses.KEY_ENTER or key in [10, 13]:
            pass
        elif key == 27:  # ESC
            break

    curses.napms(100)

if __name__ == '__main__':
    curses.wrapper(terminal)  # start terminal

