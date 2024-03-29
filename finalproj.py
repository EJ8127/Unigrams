
"""
Eric Gomez
Final Project

Creating Unigrams 
"""

def main():
    #opens the file up
    story = open('green.txt')
    #processes the file that was opened
    txt = story.read()
    
    #replaces \n which is caused when skipping a line with a blank space
    txt = txt.replace("\n", " ")
    #seperates the text to put into a list
    txt = txt.split(" ")
    
    #creates an empty set of list
    one = []
    count = []
    
    #for loop that goes through each text and puts it into the list
    for i in range(len(txt)):
        #checks if its in the list or not
        if txt [i] not in one:
            one.append(txt[i])
            count.append(1)
        else:
            test = one.index(txt[i])
            count[test] += 1
    #it counts and prints the text and the number of times it was repeated
    for i in range(len(one)):
        print(one[i], " ", count[i])
        
main()

'''
Psuedocode

The story variable opens the text file and stores the text

variable txt reads and stores the read text from story
txt.replace is used to replace \n with a space so it doesnt mess with the list
txt.split basically seperates each word/text to make it possible to put into a list

list called one and count are created so we can populate them

A for loop that contains an if statment is created to run over and over until the full length of the txt is ran through
if txt[i] is not in the variable list one then it adds it and adds a count to it
else it adds 1 to the count to whatever it already has

another for loop that goes through the whole list of one and prints each list text and how many times it appeared in it
'''