"""
    *args doesn't need the "args" part, it needs the asterisk,
    therefore it could be *anythingyouwant and the same
    logic would be applied
"""

def test_var_args(t_arg, *args):
    print("first normal arg:", t_arg)
    for arg in args:
        print("another arg through *args:", arg)

test_var_args('science', 'tecnology', 'love', 'existence')

"""
    So, what is happening here? 
    Basicly args packs together all variables
    after the ones we directly called
    The function bellow should make it even easier to understand
"""

def simpler_args_function(a, b, *args):
    print(a, b, args)
    print(args)

simpler_args_function(1,2,3,4,5,6)

"""
    the output of the above function is:
    1 2 (3, 4, 5, 6)
    (3, 4, 5, 6)
"""

def warming_up(*args):
    print(args)
    print(*args)

test_list = [1,2,3,4,5]
warming_up(*test_list)
"""
    Output: 
    (1, 2, 3, 4, 5)
    1 2 3 4 5
"""
