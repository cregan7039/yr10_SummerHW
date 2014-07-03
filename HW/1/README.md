#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
Because at the basic level a computer is only a series of switches that are either on or off, 1's and 0's
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
181
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
String
```

(b) What type of data is returned by this function? **(1 mark)**
```
Boolean
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
7, output spelt incorrectly
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
A mistake made by the programmer e.g misspelt word
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
Where the program runs but it dosent do what you wanted it to do
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
Run-time errors are errors that occur while your program runs. These typically occur when your program attempts an operation that is impossible to carry out. An example of this is dividing a number by 0.

```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
answer here
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe: This is where computers, servers and printers are joined to one cable which is called "the bus" and at each end of the cable there are terminators. There are used to stop signals from reflecting down the bus.

Advantages: Easy to install this.

Disadvantages: All devices can see the data so there are security risks.
```

**Ring Topology (6 marks)**
```
Describe: All devices are connected in a ring and data flows through all the devices in one direction.

Advantages: No need for a network server.

Disadvantages: If one workstation fails then the rest of the network will get affected.
```

**Star Topology (6 marks)**
```
Describe: Each device on the network has its own cable that connects to a switch or a hub.

Advantages: High preformance because no data collisions will occur

Disadvantages: If the hub or switch fails then there will be no network connection.
```
