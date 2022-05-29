from fileinput import filename


def countWords():
    filename=input("Enter File Name")
    numberOfWords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("number of words")
    print(numberOfWords)
countWords()