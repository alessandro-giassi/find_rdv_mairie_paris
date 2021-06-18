# find_rdv_mairie_paris
After the end of the lockdown, in Paris it is very difficult to access a public office, for example those where the id cards are delivered. 
The Paris City Hall put in place a web form to find an available rendez-vous, if any. 
But the user has to click on the form and check, on each of the 20 possible civic centers, if there is any availability.

The answer can change at any moment, since time slots can be free after a withdrawal.

This python script uses pyautogui package to automatically click on buttons until an availability is found.

Warning : my code is very raw, I spent 30min to write it and I debug it ...until I found a rendez-vous :) 

Do not use it as-is on sensitive web applications!

Author: Alessandro Giassi 2021
