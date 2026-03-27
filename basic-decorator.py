def basic_decorator(func):
    def wrapper():
        print("Before the function is called.")
        print(f"Calling function: {func().upper()}")
        print("After the function is called.")
    return wrapper
@basic_decorator
def say_hello():
    return "Hello, World!"
if __name__ == "__main__":
    say_hello()