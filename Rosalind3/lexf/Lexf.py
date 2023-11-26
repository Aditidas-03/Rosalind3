import  itertools

with open("lexf/rosalind_lexf.txt", 'r') as f:
    alphabet = f.readline().split()
    n = int(f.readline().strip())#more eficient this way beacuse dont need to take out space by hand like below
    result = list(itertools.product(alphabet, repeat = n))
    print("\n".join(["".join(x) for x in result]))

'''def lexf(alphabet, n):
    alphabet = sorted(alphabet)  # Sort the alphabet lexicographically
    k_mers =[''.join(item) for item in product(alphabet, repeat=n)]
    return k_mers
   
alphabet = "ABCDEF" 
n = 3  # Replace with your positive integer n 

result = lexf(alphabet, n)
for item in result:
    print(item)'''




