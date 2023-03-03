def main():
    #Imported helpful modules
    import math
    from itertools import permutations

    n = 7
    total = math.factorial(n)
    l1 = []
    l2 = []

    #Created a list to store the possible non-zero integer values
    for i in range(1,n+1):
        l1.append(i)

    #Created a list of the possible permutations, which were performed on a list
    l2 = permutations(l1)

    #Print output
    
    print total
    for permutation in l2:
        s = ""
        for i in range(n):
            s += str(permutation[i])
            s += " "
        print s




main()