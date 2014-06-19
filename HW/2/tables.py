userNum = int(input("Enter a number of which you would like to find the timestable for: ")) #User enters number for the timestable the wish to see.
number = 1 #Number that gets multiplied by the users number
while number != 13: #Loop stops when number equals 13
    overall = userNum * number #This times the users number by num
    print(overall) #Prints out the overall number
    number = number + 1 #This steps number up so when it loops through everything num goes up one which makes the timestable increase

