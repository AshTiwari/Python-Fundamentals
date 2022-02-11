""" Generators """

def generate123():
    yield 1
    yield 2
    yield 3
    
def generatorWorking():
    """ shows how `next()` and `yield` works """
    print("\nshows how `next()` and `yield` works ")
    g1 = generate123()
    print(next(g))
    print(next(g))
    print(next(g))

def generatorObjectIds():
    """ for multiple generator_object, each have a different id """
    print("\nfor multiple generator_object, each have a different id ")
    g1 = generate123()
    g2 = generate123()
    if g1 is not g2:
        print("g1 is not g2")
        print(f"g1: {g1}")
        print(f"g1: {g2}")    

def generatorObjectAdvances():
    """ different generator_objects advances independently """
    print("\ndifferent generator_objects advances independently ")
    g1 = generate123()
    g2 = generate123()
    next(g1)
    if next(g1) != next(g2):
        print("g1 and g2 advancing independently.")
        print(f"next(g1) = {next(g1)}")
        print(f"next(g2) = {next(g2)}")

def resumeExecutionUtil():
    '''The second print statement is executed after the second `next()` is called.'''
    print('\nThe second print statement is executed after the second `next()` is called.')
    print('First Yield.')
    yield 1
    print('Second Yield.')
    yield 2

def resumeExecution():
    '''The generator function is only executed until the yield is reached.
        It resumes execution from last yield the next time it is called.'''
    g = resumeExecutionUtil()
    next(g)
    next(g)

def yieldingWithForLoop():
    '''yield values from generator without `next()`.
        The generator returned by `generate123()` generator function is iterated over by for loop. '''
    print('\nyield values from generator without `next()`')
    for item in generate123():
        print(item)
        
if __name__ == "__main__":
    generatorObjectIds()
    generatorObjectAdvances()
    resumeExecution()
    yieldingWithForLoop()
