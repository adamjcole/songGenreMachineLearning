
def getFeatures():
    z=[]
    y=[]
    with open('features.txt') as f:
        x = f.read().splitlines()
        for val in x:
            for i in val:
                y.append(int(i))
            z.append(y)
            y=[]
    f.close()    
        
    return(z)

def setFeatures(feat):
    p =(''.join(map(str, feat)))
    f=open('features.txt', 'a')
    f.writelines('\n')
    f.writelines(p)
    f.close
