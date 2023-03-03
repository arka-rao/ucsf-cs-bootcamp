def main():
    #I started by importing modules necessary for my approach to this question. There are definitely easier ways to do this.
    import math
    from itertools import combinations

    k = 21
    m = 21
    n = 21

    total = k + m + n
    pair = 2

    #After establishing k,m, and n as well as the total and pair variables that are useful for combos, I built a list of relevant genotypes
    #These genotypes are modified by the value of k,m, and n, which represent the number of indiv. w/ each genotype
    combo = (math.factorial(total))/((math.factorial(total - pair))*(math.factorial(pair)))
    offspring = combo * 4

    l1 = []

    counter = 0
    while counter < (total-(m+n)):
        l1.append("XX")
        counter += 1
        

    counter = 0
    while counter < (total-(k+m)):
        l1.append("Xx")
        counter += 1
    
    counter = 0
    while counter < (total-(k+n)):
        l1.append("xx")
        counter += 1

    print l1
    
    #I used a function from the itertools module to create an object list of possible tuples
    comb = combinations(l1,2)

    #I then created a forloop to keep a track of possible combinations that would yield offspring with the recessive phenotype
    recessive = 0

    for i in list(comb):
        if i == ("xx", "xx"):
            recessive += 4
        elif i == ("Xx", "xx"):
            recessive += 2
        elif i == ("Xx", "Xx"):
            recessive += 1
        else:
            continue
    
    #From there it was just simple subtraction and some printing checks to verify my answer was correct.
    print "recessive: " + str(recessive)

    dom = offspring - recessive

    print "dominant: " + str(dom)

    prob = float(dom)/offspring

    print "probability: " + str(prob)

main()