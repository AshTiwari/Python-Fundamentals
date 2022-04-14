# Law Of Demeter

class A:
    def __init__(self, objectOfB, objectOfC):
        self.objectOfB = objectOfB
        self._objectOfC = objectOfC

    # follows the principle of Law Of Demeter.
    def methodOfC(self):
        return self._objectOfC.methodOfC()

    # Doesn't follow Law of Demeter.
    def methodOfB(self):
        return self.objectOfB.methodOfB()

class B:
    def methodOfB(self):
        return "B"

class C:
    def methodOfC(self):
        return "C"

if __name__ == "__main__":
    c = C()
    b = B()
    a = A(b, c)
    print(a.methodOfC())
    print(a.methodOfB())
