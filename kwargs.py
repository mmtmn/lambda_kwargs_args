def join(**kwargs):
    """ this function concatenates values
        and variable names using kwargs
    """
    concatenates_values = ""
    concatenates_variable_names = ""

    for values in kwargs.values():
        concatenates_values += values
    for variable_names in kwargs:
        concatenates_variable_names += variable_names
    return concatenates_values, concatenates_variable_names

print(join(a="Hello ", b="from ", c="kwargs ", d="!"))