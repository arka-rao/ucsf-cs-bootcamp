def main():
    #Establish the string s variable
    s_main = "fselV9FE5YiaCzX1PS3DqxECygnuseFCJGK82RBfgtyXGNReIHP2vDMoMYY27PB6QRPLawDhK9DrNXe28cDuVrdx5mQtarandusVY0Lt2gtgqJkx2fIoaw48OwMMfFvIWsSItfSQAi7yldIDTizHXthpA05O6Fg2NPAUorijURySSPRc."

    #Establish the indices variables (?) that represent positions to slice at/between
    a = 23
    b = 28
    c = 91
    d = 98

    #Operate on string s using the given indices and see if it returns the sample output "Humpty Dumpty". I had to add in an extra position?
    s_ab = s_main[a:b+1]
    s_cd = s_main[c:d+1]

    print s_ab + " " + s_cd
   
    #I then modified this program to include the values from the dataset for the initial string and the required indices.
main()




