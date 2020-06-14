import time

def flight_script_1(c, params):
    print(params)
    conn = c
    vessel = conn.space_center.active_vessel
    vessel.auto_pilot.target_pitch_and_heading(90, 90)
    vessel.auto_pilot.engage()
    vessel.control.throttle = 1
    time.sleep(1)
    print('Launch!')
    vessel.control.activate_next_stage()