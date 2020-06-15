import krpc
c = krpc.connect('devconsole')
conn = c
vessel = conn.space_center.active_vessel
flight = vessel.flight()