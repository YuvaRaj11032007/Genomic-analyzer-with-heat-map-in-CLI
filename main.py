import argparse
from Bio import SeqIO
import stats_engine as sec
from visualizer import heatmap
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
        print(result)
        heatmap(codon_freq)
if __name__ == "__main__":
    main()