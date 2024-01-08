import time
# Creating a Decorator
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # DO something before
        function()
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

# Another way to call/use the decorator
decorated_function = delay_decorator(say_greeting)
decorated_function()