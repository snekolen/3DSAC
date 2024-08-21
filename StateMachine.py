from positionCalc import *
from multiprocessing import Process

'''
State Machine
0: Calbration/Recalibration
1: Running system
'''

class StateMachine:
    def __init__(self):
        self.speakers = [] #Contains info about all speakers
        self.state = 0 #Starts w/ calibration
    
    def addSpeaker(self,speaker):
        self.speakers.append(speaker)
        
    def removeSpeaker(self, speaker):
        self.speakers.remove(speaker)
        
    def resetAll(self): #Clears all speakers in list / Use for recalibration
        self.speakers.clear()
        self.state = 0
        
    def changeState(self):
        match self.state:
            case 0:
                self.state = 1
            case 1:
                self.state = 0
        
    def run(self): #Runs 
        try:
            calibrate()
        except Exception: #catches exception
            self.run() #Recalibrates again and continues until at least a spaker is added
            
        while True:
            match self.state:
                case 0: #System reset/recalibration
                    self.resetAll()
                    self.run()
                case 1:
                    pass
                    #Make speakers operate parallel to each other and update location after every clock period (Use multiprocessing module)
                    #If unreponsive for n seconds, reset all and rerun
                    
                    
                    
                    
                    

