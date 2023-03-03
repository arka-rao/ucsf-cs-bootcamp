def main():
    import itertools

    #Open text file, read in the symbols and make them into a string

    f = open("rosalind_lexf.txt","r")

    s1 = f.readlines()[0]
    s1 = s1.strip()
    s1 = s1.replace(" ","")
    
    #Hard code the number n and make a list of the symbols
    n = 4
    l1 = []
    for letter in s1:
        l1.append(letter)

    #Using the itertools module, use the product function to make an iterable object
    #The iterable object makes permutations of n symbols and I make(?) that into a list later
    #That list later also stores the position as an incremented number
    permutations = itertools.product(l1, repeat = n)
    l2 = []

    
    #i is position, J is an n-ple permutation of n letters
    for i,j in enumerate(list(permutations)):
        p = ""
        for symbol in j:
            p += str(symbol)
        l2.append(p)

    #print the desired output
    for string in l2:
        print string

    f.close()
main()