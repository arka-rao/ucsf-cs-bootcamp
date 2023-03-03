def main():
    #Set up variables to correctly get a list of type int
    f = open("rosalind_iev.txt", "r")
    s = f.readline()
    l1 = s.split()
    l2 = []

    for i in range(0, len(l1)):
        l2.append(int(l1[i]))
    
    #Sum that yields an average based on the genotypes/pairs given
    sum = (l2[0]*1 + l2[1]*1 + l2[2]*1 + l2[3]*0.75 + l2[4]*0.5 + l2[5]*0)*2

    print str(sum)

    f.close()

main()