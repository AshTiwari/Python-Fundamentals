''' Stateful Generator Function '''

def firstN(n, iterable):
    ''' This function returns the first `n` items of the `iterable`.
        It does a `lazy-evaluation`.
        
        Generator Function maintains the value of the variable `counter` apart from `item`
        to use it when the function resumes for the next evaluation. '''

    counter = 0
    for item in iterable:
        if counter == n:
            return
        counter += 1
        yield item

def unique(iterable):
    ''' This function returns the unique values on the iterable based on the first occurence.
        It does a `lazy-evaluation`.

        Generator Function maintains the state of the variable `see `
        to use it when the function resumes for the next evaluation.

        `see.add(item)` comes after `yield` statement and so it is executed only when the
        generator function resumes.
        Till then, the state of the `seen` and `item` is maintained. '''

    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

if __name__ == "__main__":
    for item in firstN(3, unique([1,2,2,3,3,4,5])):
        print(item)
