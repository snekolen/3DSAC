import subprocess
import time


#Calculates vectors for 2 or more speakers
def calcVectors(speakers, userLoc, volume): #Speaker obj, int arr[x, y, z], int
    relVecs = [] #For both speakers
    volume *= 0.01

    #Creates vectors for both speakers
    for s in speakers:
        sLoc = s.getLocation()
        relVecs.append([userLoc[0] - sLoc[0], userLoc[1] - sLoc[1], userLoc[2] - sLoc[2]])
    
    #Creates volume vectors
    netVecs = []
    volVecs = [[], []]
    for i in range(0, 2):
        netVol = ((relVecs[i][0])**2 + (relVecs[i][1])**2 + (relVecs[i][2])**2) ** (1/3)
        netVecs.append(netVol)
    print(relVecs)

    vecTot = netVecs[0] + netVecs[1]
    
    #Vectors
    #vec0 = netVecs[0] ** 3
    x = ((volume * netVecs[0] / vecTot) ** 3 / ((relVecs[0][0])**2 + (relVecs[0][1])**2 + (relVecs[0][2])**2)) ** 0.5

    for i in range(0, 3):
        volVecs[0].append(relVecs[0][i] * x)


    #Vector 1
    y = ((volume * netVecs[1] / vecTot) ** 3 / ((relVecs[1][0])**2 + (relVecs[1][1])**2 + (relVecs[1][2])**2)) ** 0.5
    
    for i in range(0, 3):
        volVecs[1].append(relVecs[1][i] * y)
    
    totVecs = []
    #Sums up length of vectors
    for i in range(0, 2):
        totVecs.append(((volVecs[i][0])**2 + (volVecs[i][1])**2 + (volVecs[i][2])**2) ** (1/3))
        
    return totVecs #Returns volumes of vectors





# a value between 0 and 100
def setVolume(volume):
    command = ["amixer", "sset", "Master", "{}%".format(volume)]
    subprocess.Popen(command)
    time.sleep(0.3)
    
    
    
#Selects case
def selCase(s):
    match(s):
        case 1 | 12 | 18: return [0, 0, 0]
        case 11 | 13: return [0, 3, 0]
        case 2: return [0, 0, 2]
        case 3: return [-1, 1, 0]
        case 4: return [1, 1, 1]
        case 5: return [-1, 1, 1]
        case 6: return [-4, 0, 0]
        case 7: return [3, 0, 4]
        case 8: return [-4, 0, 4]
        case 9: return [4, 0, 4]
        case 10: return [3, 0, 0.1] #At a speaker
        case 14: return [-2, 3, 3]
        case 15: return [0, 0, 1]
        case 16: return [1, 2, 0]
        case 17: return [3, 2, 2]

