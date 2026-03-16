import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
def heatmap(codon):
    values=list(codon.values())
    matrix=np.array(values).reshape(8,8)
    labels=np.array(list(codon.keys())).reshape(8,8)
    plt.figure(figsize=(12, 10))
    sns.heatmap(matrix, 
            annot=labels,      
            fmt="",            
            cmap="YlGnBu",     
            linewidths=.5,     
            cbar_kws={'label': 'Frequency Count'})
    plt.title("64 Codon Frequency Heatmap", fontsize=16)
    plt.show()
    plt.savefig("heat map")