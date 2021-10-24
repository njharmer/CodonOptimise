# CodonOptimise
A bespoke codon optimisation script written in Python 3

The zip file "CodonOptimise" contains a Python 3 script and a folder of associated modules. The software was written in Spyder v.4 under Anaconda.

The aim of the script is to take a protein sequences and optimise it for expression in Escherichia coli. Codon usage was assigned following the E. coli K12 strain codon usage at https://www.kazusa.or.jp/codon/. The script aims to randomly assign codons in the same frequency as used by E. coli. The first 30 amino acids are selected to avoid rare codons, and to bias towards codons that are richer in A and T to reduce the risk of the Shine-Dalgarno sequence being blocked by RNA secondary structure (https://doi.org/10.1016/j.molcel.2018.05.008). The script will not include sites for any of the following common restriction enzymes used to clone genes for expression: BamHI, EcoRI, HindIII, KpnI, NcoI, NdeI, NotI, PstI, SpeI, XbaI, XhoI, XmaI. Other restriction sites could readily be added so long as they are eight or fewer bases in length and do not include wild-cards. The code performs a reality check of the final sequence to ensure that none have slipped through.

The sequence input recognised is a FASTA sequence (without a header line), without any carriage returns, in either upper or lower case. The twenty canonical amino acids and the stop codon * are recognised. 

Any ideas for improvement are welcome!
