def main():

    def find(l1): 
        n = len(l1) 
        s = l1[0] 
        l = len(s) 
    
        substring = "" 
    
        for i in range(l) : 
            for j in range(i + 1,l + 1):  
                stem = s[i:j] 
                k = 1
                for k in range(1, n):  
                    if stem not in l1[k]: 
                        break
                if (k + 1 == n and len(substring) < len(stem)): 
                    substring = stem 
    
        return substring 
        
    source = open("rosalind_lcsm.txt", "r")

    s1 = ""
    l1 = []
    for line in source:
        if line[0] == ">":
            if not len(s1) == 0:
                s1=s1.replace("\n","")
                l1.append(s1)
                s1 = ""
        else:
            s1 += line
    s1 = s1.replace("\n","")
    l1.append(s1)

    data = find(l1) 
    print(data) 
    source.close()

main()