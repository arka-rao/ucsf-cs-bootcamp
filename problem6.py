def main():
    #Establish an empty dictionary variable and a variable to hold the sample input string
    d = {}

    s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

    #Build a forloop with if/else statements to print the words + number of occurences

    for i in s.split(" "):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
    
    #Print the dictionary in the requested output format
    for key, value in d.items():
        print key + " " + str(value)
  
    
 

        


main()