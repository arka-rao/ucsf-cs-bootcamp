def main():
    import requests

    f = open("rosalind_mprt.txt", "r")
    ID = f.readlines()

    d = {}

    for pepID in ID:
        pepID = pepID.strip()
        pepFASTA = requests.get("https://www.uniprot.org/uniprot/" + pepID + ".fasta").text
        lines = pepFASTA.splitlines()
        body = ""
        for line in lines:
            if line[0] == ">":
                header = line[1:]
            else:
                body += line
        local = []
        for i in range(len(body)-4):
            kmer = body[i:i+4]
            if kmer[0] == "N" and kmer[1] != "P" and kmer[3] != "P" and (kmer[2] == "S" or kmer[2] == "T"):
                local.append(str(i+1))
        if local != []:
            d[pepID] = local

    for key, value in d.items():
        s = ""
        for i in value:
            s += i 
            s += " "
        print key
        print s
   
    
    f.close()
    

main()

# import urllib

    # f1 = open("rosalind_mprt.txt", "r")
    # #output = open("problem22.txt", "w")

    
    # for line in f1:
    #     url = "https://www.uniprot.org/uniprot/" + line.strip() + ".fasta"
    #     f2 = urllib.urlopen(url)
    #     f3 = f2.readlines()
    #     f4 = ""
    #     for line2 in f3:
    #         if line2[0] == ">":
    #             pass
    #         else:
    #             line2.replace("\n","")
    #             f4 += line2
    #     s = ""

    #     #below is the problematic loop
    #     for i in range(0,(len(f4))-4):
    #         if f4[i] == 'N' and f4[i+1] != 'P' and (f4[i+2] == "S" or f4[i+2] == "T") and f4[i+3] != 'P':
    #             s += str(i) + ' '
                
        
    #     if s != "":
    #         print line.strip()
    #         print s.strip()


            


    # f1.close()
    # #output.close()