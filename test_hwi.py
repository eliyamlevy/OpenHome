from HardwareInterface import HardwareInterface

hwi = HardwareInterface({
1: "sounds/piano1.wav",
2: "sounds/piano1.mp3"
})
# check that it plays .wav and .mp3 properly
hwi.playSound(1)
hwi.playSound(2)
# check volume works
hwi.mute()
hwi.playSound(1) # should be silent
hwi.volumeUp()
hwi.playSound(1) # should hear tone now
hwi.volumeUp()
hwi.playSound(1) # should be significantly louder
hwi.volumeDown()
hwi.playSound(1) # should be quieter again
