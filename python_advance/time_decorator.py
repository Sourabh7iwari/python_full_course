import time
def decorator(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time() 
        print(f"Function '{func.__name__}' took {end - start:.6f} seconds")
    return wrapper


marks = int(input("enter marks"))

@decorator
def without_and(marks):
    if marks>100:
        print("marks high")
    elif marks>=90:
        print("A")
    elif marks>=80:
        print("B")
    elif marks>=70:
        print("C")
    else:
        print("fail")

@decorator
def with_and(marks):
    if marks>100:
        print("marks high")
    elif marks>=90 and marks<100:
        print("A")
    elif marks>=80 and marks<90:
        print("B")
    elif marks>=70 and marks<80:
        print("C")
    else:
        print("fail")


without_and(marks)
with_and(marks)