# Common functions

# Calling Remote Procedures

# Converting Remote Procedure to Protocol Buffer message that can be used by Expressions
# protobuff_message = c.get_call(getattr, object_to_get_data_from, 'attibute_name_from_object') 
mean_altitude = c.get_call(getattr, flight, 'mean_altitude')

# Expressions work on messages
expr = c.krpc.Expression.greater_than(
    c.krpc.Expression.call(mean_altitude),
    c.krpc.Expression.constant_double(1000)
    )

# Create an event from the expression
event = c.krpc.add_event(expr)

# Display message
c.ui.message('dupa', 3)

# List vessel parts
vessel_parts = [ 
    {'title': part.title,
     'name': part.name,
     'attachment': 'A' if part.axially_attached else 'R' if part.radially_attached else 'X',
     'stage': part.stage,
     'decouple_stage': part.decouple_stage,
     'mass': part.mass,
     'dry_mass': part.dry_mass,
     }
    for part in vessel.parts.all ]

