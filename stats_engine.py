def Gc_content(rand,count):
    G=rand.count("G")
    C=rand.count("C")
    percent=(((G+C)/count))*100
    return percent
def codons(read):
    read= read[:len(read)-len(read)%3]
    codon= {
    'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0, 'TCG': 0,
    'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0, 'TGT': 0, 'TGC': 0, 'TGA': 0, 'TGG': 0,
    'CTT': 0, 'CTC': 0, 'CTA': 0, 'CTG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0,
    'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0, 'CGG': 0,
    'ATT': 0, 'ATC': 0, 'ATA': 0, 'ATG': 0, 'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0,
    'AAT': 0, 'AAC': 0, 'AAA': 0, 'AAG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0,
    'GTT': 0, 'GTC': 0, 'GTA': 0, 'GTG': 0, 'GCT': 0, 'GCC': 0, 'GCA': 0, 'GCG': 0,
    'GAT': 0, 'GAC': 0, 'GAA': 0, 'GAG': 0, 'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0
    }
    for i in range(0,len(read),3):
        triplet=str(read[i:i+3])
        if triplet in codon:
            codon[triplet] +=1
    return codon
def kmer(read,klen):
    k_mer_counts={}
    for i in range(0,len(read)-klen+1):
        mer=str(read[i:i+klen])
        if mer in k_mer_counts:
            k_mer_counts[mer]+=1
        else:
            k_mer_counts[mer]=1
    return k_mer_counts
def motif(read,length,mot):
    n=len(mot)
    count=0
    for i in range(0,length-n):
        k=str(read[i:i+n])
        if k ==mot :
            count+=1
    return count
            

        

        


 

        