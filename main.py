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
            if keyboard.is_pressed('up') or (keyboard.is_pressed('w')):
                direction = 'vorwärts'
            elif keyboard.is_pressed('down') or (keyboard.is_pressed('s')):
                direction = 'rückwärts'
            elif keyboard.is_pressed('left') or (keyboard.is_pressed('a')):
                direction = 'links'
            elif keyboard.is_pressed('right') or (keyboard.is_pressed('d')):
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
            current_room = self.map.get_current_room_for_player()
            print(f"Du befindest dich jetzt in: {current_room.roomName}")
            if current_room.objectInRoom != None:
                print(f"Hey du hast ein item gefunden: {current_room.objectInRoom.itemName}")
            self.player.pick_up_item(current_room)

            time.sleep(0.1)

if __name__ =="__main__":
    app = Startup()
    app.run()