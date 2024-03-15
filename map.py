import os


class Map:
    def __init__(self, x, y):
        self.map = [[' ' for _ in range(x)] for _ in range(y)]
        self.player_location = [0, 0]
        self.update_player_location()

    def update_player_location(self):
        # Zuerst die Karte bereinigen
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                self.map[y][x] = ' '
        # Dann den Spieler an der neuen Position eintragen
        self.map[self.player_location[1]][self.player_location[0]] = 'P'

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
            print(row)