from Bio import SeqIO
with open ("kmp/rosalind_kmp.txt",'r') as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
       s = seq_record.seq 
       


    n = len(s)
    P = [0] * n#creating an array p of length n 
    j = 0#to keep track of the length of the proper prefix that is also a suffix.

    for i in range(1, n):
        while j > 0 and s[j] != s[i]:
            j = P[j - 1]

        if s[j] == s[i]:
            j += 1

        P[i] = j



with open('kmp/outputkmp.txt', "w") as output:
    output.write(" ".join(map(str, P)))#answers from the terminal was not accepted beacuse it cant print so manyy characters perfectly
