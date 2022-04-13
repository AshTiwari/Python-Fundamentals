''' (not) keywoard Self '''

class Class:
    ''' First parameter of a method represents it's object/instance.
        Generally 'self' is used to represent it's object.
        Different methods can have different names for their object/instance.
    '''

    def __int__(self):
        print(self)
    def method1(self1):
        print(self1)
    def method2(self2):
        self2.method1()
        print(self2)
        
def objectMethodRepresentation():
    '''
    1. object_name.method_name() is eqvivalent to Class_name.method_name(object_name)
    2. However, first approach is used more oftern to give a narrative that
    " the method belongs to an object"
    intead of
    " the object is the first parameter of the method" '''
    
    object1 = Class()

    if object1.method1() == Class.method1(object1):
        print('object1.method1() is eqvivalent to Class.method1(object1)')

def needOfSelf():
    '''
    - One of the syntax for calling a method is 'Class.method1(obj)'
    - Hence, method takes an object as it's first parameter.  '''

    obj = Class()
    #other way of calling a method.
    Class.method1(obj)
    
if __name__ == "__main__":
    object1 = Class()
    object1.method1()
    object1.method2()
    objectMethodRepresentation()
    needOfSelf()
