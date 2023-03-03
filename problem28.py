def main():

    #This is a function that removes substrings in a given list from a bigger string (variable)
    #Returns the trimmed, exon only DNA strand
    def removeIntrons(main_DNA,intron_DNA):
        for intron in intron_DNA:
            main_DNA = main_DNA.replace(str(intron),"")
        return main_DNA

    #Transcribes a DNA strand into a RNA strand and returns the RNA strand
    def transcribe(exon_DNA):
        exon_RNA = ""
        for base in exon_DNA:
            if base == "T":
                exon_RNA += "U"
            else:
                exon_RNA += base
        return exon_RNA
    
    #Translates any RNA strand into a protein from codons
    def translate(exon_RNA,d):
        start = 0
        end = start + 3
        protein = ""
        codon_count = len(exon_RNA)/3
        counter = 0

        while counter < codon_count:
            codon = exon_RNA[start:end]
            if codon in d and d[codon] != "Stop":
                protein += d[codon]
            counter += 1
            start += 3
            end += 3
        
        return protein


    #RNA Codon dictionary
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

    #Opened a file and read the DNA strings into a list
    f = open("rosalind_splc.txt", "r")

    s1 = ""
    DNA_list = []
    for line in f:
        if line[0] == ">":
            if not len(s1) == 0:
                s1=s1.replace("\n","")
                DNA_list.append(s1)
                s1 = ""
        else:
            s1 += line
    s1 = s1.replace("\n","")
    DNA_list.append(s1)

    #Established the main DNA strand as a string, and put the introns in a list
    seq_num = len(DNA_list)
    main_DNA = ""
    intron_DNA = []
    

    for i in range(seq_num):
        if i == 0:
            main_DNA += DNA_list[i]
        else:
            intron_DNA.append(DNA_list[i])

    #Removed introns from the main DNA string using a function
    exon_DNA = removeIntrons(main_DNA,intron_DNA)

    #Transcribed the exons only into RNA
    exon_RNA = transcribe(exon_DNA)

    #Translated the exons only into a protein
    exon_protein = translate(exon_RNA,d)

    #Printed the final protein 
    print exon_protein
    f.close()


main()