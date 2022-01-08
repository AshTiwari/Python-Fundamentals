# List Repetition.

def listRepetetion():
    lst1 = [1,2,3,4,5]
    lst2 = lst1*2
    print(lst1)
    print(lst2)

def shallowRepetetion():
    lst1 = [[1,2],[3,4]]
    lst2 = lst1*2
    print(lst1)
    print(lst2)
    print(lst2[0] is lst2[2])   # => True
    print(lst2[1] is lst2[3])   # => True


if __name__ == "__main__":
    listRepetetion()
    shallowRepetetion()
