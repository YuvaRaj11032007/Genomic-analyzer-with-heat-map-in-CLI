# Genomic Sequence Analyzer & Bacterial Promoter Predictor

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Biopython](https://img.shields.io/badge/Biopython-1.83-green)](https://biopython.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-orange)](https://scikit-learn.org/)

A fast, modular Python toolkit for bacterial genomics analysis and machine learning-based promoter prediction.

Built by a 2nd-year Biotechnology student at NIT Andhra Pradesh to bridge classical bioinformatics with modern ML for gene regulation studies.

---

##  Features

- **FASTA Sequence Analysis**
  - Sequence length & GC content calculation
  - 64-codon frequency analysis with heatmap visualization
- **k-mer Frequency Profiling** (k = 3–6)
- **Motif Search & Enrichment** (TATA-box, -10/-35 elements, etc.)
- **Bacterial Promoter Predictor v1** (Machine Learning)
  - Trained Logistic Regression model on E. coli promoters vs random sequences
  - Uses 6-mer frequency features
  - Returns promoter probability + top contributing k-mers

---

##  Installation


git clone https://github.com/YuvaRaj11032007/Genomic-analyzer-with-heat-map-in-CLI.git
cd Genomic-analyzer-with-heat-map-in-CLI

pip install -r requirements.txt

## Usage
Basic Analysis + Codon Heatmap
Bashpython main.py ecoli.fasta
With k-mer & Motif Search
Bashpython main.py ecoli.fasta --kmer 6 --motif TATA
Promoter Prediction (Main Feature)
Bashpython main.py mulatta.fasta --predict-promoter
Example Output:
textLoaded_id FP000014
length of sequence 60
GC content: 55.00%
Motif TAT appears 1 times

--- Promoter Prediction Analysis ---
Probability of being a Promoter: 92.86%
Result: POSITIVE (Likely a Promoter)

Top 5 discriminative k-mers:
- TTGACA : 0.3421
- TATAAT : 0.2187
...

## Technical Details

Promoter Model: Logistic Regression trained on E. coli promoters (RegulonDB) vs random negatives using 6-mer frequency vectors.
Test Accuracy: ~0.85–0.92
Libraries: Biopython, scikit-learn, Matplotlib, Seaborn, pandas


## Future Work

Integration with Google DeepMind’s AlphaGenome for regulatory variant effect prediction on bacterial genomes
Fine-tuning on larger bacterial datasets
Streamlit/Gradio web demo
Contribution to official AlphaGenome research repository


## Visualizations

64-codon frequency heatmap


<img width="1200" height="810" alt="Figure_1" src="https://github.com/user-attachments/assets/1e538d01-23f3-4d9f-9527-4c13fde5a0ec" />


Top discriminative k-mers bar chart

<img width="640" height="480" alt="Figure_2" src="https://github.com/user-attachments/assets/8233b1d8-80ee-43df-9e2b-ed1a6db52848" />




## Dataset

data/promoters.csv contains labeled E. coli promoter sequences (1 = promoter, 0 = non-promoter).

## License

MIT License.

## About Me

Made with passion for computational genomics

Pendyala YuvaRaj | NIT Andhra Pradesh | [GitHub](https://github.com/YuvaRaj11032007) | [LinkedIn](https://www.linkedin.com/in/yuvaraj-pendyala-5625a8363/)
