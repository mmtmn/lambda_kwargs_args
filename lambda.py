"""
    the lambda function is withing the first set
    of parentheses, the value we wish to test on
    the lambda function is in the secound set of
    parentheses
"""
add_one = (lambda x : x + 1)(10)
print(add_one)


"""
    this is how a f-string works in python, it is
    important that we are looking at this before
    seeing the next lambda exemple as knowing this
    is a prerequisite
"""
galaxy = "Milky Way"
planet = "Earth"
age =  4.54
units = "billion years old"

print("%s is in the %s" % (planet, galaxy)) # uses % to get variables
print("%s is %.2f %s" % (planet, age, units)) #.2f limits the float value
"""
    Output: Earth is 4.54
            Earth is 4.54 billion years old
"""

print("{} is in the {}".format(galaxy, planet)) # uses empty dicts and .format
print("{} is {} {}".format(planet, age, units)) # more complexity
print("{} is {} {} and is in the {}".format(planet, age, units, galaxy)) # more complexity
"""
    Output: Milky Way is in the Earth
            Earth is 4.54 billion years old
            Earth is 4.54 billion years old and is in the Milky Way
"""

print(f"{planet} is {age} years old")
print(f"{planet} is in {galaxy} and is {age} {units} old.")
"""
    Output: Earth is 4.54 years old
            Earth is in Milky Way and is 4.54 billion years old old
"""


"""
    the lambda function sets two parameters at first
    and then useses python's f-string to concatenate
    the seniority and the area to print out the job
    role
"""
job_role = (lambda seniority, area: f"Job Role: {seniority.title()} {area.title()}")
print(job_role("junior", "backend dev"))
"""
    Output: Job Role: Junior Backend Dev

    So you might be asking yourself, ok, but why did we use .title?
    Here is why: The .title() method in python transforms every
    first letter of a word inside variable and turns it into an 
    uppercase letter
"""



"""
    Ok, so now we will see lambda in action with 
    a interpeter-only feature!
"""
_ = lambda x, y: x + y
print(_(1,2))
"""
    Output: 3

    Ok, so here we see the interpeter-only feature as a
    underscore:
        It's just a variable name, and it's conventional in python
        to use _ for throwaway variables. It just indicates that the
        loop variable isn't actually used.
"""

"""
    Now we will se how to use nested lambda functions!
"""
lambda_function = (lambda x, your_function: x + your_function(x))
nested_lambda = lambda_function(2, lambda x: x * x)
print(nested_lambda)
nested_lambda2 = lambda_function(4, lambda x: x + 5)
print(nested_lambda2)
"""
    Outputs: 6
             13

    In this exemple, python exposes higher-order functions 
    as built-in functions or in the standard library
"""