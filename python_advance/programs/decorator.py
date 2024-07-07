def decorator(func):
    def wrapper():
        print("\nrunning",func.__name__)
        func()
        print("end of",func.__name__,"\n")
    return wrapper


@decorator
def do_this():
    print("doing this")

@decorator
def do_that():
    print("doing that")

do_that()
do_this()