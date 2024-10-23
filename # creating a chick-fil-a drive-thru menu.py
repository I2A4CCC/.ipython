# creating  a function that creates a list containing a string for the name of the individual and their email address inside <>
def full_email(people):
    result = []
    for email, name, age in people:
        result.append("{} <{}> : {}".format(name, email, age))
    return result
print(full_email([("alex@example.com", "Alex Diego", "21"), ("shay@example.com", "Shay Brandt", "25")]))
        