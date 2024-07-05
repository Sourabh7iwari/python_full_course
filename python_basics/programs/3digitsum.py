import time
number = int(input("enter the number"))
n= str(number)

def digitsum1(number):
    start_time = time.time()
    son=0
    while number>0:
        son +=number%10
        number //=10
    end_time = time.time()
    return son, end_time-start_time

print(f"solution by first method: {digitsum1(number)[0]}, time taken {digitsum1(number)[1]}")

def digitsum2(number):
    start_time = time.time()
    numer = list(n.strip(""))
    number = sum([int(i) for i in n ])
    end_time = time.time()
    return number, end_time-start_time
print(f"solution by first method: {digitsum2(number)[0]}, time taken {digitsum2(number)[1]}")