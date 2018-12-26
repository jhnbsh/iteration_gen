# iteration_gen v1.0 Help File

# Description
 This python script generates combinations of words from a provided
 dictionary for use in password cracking.  The input is a dictionary of words (see input.txt)
 and the output is a listing of all combinations based on the user supplied number of iterations. 
 
 Example: 
 If the input dictionary is: Apple, Banana, Orange, and the number of iterations is chosen as 4, the output will be:
 
AppleAppleAppleApple  
AppleAppleAppleBanana  
AppleAppleAppleOrange  
AppleAppleBananaApple  
AppleAppleBananaBanana  
AppleAppleBananaOrange  
AppleAppleOrangeApple   
AppleAppleOrangeBanana.... (continued) 

# Why is this script needed?:
  This program creates a password cracking dictionary (of user defined length / iterations) to defeat 
  passwords made from sequential words.  The idea for this program is a response to the 
  popular cartoon "xkcd" which makes an argument in one issue regarding password strength.
  xkcd argues the entropy in four random words is stronger than a shorter password of 
  difficult to remember characters.

  The xkcd cartoon can be viewed at:  https://www.xkcd.com/936/

# Prerequisites:
   Python v2 is needed to execute the script.  The following provides basic directions
   on installing Python on your respective operating system.

   Windows users: As of Windows 8.1 you will need to install Python v2.
   1. Download and install python from https://www.python.org/downloads/ . Note: Choose any version of Python that starts with "2", not "3".
   1. Select all default settings, except for on the 'Customize Python'
   screen click "Add python.exe to Path" and choose "Will be installed to local hard-drive".

   MacOS users:  None, python should be natively installed.

   Linux users:  None, python should be natively installed.

# Execution instructions
  Place your dictionary (input.txt) in the same directory as iteration_gen.py.  
  Run iteration_gen from a command prompt or terminal window with:
  
    python iteration_gen.py
    
# Note on filesize and RAM: 
As of version 1.0 this script works only with small dictionaries and iterations.  If too large a dictionary is used, or
too high an iteration value, your computer will likely exhaust all of its RAM and the program will crash.

# Planned updates:
* Provide user control over printing sub-iterations.
* Provide estimation of final filesize.
* Provide estimation on required RAM to compute final dictionary.
* Memory management to calculate larger dictionaries and iterations.
    
    
