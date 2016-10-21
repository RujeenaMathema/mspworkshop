argument = 3
def number(*argument):
    argument = 4
    print("local variable",argument)
number()
print("global",argument)
