
from itertools import permutations
import itertools

n = 6 #change input according to question <=7
seq = list(range(1, n+1))

perm = list(itertools.permutations(seq))#doing permutations and keeping them in a list
total_perm= len(perm)
print(total_perm)#printing the total no

for p in perm:
    print(*p)#iterating and printing them in a new line
    

