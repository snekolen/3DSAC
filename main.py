from sProfiles import *
from volume import *
from channels import play
import pygame

pygame.init()
pygame.mixer.init()
channel = pygame.mixer.find_channel()

volume = 50

#Testing speaker values
s1 = Speaker("30sdfs93:2321", "Speaker 1", [0, 8, 7]) #Left
s2 = Speaker("30sufs93:2782", "Speaker 2", [8, -18, 4]) #Right


print("------------------------------------")
print("Name:", s1.getName())
print("ID:", s1.getID())
print("Current Location:", s1.getLocation())
print("\nAudio Vector: ", s1.createVec())
print("------------------------------------")

print("Changing speaker location to (23, 1, 0)")

s1.updateLocation([23, 1, 0])

sList = [s1, s2]
userLocation = [13, -18, -9]

print("\nUser Location: ", userLocation)

print("Speaker 1 Location: ", s1.getLocation(), "\nSpeaker 2 Location: ", s2.getLocation())

print("\nAudio Vectors: ", calcVectors(sList, userLocation, volume))

#Running program
while (1):
    userInput = input("Enter 3D user coordinate: ")
    if userInput == "V":    #Changes volume
        volume = int(input("Enter volume: ")) 
        setVolume(volume)
    else:
        xyz = list(map(int, userInput.split()))
        cVecs = calcVectors(sList, xyz, volume) #Prints out volume vectors
        print(cVecs)
        play(cVecs[0], cVecs[1])
    
    
    


'''
Straight line:
Case 0: Same xy plane (Different z)
Case 1: Same yz plane (Different x)
Case 2: Same xz plane (Different y)

Diagonal:
Case 3: Same x coord
Case 4: Same y coord
Case 5: Same z coord

#Different coordinates
Case 6: Different xyz (All different coordinates)


'''

#Getting bluetooth mac address: https://www.geeksforgeeks.org/extracting-mac-address-using-python/

#Gets all devices: https://python-sounddevice.readthedocs.io/en/0.3.15/api/checking-hardware.html
