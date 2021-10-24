# Script to turn a protein sequence into DNA, with defined restriction
# sequences removed.

# Import generic modules
import random

# Import specific modules
from modules.Ala import Ala
from modules.Cys import Cys
from modules.Asp import Asp
from modules.Glu import Glu
from modules.Phe import Phe
from modules.Gly import Gly
from modules.His import His
from modules.Ile import Ile
from modules.Lys import Lys
from modules.Leu import Leu
from modules.Asn import Asn
from modules.Pro import Pro
from modules.Gln import Gln
from modules.Arg import Arg
from modules.Ser import Ser
from modules.Thr import Thr
from modules.Val import Val
from modules.Tyr import Tyr
from modules.stop import stop
from modules.Restest import Restest

# Allowed characters and restriction sites
allow = 'a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s'\
,'t','v','w','y','A','C','D','E','F','G','H','I','K','L','M','N','P','Q',\
'R','S','T','V','W','Y','*'
res=('GGATCC','GAATTC','AAGCTT','GGTACC','CCATGG','CATATG','GCGGCCGC',\
     'CTGCAG','ACTAGT','TCTAGA','CTCGAG','CCCGGG')


# Ask for the FASTA sequence
seq = input('Enter the desired sequence in FASTA format, including a stop \
codon if desired. \n')

seqlen=len(seq)
#print(allow)
#print(seqlen)

# Set up a loop to codon optimise until there is a good solution
for j in range(3):

    opt = []
    i = -1

    # Do the codon optimisation
    while i < len(seq)-1:
        i = i + 1

        # Test for new restriction sites and remove the last two codons
        # if present
        # Join up the codons into a single sequence
        optimised = ''.join(opt)

        # Test for restriction sites
        for r in res:
            f = optimised.find(r)
            if f > 1:
                print('restriction site '+ r + ' found at position '+ str(f))
                del opt[-1]
                del opt[-1]
                del opt[-1]
                i = i - 3
                break

        # Set a random number to choose the codon        
        a = random.randint(1, 100)
        print (i,a)

        # Test that the character is allowed
        t = seq[i] in allow
        if t == False:
            print('Character ' + seq[i] + 'at position ' + str(i) + \
                  ' is illegal')
            break; break

        # Add the codon
        elif seq[i] == "a" or seq[i] == "A":
            Ala(i,a,opt)
        elif seq[i] == "c" or seq[i] == "C":
            Cys(i,a,opt)
        elif seq[i] == "d" or seq[i] == "D":
            Asp(i,a,opt)
        elif seq[i] == "e" or seq[i] == "E":
            Glu(i,a,opt)
        elif seq[i] == "f" or seq[i] == "F":
            Phe(i,a,opt)
        elif seq[i] == "g" or seq[i] == "G":
            Gly(i,a,opt)
        elif seq[i] == "h" or seq[i] == "H":
            His(i,a,opt)
        elif seq[i] == "i" or seq[i] == "I":
            Ile(i,a,opt)
        elif seq[i] == "k" or seq[i] == "K":
            Lys(i,a,opt)
        elif seq[i] == "l" or seq[i] == "L":
            Leu(i,a,opt)
        elif seq[i] == "m" or seq[i] == "M":
            opt.append('ATG')
        elif seq[i] == "n" or seq[i] == "N":
            Asn(i,a,opt)
        elif seq[i] == "p" or seq[i] == "P":
            Pro(i,a,opt)
        elif seq[i] == "q" or seq[i] == "Q":
            Gln(i,a,opt)
        elif seq[i] == "r" or seq[i] == "R":
            Arg(i,a,opt)
        elif seq[i] == "s" or seq[i] == "S":
            Ser(i,a,opt)
        elif seq[i] == "t" or seq[i] == "T":
            Thr(i,a,opt)
        elif seq[i] == "v" or seq[i] == "V":
            Val(i,a,opt)
        elif seq[i] == "w" or seq[i] == "W":
            opt.append('TGG')
        elif seq[i] == "y" or seq[i] == "Y":
            Tyr(i,a,opt)
        elif seq[i] == "*":
            stop(i,a,opt)

    # Join up the codons into a single sequence        
    optimised = ''.join(opt)
    print(optimised)
        
    # Test for restriction sites
    rest=0
    for r in res:
        f = optimised.find(r)
        if f > 1:
            print('restriction site '+ r + ' found at position '+ str(f))
            rest=1
    if rest == 0:
        print('Good sequence')
        break
                 


    
            

       
