import keras
#This file works with audio calibration and correction

def calibrate(obj, speakers): #Calibrates 
    #Detect speakers and create profiles
    
    #Press button on remote when finished with calibration
    
    #If no speakers detected
    if speakers == []:
        raise Exception("Unable to calibrate system")

    #Successful calibration
    obj.changeState() #Changes state to 1 (Starts at 0)
    return
    

def correction(): #Corrects audio
    pass

def ambient(): #For Ambient noise
    pass

def materials(): #For materials that distort noise
    pass
