def mul(*numbers):
    mul=1
    for number in numbers:
        mul *=number
    return mul
print(mul(1))
print(mul(1,2,3))
print(mul(11,4))
