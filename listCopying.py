# list copying

def equaltoOperator():
    a = [1,2,3,4,5]
    b = a
    a.append(6)
    print(a == b)   # => True

def listSlicing():
    a = [1,2,3,4,5]
    b = a[:]
    a.append(6)
    print(a == b)   # => False

def copyMethod():
    a = [1,2,3,4,5]
    b = a.copy()
    a.append(6)
    print(a == b)   # => False

def listComprehension():
    a = [1,2,3,4,5]
    b = [item for item in a]
    a.append(6)
    print(a == b)   # => False  

def shallowCopying():
    a = [[1,2],[2,3]]
    b = a.copy()
    # It shows that a and b refer to different lists
    # But the elements in them still refer to same list.
    print(a is b)   # => False
    print(a[0] is b[0]) # => True
    
    
if __name__ == "__main__":
    # The new list will refer to the same list object.
    equaltoOperator()
    # The new list will refer to a new list Object. 
    listSlicing()
    copyMethod()
    listComprehension()
    # Shallow Copying
    shallowCopying()
