import os
import random

from Potion import Potion
from key import Key
from monster import Monster
from room import Room
from BeamOMat import BeamOMat
from bookOfLife import BookOfLife


class Map:

    def __init__(self, x, y):
        self.playerIcon = 'X'

        self.map = [[Room() for _ in range(x)] for _ in range(y)]
        self.player_location = [5, 5]
        self.start_location = [5, 5]
        self.update_player_location()
        self.place_items_randomly(1)
        self.create_garden()
        self.create_rooms()

    def create_rooms(self):
        self.create_room('library', BookOfLife('Wissen'), 'L')
        self.create_room('office', None, 'O')
        self.create_room('laboratory', BeamOMat('Teleportation'), 'B')

    def create_room(self, room_name, item, icon):
        room_placed = False
        while not room_placed:
            x = random.randint(0, len(self.map[0]) - 1)
            y = random.randint(0, len(self.map) - 1)
            room = self.map[y][x]
            if room.objectInRoom is None:  # Prüft, ob der Raum leer ist
                room.roomName = room_name
                room.objectInRoom = item
                room.roomIcon = icon  # Setzt das Icon für den Raum
                room_placed = True

    def get_next_room(self, direction):
        new_x, new_y = self.player_location
        if direction == "vorwärts" and new_y > 0:
            new_y -= 1
        elif direction == "rückwärts" and new_y < len(self.map) - 1:
            new_y += 1
        elif direction == "links" and new_x > 0:
            new_x -= 1
        elif direction == "rechts" and new_x < len(self.map[0]) - 1:
            new_x += 1

        # Gibt den Raum an der neuen Position zurück, ohne die Position des Spielers zu aktualisieren
        return self.map[new_y][new_x].roomName

    def create_garden(self):
        garden_placed = False
        while not garden_placed:
            x = random.randint(0, len(self.map[0]) - 1)
            y = random.randint(0, len(self.map) - 1)
            room = self.map[y][x]
            if room.objectInRoom is None:  # Prüft, ob der Raum leer ist
                # Ändert die Eigenschaften des Raums, um ihn zu einem Garten zu machen
                room.roomIcon = '▒'  # Oder jedes andere Icon, das du für den Garten verwenden möchtest
                room.roomName = 'Garden'
                garden_placed = True

    def is_monster_in_room(self):
        # Greift auf den aktuellen Raum des Spielers zu
        current_room = self.map[self.player_location[1]][self.player_location[0]]
        # Prüft, ob im aktuellen Raum ein Monster vorhanden ist
        if isinstance(current_room.objectInRoom, Monster):
            self.player_location = self.start_location.copy()  # Spieler zurück zum Start setzen
            self.update_player_location()
            return True, current_room.objectInRoom.monsterName
        else:
            return False, None

    def place_items_randomly(self, num_items):
        for _ in range(num_items):
            item_placed = False
            while not item_placed:
                x = random.randint(0, len(self.map[0]) - 1)
                y = random.randint(0, len(self.map) - 1)
                if not self.map[y][x].objectInRoom:  # Prüft, ob der Raum leer ist
                    self.map[y][x].objectInRoom = Key('Key to Garden')  # Beispiel: Platziert einen Schlüssel
                    self.map[y][x].roomIcon = '#'
                    item_placed = True

        for _ in range(num_items):
            item_placed = False
            while not item_placed:
                x = random.randint(0, len(self.map[0]) - 1)
                y = random.randint(0, len(self.map) - 1)
                if not self.map[y][x].objectInRoom:  # Prüft, ob der Raum leer ist
                    self.map[y][x].objectInRoom = Potion('Healthy - Potion')  # Beispiel: Platziert einen Schlüssel
                    self.map[y][x].roomIcon = '#'
                    item_placed = True

        for _ in range(num_items + 1):
            item_placed = False
            while not item_placed:
                x = random.randint(0, len(self.map[0]) - 1)
                y = random.randint(0, len(self.map) - 1)
                if not self.map[y][x].objectInRoom:  # Prüft, ob der Raum leer ist
                    self.map[y][x].objectInRoom = Monster('Gustav')  # Beispiel: Platziert einen Schlüssel
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
