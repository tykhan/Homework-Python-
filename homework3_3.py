#solution for CodeWars
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {}!".format(name)



#solution2 
def greet():
    name = (input("Hi, what is your name?\n"))
    if name == "Johnny":
        print ("Hello, my love!")
    else:
        print ("Hello, {}!".format(name))
greet()