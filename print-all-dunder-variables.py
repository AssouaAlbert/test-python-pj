def generate_dunder_variables():
    dunder_variables = []
    for name in dir(__builtins__):
        if name.startswith('__') and name.endswith('__'):
            dunder_variables.append(name)
    return dunder_variables
if __name__ == "__main__":
    dunder_vars = generate_dunder_variables()
    print("Dunder variables in the built-in namespace:")
    for var in dunder_vars:
        print(var)
        print(f"Value of {var}: {getattr(__builtins__, var)}")