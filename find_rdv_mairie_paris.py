"""
After the end of the lockdown, in Paris it is very difficult to access a public office, for example those where the id cards are delivered.
The Paris City Hall put in place a web form to find an available rendez-vous, if any.
But the user has to click on the form and check, on each of the 20 possible civic centers, if there is any availability.

The answer can change at any moment, since time slots can be free after a withdrawal.

This python script uses pyautogui package to automatically click on buttons until an availability is found.

Warning : my code is very raw, I spent 30min to write it and I debug it ...until I found a rendez-vous :)
Do not use it as-is on sensitive web applications!

Author: Alessandro Giassi 2021
"""

'''
Before to start, you have to fill the form (https://rdv-titres.apps.paris.fr/) 
and follow the procedure until the form will ask you to choose a place for the rendez-vous.
Then the code can be used to automatize the search among the 20 civic centers.
'''

#Packages
import pyautogui
import time
import winsound

#find the icon of the targeted web site among the open tabs of your browser, then move to this position (TODO: exception not managed)
pyautogui.moveTo('.\\buttons_pictures\\icone_site_web.png')

#then click to activate the right web page
pyautogui.click()

#start a 'while' cycle until all the civic centers are checked or a rendez-vous is found
N_civiccenters = 19

n=0
while True:
    n +=1
    
    try:
        #click anywhere (on a non active position)
        pyautogui.click(100,200)
        
        #find the button where the possible civic centers are shown, and click on it 
        pyautogui.moveTo('.\\buttons_pictures\\choisissez.png')
        pyautogui.click()
    except:
        #a short beep to say that the script cannot find the button (could be a problem of resolution)
        winsound.Beep(1000, 1000)
        break
    
    #scroll down the list of civic centers until it reaches the n-th center, then click 
    for i in range(0,n):
        pyautogui.press('down')
    pyautogui.click()

    #the web site reacts after a (variable) amount of time, this 'while' cycle waits until the screen changes
    refimage = pyautogui.screenshot()
    while True:
        if pyautogui.locateOnScreen(refimage, confidence=0.99):
            time.sleep(1)
        else:
            break

    #if the 'pasderdvbla.png' message appears, it means that there is no possible rendez-vous in this civic center
    try:
        pyautogui.moveTo('.\\buttons_pictures\\pasderdvblabla.png')
        nordv = True
    except:
        nordv = False

    #if no rdv click on the 'nordvok.png' button, to move on
    if nordv:
        try:
            pyautogui.moveTo('.\\buttons_pictures\\nordvok.png')
            pyautogui.click()
        except:
            print('no rdv, but cannot find ok button')
    else:
        #there is a rendez-vous! A sound to celebrate
        duration = 3000  # milliseconds
        freq = 540  # Hz
        winsound.Beep(freq, duration)
   
    #close the main 'while' cycle if the rendez-vous is found or if all civic centers are checked
    if (nordv==False)|(i==N_civiccenters):
        break
	