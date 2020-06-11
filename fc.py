# Flight controller
import krpc
import time


def main_loop(c):
    while True:
        while c.krpc.paused or c.krpc.current_game_scene.name != 'flight':  # wait for flight mode
            time.sleep(3)
        bodies = c.space_center.bodies
        vessel = c.space_center.active_vessel
        print(bodies, vessel)
        break


def connect_and_loop(name):
    with krpc.connect(name) as c:
        already_connected = sum([ True if name in client else False for client  in c.krpc.clients ]) > 1
        if already_connected:
            c.close()
            raise Exception(f'Client {name} already connected')
        return main_loop(c)

connect_and_loop('Flight Controller')