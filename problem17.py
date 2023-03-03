def main():
    #Establish variables to handle the problem's input
    n = 96 #months total
    m = 19 #lifespan in months

    #Build a list variable and fill it based on the modifications to the Fibonacci sequence model
    f = [0]*(n+1)

    f[0] = 1

    for i in range (2, n+1):
        f[i] = f[i-2] + f[i-1] - f[i-m-1]
    
    print f[n] + f[n-1]


main()


