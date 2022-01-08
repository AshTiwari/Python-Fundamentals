# LEGB scope

global_var1 = "Global Variable 1"
global_var2 = "Global Variable 2"  

class enclosingClass:
    enclosing_var1 = "Enclosing Variable 1 in Class"

    def __int__(self):
        print("Global variable 1 and 2 before local functions.")
        self.checkVaraibles()
        self.local_func1()
        self.local_func2()
        print("Global variable 1 and 2 after local functions.")
        checkVariables()
        
    def local_func1(self):
        local_var1 = "Local Variable 1"        
        # below variable will be treated as local variable 
        # and will not update global variable.
        global_var1 = local_var1
        
    def local_func2(self):
        global global_var2
        # updating this will update global variable.
        global_var2 = "Global Var updated in local scope."
        
    def checkVariables(self):
        global global_var1, global_var2
        print(f"Global Var 1: {global_var1}")
        print(f"Global Var 2: {global_var2}")

 
        
def enclosingFun():
    enclosing_var2 = "Enclosing Variable 2 in Function."
    enclosing_var3 = "Enclosing Variable 3 in Function."
    
    def checkVariables():
        nonlocal enclosing_var2, enclosing_var3
        print(f"Enclosing Var 2: {enclosing_var2}")
        print(f"Enclosing Var 3: {enclosing_var3}")
    
    def local_func2():
        local_var2 = "Local Variable 2"
        # below variable will be treated as local variable 
        # and will not update enclosing variable.
        enclosing_var2 = local_var2

    def local_func3():
        nonlocal enclosing_var3
        # updating this will update enclosing variable
        enclosing_var3 = "Enclosing var updated in Local Scope."

    print("Enclosing variable 2 and 3 before local functions.")
    checkVariables()
    local_func2()
    local_func3()
    print("Enclosing variable 2 and 3 after local functions.")
    checkVariables()
    
        
if __name__ == "__main__":
    encClass = enclosingClass()
    enclosingFun()



    
    
