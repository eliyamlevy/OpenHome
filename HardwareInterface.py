from gtts import gTTS 
import os

class HardwareInterface:

    #sound effects should be a dictionary mapping ints to filepaths
    #of sound effects
    def __init__(self, sound_effects):
        self.sound_effects = sound_effects

    #sound will be an int referencing a preset list of effects
    def playSound(self, sound):
        print("Playing sound " + str(sound))
        # Playing the converted file 
        os.system("mpg321 " + self.sound_effects[sound])

    #does text to speak on an inputted text
    def speak(self, text):
        print("Speaker says: " + text)
        language = 'en'

        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed 
        myobj = gTTS(text=text, lang=language, slow=False) 

        # Saving the converted audio in a mp3 file named 
        # welcome 
        myobj.save("sounds/say.mp3") 

        # Playing the converted file 
        os.system("mpg321 sounds/say.mp3") 


    #does the led controls
    def flash(self, color):
        pass