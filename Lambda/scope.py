# LEGB

# Local
#        - Local scope looks at the function and what is being passed, it looks in the available scope
# enclosed
#        - special case when there is a function within a function, call inner which is enclosed in the outer
# global
#        - Looks at the entire scope within a module
# Built-in
#        - looks through the scope chain to check the functions and to check if it's built in e.g. print(), type()

# avoid messing with the order of LEGB scopes

