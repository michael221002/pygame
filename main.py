import os

import keyboard
from map import Map
from player import Player
import time
class Startup:
    def __init__(self):
        print("Anwendung gestartet!")
        self.map = Map(10, 10)
        self.map.display()
        self.player = Player('Der ultimative Micha')
        self.player.show_inventory()
    def run(self):
        self.map.display()
        self.player.show_inventory()
        while True:
            if keyboard.is_pressed('up'):
                direction = 'vorwärts'
            elif keyboard.is_pressed('down'):
                direction = 'rückwärts'
            elif keyboard.is_pressed('left'):
                direction = 'links'
            elif keyboard.is_pressed('right'):
                direction = 'rechts'
            elif keyboard.is_pressed('esc'):
                print("Spiel beendet.")
                break
            else:
                # Wartet kurz, um zu verhindern, dass die Schleife zu schnell durchläuft
                time.sleep(0.1)
                continue  # Springt zurück zum Anfang der Schleife, wenn keine Taste gedrückt wurde

            self.map.move_player(direction)
            self.map.display()
            self.player.show_inventory()
            time.sleep(0.1)

if __name__ =="__main__":
    app = Startup()
    app.run()