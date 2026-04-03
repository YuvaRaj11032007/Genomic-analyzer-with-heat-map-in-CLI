import argparse
from Bio import SeqIO
import stats_engine as sec 
from visualizer import heatmap, kmertable
import promoter_predictor as pp
def load_sequence(file_path):
    try:
        for record in SeqIO.parse(file_path,"fasta"):
            print("Loaded_id",record.id)
            length=len(record.seq)
            print("length of sequence",length)
            return record.seq,length
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None, None
def main():
    parser = argparse.ArgumentParser(description="Genomic Sequence Analyzer Tool")
    parser.add_argument("input", help="Path to the input FASTA file (e.g., ecoli.fasta)")
    args = parser.parse_args()
    dna, length = load_sequence(args.input)
    if dna:
        codon_freq=sec.codons(dna)
        result=sec.Gc_content(dna,length)
        klen=int(input("enter the K-mer length: "))
        motif_seq=input("enter the motif sequence:")
        motif_freq=sec.motif(dna,length,motif_seq)
        kmer_freq=sec.kmer(dna,klen)
        print(result)
        print("the desired",motif_seq,"appears",motif_freq,"times")
        print("\n--- Promoter Prediction Analysis ---")
        probability, top_motifs = pp.predict_promoter(str(dna))
        print(f"Probability of being a Promoter: {probability:.2%}")
        if probability > 0.5:
            print("Result: POSITIVE (Likely a Promoter)")
        else:
            print("Result: NEGATIVE (Likely non-promoter)")
        print("\nTop Contributing K-mers:")
        for kmer, weight in top_motifs:
            print(f"  - {kmer}: {weight}")
        heatmap(codon_freq)
        kmertable(kmer_freq)
if __name__ == "__main__":
    main()