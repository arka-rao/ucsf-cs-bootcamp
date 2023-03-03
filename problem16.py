def main():
    #Imported a library I found online that makes matrices look better in terminal
    #Also created a file import variable
    
    source = open("rosalind_cons.txt", "r")

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

    #Built a matrix-ish list
    matrix = []

    for i in l1:
        matrix.append([j for j in i])

    Alist,Clist,Glist,Tlist = [],[],[],[]
    
    pos = 0
    length = len(matrix[0])
    
    #Built a loop to get the number of each base at each position in each DNA strand
    while pos < length:
        A,C,G,T = 0,0,0,0
        for item in matrix:
            base = item[pos]
            if base == "A":
                A += 1
            elif base == "C":
                C += 1
            elif base == "G":
                G += 1
            elif base == "T":
                T += 1
            else:
                pass
        Alist.append(A)
        Clist.append(C)
        Glist.append(G)
        Tlist.append(T)
        pos += 1

    #con_list = []
    consensus = ""

    # con_list.append(Alist)
    # con_list.append(Clist)
    # con_list.append(Glist)
    # con_list.append(Tlist)

    # print Alist
    # print Clist
    # print Glist
    # print Tlist

    #print con_list

    for i in range(len(Alist)):
        a_max = Alist[i]
        c_max = Clist[i]
        g_max = Glist[i]
        t_max = Tlist[i]
        con_max = max(a_max,c_max,g_max,t_max)
        if con_max == a_max:
            consensus += "A"
        elif con_max == c_max:
            consensus += "C"
        elif con_max == g_max:
            consensus += "G"
        elif con_max == t_max:
            consensus += "T"
    
    print consensus

    #Built a set of loops for the desired print output
    a_str = ""
    for number in Alist:
        a_str += str(number)
        a_str += " "
    
    c_str = ""
    for number in Clist:
        c_str += str(number)
        c_str += " "
    
    g_str = ""
    for number in Glist:
        g_str += str(number)
        g_str += " "
    
    t_str = ""
    for number in Tlist:
        t_str += str(number)
        t_str += " "

    print "A: " + a_str
    print "C: " + c_str
    print "G: " + g_str
    print "T: " + t_str

    source.close()
main()





# while counter < len(Alist):
#         for item in con_list:
#             if item[counter] == Alist[counter]:
#                 print "==="
#                 print item[counter]
#                 print Alist[counter]
#                 consensus += "A"
#                 counter += 1
#                 print counter
#                 print consensus
#                 print "==="
#             elif item[counter] == Clist[counter]:
#                 print "==="
#                 print item[counter]
#                 print Clist[counter]
#                 consensus += "C"
#                 counter += 1
#                 print counter
#                 print consensus
#                 print "==="
#             elif item[counter] == Glist[counter]:
#                 print "==="
#                 print item[counter]
#                 print Glist[counter]
#                 consensus += "G"
#                 counter += 1
#                 print counter
#                 print consensus
#                 print "==="
#             elif item[counter] == Tlist[counter]:
#                 print "==="
#                 print item[counter]
#                 print Tlist[counter]
#                 consensus += "T"
#                 counter += 1
#                 print counter
#                 print consensus
#                 print "==="