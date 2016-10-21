def change_list(mylist):
    mylist = [1,2,3]
    print("value inside function",mylist)
    return
mylist = [5,6,7]
print("value outside the function:",mylist)
change_list([1,5])

print("------------------------------------------")
def change_list(name, age):
    mylist = [1,2,3]
    print("name is",name)
    print("age is",age)
    return
change_list("rujeena",19)
change_list(19,"namrata")
change_list(age=19, name="rujeena")
print("------------------------------------------")
def change_list(name, age=19):
    mylist = [1,2,3]
    print("name is",name)
    print("age is",age)
    return
change_list("rujeena")
change_list("namrata")
change_list( name="rujeena")
