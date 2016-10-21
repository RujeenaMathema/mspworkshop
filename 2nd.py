def sum(*numbers):
    sum=0
    for number in numbers:
        sum +=number
        return sum
    

print(sum(2,3))
print(sum(1,2,3))

def sum(*numbers):
    sum=0
    for number in numbers:
        if number<0:
            continue
        sum +=number
    return sum
    

print(sum(2,3))
print(sum(1,2,3))
print(sum(2,2,-2))

    
