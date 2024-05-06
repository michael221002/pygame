import os

import keyboard

from BeamOMat import BeamOMat
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
        won = False;
        while True:

            output = ''

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

            if (self.map.get_next_room(direction) != 'Garden'):
                self.map.move_player(direction)

                if self.map.get_current_room_for_player().roomName == 'laboratory' and self.player.has_item('BookOfLife') and self.player.has_item('Beam-O-Mat'):
                    output = 'Du hast gewonnen'
                    won = True
            else:
                if ('Garden' in self.map.get_next_room(direction) and self.player.has_item('Key') and self.player.has_item('Potion')):
                    self.map.move_player(direction)
                    output = 'Du hast gewonnen'
                    won = True
                else:
                    output = '''Du hast noch nicht ale Items'''

            self.map.display()
            self.player.show_inventory()

            if output != '':
                if (won):
                    print(output)
                    exit(0)
                else:
                    print(output)


            current_room = self.map.get_current_room_for_player()
            print(f"Du befindest dich jetzt in: {current_room.roomName}             X = Player | # = Etwas ist im Raum")
            if current_room.objectInRoom != None:
                monster_in_room, monster_name = self.map.is_monster_in_room()
                if monster_in_room:
                    print(f"Achtung! Ein wildes Monster erscheint: {monster_name}")
                    print("Du wirst zum Start zurückgesetzt")
                else:
                    print(f"Hey du hast ein item gefunden: {current_room.objectInRoom.itemName}")
                    awnser = input("Möchtest du diesen mitnehmen? (y/n): ")
                    if awnser == 'y':
                        self.player.pick_up_item(current_room)

            time.sleep(0.1)

if __name__ =="__main__":
    app = Startup()
    app.run()