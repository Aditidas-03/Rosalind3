with open('eubt/rosalind_eubt.txt', 'r') as file:
    taxa = file.read().split()
    trees = [['(', '(', taxa[1], ',', taxa[2], ')', ')', taxa[0], ';']]

newly_added = taxa[3:]

def unrooted_bin_tree(list, n_taxa):
    n_tree = []
    for i in range(1,len(list)-2):#starting from index 1 and ending at the second-to-last index.
        j = -1
        if not list[i] in '(),;':#checks if the current element at index i is not one of '(),;'. If true, it sets j to the current index i.
            j = i
        if list[i]=='(':
            counter=1#if yes a counter m to  iterates from the next index (i + 1) to find the  closing parenthesis.
            for j in range(i+1, len(list)):
                if list[j]=='(':
                    counter +=1
                elif list[j]==')':
                    counter -=1
                if counter == 0:
                    break# m becomes 0, indicating the closing parenthesis.
        if j!=-1:#then  position to insert the new taxa
            t =  list[:i] + ['('] + list[i:j+1] + [','] + [n_taxa] + [')'] + list[j+1:]
            n_tree.append(t)
    return n_tree



for n_taxa in newly_added:
    t = []
    for tree in trees:

        t2 = unrooted_bin_tree(tree, n_taxa)
        t = t + t2
    trees = t[:]

for tree in trees:
    print (''.join(tree))