''' Useful example of generators '''

def fibonnaci():
    ''' Helpful when you want to access the fibonacci number only once. '''
    yield 0
    yield 1
    yield 1
    a = b = 1
    while True:
        a, b = b, a+b
        yield b

if __name__ == "__main__":
    f = fibonacci()
    print(next(f))
    print('Press y to continue or any other key to stop.')
    while(input().lower() == 'y'):
        print(next(f))
        
