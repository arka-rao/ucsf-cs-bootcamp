def main():
    #Establish two file variables 
    source_file = open("rosalind_ini5.txt", "r")
    output_file5 = open("output_file5.txt", "w")

    #Make an empty string and add the source_file stuff to it. Might be inefficient.
    s1 = ""

    for line in source_file:
        s1 += line

    #Split lines into a list and establish a counter variable
    s2 = s1.splitlines()

    counter = 1

    #Build a forloop to write the output text file
    for i in s2:
        if counter <= len(s2):
            sentence = s2[counter]
            output_file5.write(sentence + '\n')
            counter += 2
        else:
            break
    
    #Close all files
    source_file.close()
    output_file5.close()


   
   

  
        







main()