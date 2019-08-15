

def getLabels():
    f = open('labels.txt', "r")
    x = [] #all the data
   
    for i in f.read():
        if(i!="\n"):
        
            i.strip()
            x.append(int(i))
    f.close()
    
    return(x)

def setLabels(label):
    x = str(label)
    f=open('labels.txt', 'a')
    f.writelines("\n")
    f.writelines(x)
    f.close
