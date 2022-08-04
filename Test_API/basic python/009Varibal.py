var_1 = 100  # Global variable
var_2 = 20  # Global variable

print(var_1, var_2)


def summ():
    # var_1 = 30  # Local variable
    # var_2 = 40  # local variable
    result = var_1 + var_2
    print(result)


def sub():
    var_2 = 30
    result = var_1 - var_2
    print(result)

summ()
sub()