'''This file aims to creates a speaker profile for each speaker'''

class Speaker:
    def __init__(self, mac, name, location): #Each speaker profile
        self.mac = mac #Speaker address
        self.name = name #Speaker nickname
        self.location = location #Sets initial location during calibration (use array)
    
    def getID(self): #Gets mac address
        return self.mac
    
    def getName(self):
        return self.name
    
    def getLocation(self):
        return self.location
        
    def createVec(self): #Inverts location (pos -> neg and vice versa)
        soundVec = [-1*self.location[0], -1*self.location[1], -1*self.location[2]]
        return soundVec
    
    def updateLocation(self, coordinate): #Updates location of speaker
        self.location = coordinate
    


