'''def fac(n)->int:
    if n==1:
        return 1
    else:
        return n*fac(n-1)
'''    
nth  = int(input("enter nth term"))
fact=1
for i in range(1,nth+1):
    fact =fact * i
    sum = sum + (i/fact)

print(sum)