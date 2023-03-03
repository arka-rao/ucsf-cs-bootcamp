def main():
    #open the source file and convert it into a list, somewhat inefficiently? had to trim the first item too using pop
    source_file = open("rosalind_ini11.txt", "r")
    
    s1 = ""

    for line in source_file:
        s1 += line
    
    l1 = s1.split(">")
    l1.pop(0)
    #print "l1: " + str(l1) --> used for testing

    #building a loop to sum C, G, and total # of DNA base pairs.
    #I added some print functions to keep a track of the items it was checking and to verify sums
    #Had to convert the GC sum variable to float, otherwise I was getting 0 errors for division
    #In the loop, I reset the variables to 0 just so I can get the right answers per DNA strand
    C = 0
    G = 0
    DNAchar = 0

    for i in l1:
        s2 = ""
        s2 += str(i[:])
        print "==========================="
        print s2
        for char in s2:
            if char == "A" or char == "T":
                DNAchar += 1
            elif char == "C":
                C += 1
                DNAchar += 1
            elif char == "G":
                G += 1
                DNAchar += 1
            else:
                continue
        print "C: " + str(C)
        print "G: " + str(G)
        print "DNAchar: " + str(DNAchar)
        GC = float(G + C)
        content = (GC/DNAchar) * 100
        print "GC total: " + str(GC)
        print "GC content: " + str(content) + "%"
        print "==========================="
        C = 0
        G = 0
        DNAchar = 0


    source_file.close()


        
        
   
        
    
   
            




main()