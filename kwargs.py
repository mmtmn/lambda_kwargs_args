def join(**kwargs):
    final = ""
    for values in kwargs.values():
        final += values
    return final

print(join(a="Hello ", b="from ", c="kwargs ", d="!"))