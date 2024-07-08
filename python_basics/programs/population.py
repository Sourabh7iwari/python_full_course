"""10th year of population is 10000, id population is increasing 10per a year provide population for last 10 years"""
pop = 10000
for i in range(10,0,-1):
    print(i,pop)
    pop /= 1.1 