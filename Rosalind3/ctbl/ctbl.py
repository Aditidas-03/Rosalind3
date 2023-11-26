from Bio import Phylo

tree=Phylo.read('ctbl/rosalind_ctbl.txt','newick')
taxa=[]
for i in tree.find_clades():#iterates through clades(nodes)
    if i.name:#if the node has a name it is leaf node(end point not internal)
        taxa.append(i.name)#adds the name to taxa
taxa=sorted(taxa)#sorted lexographically

def process_clade(clade, root):
    for subclade in clade.clades:
        if not subclade.is_terminal():#then calls the function below(not terminal means has descendants)
            subtrees(subclade, root)
            process_clade(subclade, root)

def subtrees(clade, root):
    array=''
    all_nodes = set(root.get_terminals())
    on_nodes = set(clade.get_terminals())
    off_nodes = all_nodes - on_nodes
    on_tree=[]#to store the names of leaf nodes in the clade
    off_tree=[]# not in the clade
    for i in on_nodes:
        on_tree.append(i.name)
    for j in off_nodes:
        off_tree.append(j.name)
    for taxon in taxa:
        if taxon in on_tree:
            array+='1'
        elif taxon in off_tree:
            array+='0'
    print(array)#binary string

root=tree.root
process_clade(root,root)#here first root is the initial clade and the second is root of the entire tree in calls. 




