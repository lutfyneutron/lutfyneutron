def decorator(f):
    def wrapper():
        print("About to run the function ...")
        f()
        print("Done with the function.")
    return wrapper


@decorator
def hello():
    print("Hello")


hello()
