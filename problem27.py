def main():

    #Reverse complement function from problem24
    def reverse_comp(DNA):
        s = ""
        r = {"A":"T", "T":"A", "G":"C", "C":"G"}
        reverse = reversed(DNA)
        for base in reverse:
            s += r[base]
        return s


    def reverse_pal(DNA):
        l1 = []
        length = len(DNA)
        for i in range(length): #Looking at each slice and reversing complementing it
            for j in range(4, 13): #Length limitations, added 1 to the end for accuracy
                if i + j > length: #Need to make sure that we're not returning several strings of different lengths from the same start
                    continue
                s1 = DNA[i:i+j] #slices the string from pos 0 of DNA up to the min/max length specified
                s2 = reverse_comp(s1) #takes reverse comp of that
                if s1 == s2: #finds the true reverse palindromes
                    l1.append((i + 1, j)) #position, length
        return l1
        
    #Opened a file, read in the DNA string
    f = open("rosalind_revp.txt", "r")

    DNA = ""
        
    for line in f:
        if line[0] != ">":
            DNA += line
            DNA = DNA.replace("\n","")

    print DNA
    #Sent the DNA string to a function to get a list of the positions and lengths in pairs
    pair_list = reverse_pal(DNA)

    for pair in pair_list:
        print str(pair[0]) + " " + str(pair[1])

main()

# def reverse_comp(s):
    #     s = ""
    #     r = {"A":"T", "T":"A", "G":"C", "C":"G"}
    #     reverse = reversed(DNA)
    #     for base in reverse:
    #         s += r[base]
    #     return s

    # def reverse_pal(s):
    #     l1 = []
    #     l = len(s)
    #     for i in range(l):
    #         for j in range(l):
    #             if i + j > l:
    #                 continue
    #             s1 = s[i:i+j]
    #             print s1
    #             s2 = reverse_comp(s1)
    #             print s2
    #             if s1 == s2:
    #                 l1.append((i + 1, j))
    #     return l1
    
    # f = open("rosalind_ini27.txt", "r")

    # DNA = ""
    
    # for line in f:
    #     if line[0] != ">":
    #         DNA += line
    #         DNA = DNA.replace("\n","")
    
    # l1 = reverse_pal(DNA)

    # print l1