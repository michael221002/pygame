import os
import random

from key import Key
from room import Room


class Map:

    def __init__(self, x, y):
        self.playerIcon = 'X'

        self.map = [[Room() for _ in range(x)] for _ in range(y)]
        self.player_location = [5, 5]
        self.update_player_location()
        self.place_items_randomly(10)

    def place_items_randomly(self, num_items):
        for _ in range(num_items):
            item_placed = False
            while not item_placed:
                x = random.randint(0, len(self.map[0]) - 1)
                y = random.randint(0, len(self.map) - 1)
                if not self.map[y][x].objectInRoom:  # Prüft, ob der Raum leer ist
                    self.map[y][x].objectInRoom = Key(29380)  # Beispiel: Platziert einen Schlüssel
                    self.map[y][x].roomIcon = '#'
                    item_placed = True

    def update_player_location(self):
        # Zuerst die Karte bereinigen und `has_player` für alle Räume auf False setzen
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                self.map[y][x].has_player = False  # Spieler ist hier nicht
        # Dann den Spieler an der neuen Position markieren
        self.map[self.player_location[1]][self.player_location[0]].has_player = True

    def move_player(self, direction):
        if direction == "vorwärts" and self.player_location[1] > 0:
            self.player_location[1] -= 1  # Bewegt den Spieler nach oben
        elif direction == "rückwärts" and self.player_location[1] < len(self.map) - 1:
            self.player_location[1] += 1  # Bewegt den Spieler nach unten
        elif direction == "links" and self.player_location[0] > 0:
            self.player_location[0] -= 1  # Bewegt den Spieler nach links
        elif direction == "rechts" and self.player_location[0] < len(self.map[0]) - 1:
            self.player_location[0] += 1  # Bewegt den Spieler nach rechts
        self.update_player_location()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear_console()
        for row in self.map:
            rowGesamt = ''
            for room in row:
                rowGesamt += room.display_icon + '  '  # Verwende `display_icon` für die Darstellung
            print(rowGesamt)

    def get_current_room_for_player(self):
        # Greift auf die Position des Spielers zu und gibt den entsprechenden Raum zurück
        current_room = self.map[self.player_location[1]][self.player_location[0]]
        return current_room
