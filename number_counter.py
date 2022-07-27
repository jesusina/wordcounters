#the "#" sign tells the computer
#this is a COMMENT.  The computer ignores COMMENTS.
#Write COMMENTS in your code so that people
#who read your code know what it does.

#numbercounter.py -- We want to write a program that will
#count the number of 0s and 1s in the file "zeros_and_ones_data_sequence.txt"
#and tells us how many 0s and how many 1s.

f=open("zeros_and_ones_data_sequence.txt")#opens this file for reading. 
numberofZeros=0
numberofOnes=0
i=0#i keeps a count of how many lines I read
for line in f:  #"line" is a line of the file.
    i=i+1
    if int(line) == 0:#int(line) turns the line into an integer
        numberofZeros=numberofZeros+1
    if int(line) == 1:
        numberofOnes=numberofOnes+1
    #print ("the", i, "th line is:")#FOR loop does something once for each line
    #print (line)
  
print ("Current number of 0s is:", numberofZeros)
print ("I have this many 1s:", numberofOnes)
