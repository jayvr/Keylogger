import keyboard as kb
import os


class CaptureKeys:
    keystrokes = []
    kys = " "

    def __init__(self):
        kb.on_press(callback=self.getKeystrokes)

    def getKeystrokes(self, event):
        # Append the pressed key to the keystrokes list
        if event.name == "space" or event.name == "." or event.name == "enter" or event.name == "esc" or event.name == "Shift":
            self.keystrokes.append(self.kys)
            self.kys = " "
        else:
            self.kys = self.kys + event.name

    def stop(self, esc = 'esc'):
        kb.wait(esc)
        kb.unhook_all()
        return self.keystrokes




keys = CaptureKeys()

data = keys.stop()
# Print the recorded keystrokes
print('Recorded keystrokes:', data)

print ("That's All Folks!!!")
