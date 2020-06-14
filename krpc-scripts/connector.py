#controller
import logging
import psutil
import socket
import curses
import krpc
import time


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def ksp_running() -> bool:
    ''' Check if game is running '''
    return 'KSP_x64.exe' in [ proc.info['name'] for proc in psutil.process_iter(['name']) ]

def krpc_running(host: str, port: int) -> bool:
    ''' Check if KRPC server is enabled '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host,port))
    sock.close()
    if result == 0:
        return True # open
    else:
        return False

def wait_for_flight(c) -> None:
    ''' Wait until KSP is in flight mode and not paused '''
    log.info('Waiting for flight game scene')
    while c.krpc.paused or c.krpc.current_game_scene.name != 'flight':
        time.sleep(3)

def main_loop(c) -> None:
    
    while True:
        bodies = c.space_center.bodies
        vessel = c.space_center.active_vessel
        print(bodies, vessel)
        break
    return None


def connect_and_run(func, params):
    ''' Make connection and keep it until main_loop exits '''
    name = func.__name__
    if not ksp_running():
        raise Exception(f'KSP is not running')
    if not krpc_running('127.0.0.1', 50000):
        raise Exception(f'KRPC is not running')
    log.info('Connecting to KRPC')
    with krpc.connect(name) as c:
        already_connected = sum([ True if name in client else False for client in c.krpc.clients ]) > 1
        if already_connected:
            c.close()
            raise Exception(f'Client {name} already connected')
        wait_for_flight(c)
        return func(c, params)



# if __name__ == '__main__':
#     curses.wrapper(ct.terminal)
    # connect_and_run('KSP Command Center')