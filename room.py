class Room:
    def __init__(self):
        self.roomIcon = '□'  # Hier hast du 'roomIcon' genannt
        self.roomName = 'empty Room'
        self.has_player = False  # Dieses Attribut fehlte in deinem Originalcode

    @property
    def display_icon(self):
        # Rot: \033[91m, Zurücksetzen: \033[0m
        return '\033[91mX\033[0m' if self.has_player else self.roomIcon
