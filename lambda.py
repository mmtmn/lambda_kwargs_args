"""
    the lambda function is withing the first set
    of parentheses, the value we wish to test on
    the lambda function is in the secound set of
    parentheses
"""
add_one = (lambda x : x + 1)(3)
print(add_one)

job_role = (lambda seniority, area: f"Job Role: {seniority.title()} {area.title()}")
print(job_role("Junior", "Backend Development"))