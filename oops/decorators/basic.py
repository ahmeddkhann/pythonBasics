def checkCredentials(function):
    def wrapper(*args, **kwargs):
       checker = input("do you have CNIC? if yes enetr y if no enter n ")
       if checker == "y" or checker == "Y":
           print("ok you have the cnic")
           print("let us verify the CNIC")
           return function(*args, **kwargs)
       elif checker == "n" or checker == "N":
           print("ok you dont have the cnic")
           print("we can not let you in")
       else:
           print("invalid input")
    return wrapper

def verifyCredentials(function):
    def wrapper(*args, **kwargs):
       cnic = input("enter the cnic ")
       if cnic == "1234567890":
           print("your cnic is verifies")
           print("you can enter to academy")
           return function(*args, **kwargs)
       else:
           print("your cnic is not verified")
        
    return wrapper

@checkCredentials
@verifyCredentials
def greetings(name, profession):
    print("welcome to python learning academy")
    print("here you will learn about python and more languages also.")
    print(f"so your name is {name} and your profession is {profession}")

greetings("Ahmed", "programmer")


# so basically decortaors are the function that accepts a function in argument and the nested function accepts the arguments of the passed function
# and the nested function returns the result of passed function. when to use a decorator, we use @ and the function name above the function that should
# be decorated.