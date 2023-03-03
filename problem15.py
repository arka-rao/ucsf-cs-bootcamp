def main():
    source = open("rosalind_subs.txt","r")
    lines = source.readlines()

    s = lines[0]
    t = lines[1]

    j = 0
    k = len(t)

    output = []

    print "Starting string: %s" % (s)
    print "Second string: %s" % (t)

    while k <= len(s):
        substring = s[j:k-1]
        substring = substring.strip("\n")
        t = t.strip("\n")
        print "======"
        print "substring # %s: " % (str(j+1)) + substring
        print "t: %s" % (t)
        if str(substring) == str(t):
            print "Found at position %s" % (str(j+1))
            output.append(str(j+1))
        else:
            print "Not found at position %s" % (str(j+1))
        print "======"
        j += 1
        k += 1
    
    answer = ""
    for i in output:
        answer += i
        answer += " "
    
    print answer

main()