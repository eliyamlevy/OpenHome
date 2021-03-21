import os
import time
import json
import paho.mqtt.publish as publish

class HardwareInterface:

    #sound effects should be a dictionary mapping ints to filepaths
    #of sound effects
    def __init__(self, sound_effects):
        self.sound_effects = sound_effects
        self.internal_volume = 98
        self.setVolume()
        

    #sound will be an int referencing a preset list of effects
    def playSound(self, sound):
        print("Playing sound " + str(sound))
        # Playing the converted file 
        if sound in self.sound_effects:
            audio_file = self.sound_effects[sound]
            play_command = "aplay " if audio_file[-3:] == "wav" else "mpg321 "
            os.system(play_command + audio_file)
        else:
            print("sound unavailable")

    #does text to speak on an inputted text
    def speak(self, text):
        print("Speaker says: " + text)
        publish.single("hermes/tts/say", json.dumps({"text": text, "siteId": "default"}))

    def setVolume(self, volume=None):
        '''
            Submits current HardwareInterface's internal_volume member to the OS
            Optional override to set volume to any given value -- will update internal_volume accordingly
        '''
        self.internal_volume = volume if volume is not None else self.internal_volume
        os.system("amixer set Master " + str(self.internal_volume) + "%")

    def volumeUp(self):
        '''
            Increments current volume value and updates it with OS
        '''
        self.setVolume(volume=max(97, min(100, self.internal_volume + 1)))

    def volumeDown(self):
        '''
            Decrements current volume value and updates it with OS
        '''
        self.setVolume(volume=max(96, self.internal_volume - 1))

    def mute(self):
        self.setVolume(volume=0)

    #does the led controls
    def flash(self, color):
        pass


