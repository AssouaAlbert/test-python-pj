import random

def random_number():
    return random.randbytes(1) * 100
if __name__ == "__main__":
    print(f"Random number between 1 and 100: {random_number().decode}")

