def main():
    
    #This function returns the reverse complement of the given DNA string
    def reverse_comp(DNA):
        s = ""
        r = {"A":"T", "T":"A", "G":"C", "C":"G"}
        reverse = reversed(DNA)
        for base in reverse:
            s += r[base]
        return s
    
    #This funcion translates the codon into the amino acid using the DNA dict
    def translate(codon):
        amino = ""
        if codon in dna_dict.keys():
            amino += dna_dict[codon]
        return amino

    #This function finds the locations of start codons in the given DNA strings
    #It then translates the ORFs from each start position
    def possible(s):
        l1 = [] #Will store the possible protein strings from the ORFs
        positions = [] #Will store the positions of start codons

        length = len(s)
        for i in range(length):
            amino = translate(s[i:i+3])
            if amino == 'M':
                positions.append(i) #Here's where it gets start positions
        
        for i in positions: #Here's where I can build protein strings and append to a list from each ORF as limited by STOP codons
            protein = ''
            stop = False
            for j in range(i, length, 3): #The false variable and the 3 increment on range helped
                amino = translate(s[j:j+3])
                if amino == 'Stop':
                    stop = True
                    break
                protein += amino
            if stop == True:
                l1.append(protein)

        return l1

    #First, a dictionary with DNA codons or base triplets for translational purposes
    dna_dict = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

    #Open the input file and read in the DNA string and also reverse complement it
    f = open("rosalind_orf.txt","r")
    
    DNA = ""
    
    for line in f:
        if line[0] != ">":
            DNA += line
            DNA = DNA.replace("\n","")

    reverse = reverse_comp(DNA)

    #Send each string through a function that returns possible proteins as a list for each
    a = possible(DNA)
    b = possible(reverse)

    #Print the possible protein strings, not optimized for repeats or any order
    for protein in a:
        print protein
    
    for protein in b:
        print protein
    
    #close files
    f.close()

main()

# d = {}
    # d["UUU"] = "F"      
    # d["CUU"] = "L"      
    # d["AUU"] = "I"  
    # d["GUU"] = "V"
    # d["UUC"] = "F"      
    # d["CUC"] = "L"      
    # d["AUC"] = "I"      
    # d["GUC"] = "V"
    # d["UUA"] = "L"      
    # d["CUA"] = "L"      
    # d["AUA"] = "I"      
    # d["GUA"] = "V" 
    # d["UUG"] = "L"      
    # d["CUG"] = "L"      
    # d["AUG"] = "M"      
    # d["GUG"] = "V"
    # d["UCU"] = "S"      
    # d["CCU"] = "P"      
    # d["ACU"] = "T"      
    # d["GCU"] = "A"
    # d["UCC"] = "S"      
    # d["CCC"] = "P"      
    # d["ACC"] = "T"      
    # d["GCC"] = "A"
    # d["UCA"] = "S"      
    # d["CCA"] = "P"      
    # d["ACA"] = "T"      
    # d["GCA"] = "A"
    # d["UCG"] = "S"      
    # d["CCG"] = "P"      
    # d["ACG"] = "T"      
    # d["GCG"] = "A"
    # d["UAU"] = "Y"      
    # d["CAU"] = "H"      
    # d["AAU"] = "N"      
    # d["GAU"] = "D"
    # d["UAC"] = "Y"      
    # d["CAC"] = "H"      
    # d["AAC"] = "N"      
    # d["GAC"] = "D"
    # d["UAA"] = "Stop"  
    # d["CAA"] = "Q"      
    # d["AAA"] = "K"      
    # d["GAA"] = "E"
    # d["UAG"] = "Stop"   
    # d["CAG"] = "Q"      
    # d["AAG"] = "K"      
    # d["GAG"] = "E"
    # d["UGU"] = "C"      
    # d["CGU"] = "R"    
    # d["AGU"] = "S"      
    # d["GGU"] = "G"
    # d["UGC"] = "C"      
    # d["CGC"] = "R"      
    # d["AGC"] = "S"      
    # d["GGC"] = "G"
    # d["UGA"] = "Stop"   
    # d["CGA"] = "R"      
    # d["AGA"] = "R"      
    # d["GGA"] = "G"
    # d["UGG"] = "W"      
    # d["CGG"] = "R"     
    # d["AGG"] = "R"      
    # d["GGG"] = "G"

 # def transcription(DNA_slice):
    #     RNA_slice = ""
    #     for base in DNA_slice:
    #         if base == "T":
    #             RNA_slice += "U"
    #         else:
    #             RNA_slice += base
    #     return RNA_slice
    
    # def translation(RNA_slice):
    #     start_slice = 0
    #     end_slice = start_slice + 3
    #     protein = ""
    #     codon_count = len(RNA_slice)/3
    #     c2 = 0
    #     while c2 < codon_count:
    #         codon = RNA_slice[start_slice:end_slice]
    #         if codon in d and d[codon] != "Stop":
    #             protein += d[codon]
    #         c2 += 1
    #         start_slice += 3
    #         end_slice += 3
    #     return protein

     # # print "======================="
    # # print "Full DNA: " + DNA
    # # print "======================="
    # # print ""

    # start_list = []
    # c1 = 0
    # while c1 < (len(DNA)-2):
    #     codon = DNA[c1:c1+3]
    #     if codon == "ATG":
    #         start_list.append(c1)
    #     c1 += 1
    # #print start_list

    # DNA_slice = ""
    # length = len(start_list)

    # for i in range(length):
    #     if i < (length-1):
    #         DNA_slice = DNA[(start_list[i]):(start_list[i+1])]
    #         RNA_slice = transcription(DNA_slice)
    #         protein = translation(RNA_slice)
    #         # print "======================="
    #         # print "DNA slice: " + DNA_slice
    #         # print "RNA slice: " + RNA_slice
    #         # print "Protein: " + protein
    #         # print "======================="
    #         # print ""
    #     elif i == (length-1):
    #         DNA_slice = DNA[(start_list[i]):]
    #         RNA_slice = transcription(DNA_slice)
    #         protein = translation(RNA_slice)
    #         # print "======================="
    #         # print "DNA slice: " + DNA_slice
    #         # print "RNA slice: " + RNA_slice
    #         # print "Protein: " + protein
    #         # print "======================="
    #         # print ""
