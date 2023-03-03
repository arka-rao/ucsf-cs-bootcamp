def main():
    #Establish variables to represent the number of months and the number of pairs yielded from a viable pair
    n = 28
    k = 4

    #Develop a recursive function that models the Fibonacci sequence, but has a multiplier for the pairs
    def Rabbit(n,k):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return Rabbit(n-1,k) + (Rabbit(n-2,k))*k
    
    #Print the desired output
    print Rabbit(n,k)
    

    



main()