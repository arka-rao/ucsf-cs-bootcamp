def main():

    #Function that establishes the number of codons that can code for each amino acid
    def frequencies():                                         
        frequence = {}                                             
        for key, value in d.items():                                
            if value not in frequence:                                 
                frequence[value] = 0                                
            frequence[value] += 1                                      
        return (frequence)                                         

    #Function that returns the number of possible RNA strings modulo 1000000
    #This number is modified by the fact that there's 3 stop codons too
    #n is equal to 3 to start, then is multiplied by the number of codons coding for each AA
    def possible(sequence):                              
        freq = frequencies()                                      
        n = freq['Stop']                                              
        for acid in sequence:                                        
            n *= freq[acid]                                             
        return (n % 1000000)                                       

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

    f = open('rosalind_mrna.txt', 'r')
    sequence = f.read().strip()                               
   

    #print sequence
    print(possible(sequence))




main()