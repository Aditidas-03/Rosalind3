from Bio import SeqIO
seq_name,seq_string=[],[]
for seq_record in SeqIO.parse('revp/rosalind_revp.txt','fasta'):
    seq_name.append(str(seq_record.name))
    seq_string.append(str(seq_record.seq))#processing fasta files

s = seq_string[0]#getting the seq string
def reverse_complement(s):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(s))#doing the reverse complement

def palindrome(s):
    for i in range(len(s)):
        for j in range(4,13):
            if s[i:i+j] == reverse_complement(s[i:i+j]) and (i+j <= len(s)):#checking if its a palindrome and within the length of s
                print(i+1, j)

palindrome(s)
