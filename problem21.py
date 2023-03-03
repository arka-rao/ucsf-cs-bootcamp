def main():
    import math

    def bino_prob(k,n):
        #This function uses the probability of AaBb (1/4)
        #to build a list of the binomial probability per gen
        #and then sums it up as per independence prob rule
        p = 0.25

        l1 = []
        end = 2**k #this is a limiter? i took from the problem

        for i in range(n,(end+1)):
            l1.append(combo(end,i)*(p**i)*((1-p)**(end-i)))
            #l1 has the probabilities per generation
        return sum(l1)
    
    def combo(n,i):
        #to save myself this typing, I just made it a function
        n_combo = math.factorial(n)
        i_combo = math.factorial(i)
        ni_combo = math.factorial(n-i)
        return n_combo/((ni_combo)*i_combo)

    #Establish the variables for generations (k) and AaBb (n)
    k = 7
    n = 34
    print bino_prob(k,n)

main()