def main():
    #Please feel free to laugh if it provides comedic relief! I forgot files existed after working for a while on problem 13. 
    #Maybe this long dictionary will come in handy someday.

    d = {}
    d["UUU"] = "F"      
    d["CUU"] = "L"      
    d["AUU"] = "I"  
    d["GUU"] = "V"
    d["UUC"] = "F"      
    d["CUC"] = "L"      
    d["AUC"] = "I"      
    d["GUC"] = "V"
    d["UUA"] = "L"      
    d["CUA"] = "L"      
    d["AUA"] = "I"      
    d["GUA"] = "V" 
    d["UUG"] = "L"      
    d["CUG"] = "L"      
    d["AUG"] = "M"      
    d["GUG"] = "V"
    d["UCU"] = "S"      
    d["CCU"] = "P"      
    d["ACU"] = "T"      
    d["GCU"] = "A"
    d["UCC"] = "S"      
    d["CCC"] = "P"      
    d["ACC"] = "T"      
    d["GCC"] = "A"
    d["UCA"] = "S"      
    d["CCA"] = "P"      
    d["ACA"] = "T"      
    d["GCA"] = "A"
    d["UCG"] = "S"      
    d["CCG"] = "P"      
    d["ACG"] = "T"      
    d["GCG"] = "A"
    d["UAU"] = "Y"      
    d["CAU"] = "H"      
    d["AAU"] = "N"      
    d["GAU"] = "D"
    d["UAC"] = "Y"      
    d["CAC"] = "H"      
    d["AAC"] = "N"      
    d["GAC"] = "D"
    d["UAA"] = "Stop"  
    d["CAA"] = "Q"      
    d["AAA"] = "K"      
    d["GAA"] = "E"
    d["UAG"] = "Stop"   
    d["CAG"] = "Q"      
    d["AAG"] = "K"      
    d["GAG"] = "E"
    d["UGU"] = "C"      
    d["CGU"] = "R"    
    d["AGU"] = "S"      
    d["GGU"] = "G"
    d["UGC"] = "C"      
    d["CGC"] = "R"      
    d["AGC"] = "S"      
    d["GGC"] = "G"
    d["UGA"] = "Stop"   
    d["CGA"] = "R"      
    d["AGA"] = "R"      
    d["GGA"] = "G"
    d["UGG"] = "W"      
    d["CGG"] = "R"     
    d["AGG"] = "R"      
    d["GGG"] = "G"

    #Created a variable to hold the input string taken from the downloaded file, and several variables for a loop later.
    source_file = open("rosalind_ini14.txt", "r")
    RNA_strand = ""
    for line in source_file:
        RNA_strand += line

    start_slice = 0
    end_slice = start_slice + 3
    protein_strand = ""
    codon_count = len(RNA_strand)/3
    counter = 0

    #This loop breaks up the RNA sequence into sets of 3 bp codons and references them against the library to build the protein strand.
    while counter < codon_count:
        codon = RNA_strand[start_slice:end_slice]
        if codon in d and d[codon] != "Stop":
            protein_strand += d[codon]
        counter += 1
        start_slice += 3
        end_slice += 3

    #print RNA_strand
    print protein_strand
    source_file.close()


main()