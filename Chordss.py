


chordsIn = ["A", "B", "E", "C#"]
key = "B"

majorInterval = ["I", "ii", "iii", "IV", "V", "vi", "viI"]
allNotes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
notesExtended = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
#startParse(chordsIn, majorInterval, allNotes, notesExtended, key)
#properMajorInterval(notesExtended, "A")

def startParse(chordsIn):
    count = 0
    results = []
    start = 0
    for i in chordsIn:
        location = 0
        exists = False
        if(count ==0):
            results.append(1)
            count+=1
            step = 0
            for j in allNotes: #finding first note location in allNotes to subtract later
                if(i ==j):
                    start = step
                    break;
                else:
                    step+=1
        else:
            counter = 0
            
            for j in allNotes:
                if(i ==j):
                    current = counter
                    break;
                else:
                    counter+=1
            
            difference = counter-start
            if(difference%2 == 0):
                 location = (difference/2) +1
            else:
                 location = ((difference -1)/2)+2         
            
            results.append(int(location))
                            
    return(results)        
                    

#def rotateWithKey(interval, key, kind): #interval the key and major or minor specs

def properMajorInterval(notesExtended, key):
    steps= [2,2,1,2,2,2]
    results = []
    count = 0
    for i in notesExtended:
        if(i == key):
            results.append(i)
            break;
        else:
            count+=1
    
    for i in steps:
        results.append(notesExtended[count+i])
        count = count+i
    print(results)
    return(results)        

#def verifyInterval(allNotes, majorInt, interval, chords, key):
