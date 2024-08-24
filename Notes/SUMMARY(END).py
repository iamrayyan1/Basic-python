# Congratulations!
# As you exit from this course, you have more of a mental model and toolbox to address programming-related problems.
# First, you learned about "functions and variables".
# Second, you learned about "conditionals".
# Third, you learned about "loops".
# Fourth, you learned about "exceptions".
# Fifth, you learned about "libraries".
# Sixth, you learned about "unit tests".
# Seventh, you learned about "file I/O".
# Eighth, you learned about "regular expressions".
# Most recently, you learned about "object-oriented programming".
# Today you learn about many other tools you can use.(etc.)


# This was CS50!
# Creating a final program together, type code say.py in your terminal window and code as follows:

import cowsay
import pyttsx3      # text to speech library

engine = pyttsx3.init()     # initializing the library for text to speech
this = input("What's this? ")
cowsay.cow(this)       # a cow will appear saying the message
engine.say(this)       # program will speak
engine.runAndWait()   # to wait the sentence to complete
# Notice how running this program provides you with a spirited send-off.

# Our great hope is that you will use what you learned in this course to address real problems in the world, making our globe a better place.
# This was CS50!


# LEARN FROM GOOGLE, YOUTUBE AND DOCUMENTATIONS
# DO PROJECTS, APPLYING THE SKILLS IN REAL WORLD