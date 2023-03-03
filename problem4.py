def main():
    #Establish the range over which I'm looking to sum odd integers
    a = 4312
    b = 9074

    #Establish the sum variable to which I'm going to add up the odd integers between a/b
    sum = 0

    #Build a loop that adds the odd numbers ONLY to sum
    for num in range(a,b):
        if num % 2 != 0:
            sum += num
    
    #Check output with a print function
    print sum
        

main()