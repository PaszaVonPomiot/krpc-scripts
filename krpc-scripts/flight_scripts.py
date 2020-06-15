import time

def launch_to_orbit(c, params):
    vessel = conn.space_center.active_vessel
    vessel.auto_pilot.target_pitch_and_heading(90, 90)
    vessel.auto_pilot.engage()
    vessel.control.throttle = 1
    time.sleep(1)
    print('Launch!')
    vessel.control.activate_next_stage()
