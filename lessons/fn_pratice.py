"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out two numbers"""
    if number1 >= number2:
        return number1
    else: #number 1 < number2
        return number2
    
max_number: int = my_max(1,10)
ohter_max_number: int = my_max(11,3)
print(ohter_max_number)

def hello_n(n: int) -> int:
    """A silly example function"""
    return "hello " + str(n)
print(hello_n(3))