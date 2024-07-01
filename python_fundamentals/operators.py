"""Arithmetic operation in python are ( + , - , // , / , % , ** )"""
print(2+3.0)
#output -> 5.0

print(3-1)
#output -> 2

""" the operator '%' return the remainder of division"""
print(10%3,10%7,20%2)
#output -> 1 0 0

print(24//3, 24//4)
#output(the only integer part of divisor if not perfect divisor ) -> 8 6 

print(100/3,24//4)
#output(the whole divisor) -> 33.3333... 6

print(4**2)
#output -> 16

"""Bitwise operation in python are  ( & , | , < < , > > , ~ , ^ )"""
print(2 & 3, 2 & 4)
#output -> 2

print(2 | 3, 2 | 4)
#output -> 3

print(2<<1, 6<<2)
#output ->4 24 (it shift the binary bits of number into right side by the number of given after the operator) 

print(2>>1,6>>3)
#output -> 1 0 (it shift the binary bits of number into left side by the number of given after the operator)

print(~3)
#output the 2's complement of number -> -4

print(5^2, 7^4)
#output 