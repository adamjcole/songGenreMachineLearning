import numpy
from sklearn import tree
import theFeatures
import theLabels
import Chordss


def main():

    chords=["A", "C","G","G"] #                 INPUT
    interval = Chordss.startParse(chords) #translate chords to major scale
    
    keyType = 1 #1 is major, 0 is minor         INPUT
    keyStartProgression = 0 #1 is yes, 0 is no  INPUT
    
    x = similar(interval) #begins to process interval into 8 character array containg match case identifiers
    current = []
    current.append(keyType)
    current.append(keyStartProgression)
    for i in x:
        current.append(i)
        
    features = theFeatures.getFeatures() #text file of features retrieval
    labels = theLabels.getLabels()       #text file of the corresponing labels
    print(current)

    
    guess = processData(current, features, labels) #translates guess to word format
    binGuess = guessTrans(guess) #translates guess to numerical format
    response = input("Is this a " + guess + " song? (y/n) ") #user verifies if song perdiction is correct or incorrect
    if(response == "n"):
        r = input("what genre is this song? ") 
        while(True):
            if(r == "country"):
                theLabels.setLabels(0) #setting the courect label in text file
                break;
            if(r == "hip-hop"):
                theLabels.setLabels(1)
                break;
            if(r == "pop"):
                theLabels.setLabels(2)
                break;
            else:
                r =input("invalid entry, try again ")
    if(response=="y"):
        theLabels.setLabels(binGuess)
                
    theFeatures.setFeatures(current)#setting 10 character binary list to text file
        
def guessTrans(guess):
    result=0
    if(guess == "country"):
        result = 0
    if(guess == "hip-hop"):
        result = 1
    if(guess == "pop"):
        result = 2
    return(result)
    

def processData(current, features, labels):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    #where constraints will go about the song
    output = (clf.predict([current]))
    result = ""
    if(output == 0):
        result = "country"
    if(output == 1):
        result = "hip-hop"
    if(output == 2):
        result = "pop"
    return(result)
    
    
def similar(interval): # finds if matches exist by assigning value of one
    matchData = []
    length = len(interval)
    endPos = length-1
    count = 0
    for i in interval:
        while(True):  
            if(count != endPos): #proceed if positions are not comparing with themselves
                if(i == interval[endPos]):#if values match
                    matchData.append(1)
                    endPos-=1 #re-adjust for next comparision with i
                else:
                    matchData.append(0)
                    endPos-=1
            else:
                count+=1
                endPos = length-1
                break;
    print(matchData)
    m=isMatching(matchData, interval)
    return(m)

                    
def isMatching(data, interval): #for similar values, if match exists, finds the type of match

    pairData = [9]
    length = len(interval)  #amount of chords
    dataLength = len(data) - 1 # amount of data points to determine matches
    gap = 2*(length-2)
    pos = 0
    for i in data:
        #print(pos)
        if(i==1):
            while(True):       
                if(pos == 0 and data[pos]==1):
                    #print("same note starts and resolved progression.......Locations") #represent first and last, value 0
                    pairData.append(0)
                    pos+=1
                    break
                if(pos == len(interval)-2 ):
                    #print("beginning 2 chords are the same chords match")#represent first 2, value 1
                    pairData.append(1)
                    pos+=1
                    break                  
                if(pos == dataLength):
                    #print("ending 2 chords are the same") #representing last 2, value 2
                    pairData.append(2)
                    pos+=1
                    break
                if(pos== gap or pos== gap+2 or pos== gap+3 or pos== gap+4):
                    #print("matchiong chords side by side in middle of pogression") #represent other adjacent chord outcomes between start and end, value 3
                    pairData.append(3)
                    pos+=1
                    break                       
                else:
                    #print("spaced match") # any other chord repetition not as pair, nor beginning and end match, value 4
                    pairData.append(4)
                    pos+=1
                    break;
        else:
            #print("match test is negative")
            pos+=1
    print(pairData)
    
    featuresSequence =assignMatchData(pairData)       
    return(featuresSequence)

def assignMatchData(pair): #assign importance if multiple match occur or other outcomes with many matches
    data = [0,0,0,0,0,0,0,0]
    while(True):
        if len(pair)==1:
            break;
        else:
            data.pop(0)
            data.insert(0,1)
        for i in pair:
            if(i==0): #first and last simlilar, is detected first
                data.pop(1)
                data.insert(1,1)
                data.pop(3)
                data.insert(3,1)
            if(i==1): #begin pair
                data.pop(2)
                data.insert(2,1)
                data.pop(5)
                data.insert(5,1)
            if(i==2): #end chords the same
                data.pop(2)
                data.insert(2,1)
                data.pop(6)
                data.insert(6,1)
            if(i==3): # middle chord pair
                data.pop(2)
                data.insert(2,1)
                data.pop(7)
                data.insert(7,1)
            if(i==4): #any other spaced pair
                data.pop(1)
                data.insert(1,1)
                data.pop(4)
                data.insert(4,1)
                
            
        break;
                
    #print(data)        
    return(data)
            

def startsInKey(chords, key): #takes in original chords and the key to see if firat chord is the key
    dataOfKey = ["A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab"]
    #output 1 means they match, output 0 is they don't match
    matches=0
    if(key == chords[0]):
        matches = 1      
    return(matches)

main()
