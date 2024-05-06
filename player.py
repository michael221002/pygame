class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_to_inventory(self, item):
        """Fügt dem Inventar ein Objekt hinzu."""
        self.inventory.append(item)

    def show_inventory(self):
        """Gibt alle Objekte im Inventar aus."""
        if self.inventory:
            print(f"Inventar von {self.name}:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print(f"{self.name} hat ein leeres Inventar.")

    def has_item(self, item_name):
        return any(item.itemName == item_name for item in self.inventory)

    def pick_up_item(self, room):
        if room.objectInRoom:
            self.add_to_inventory(room.objectInRoom)
            print(f"{self.name} hat {room.objectInRoom} aufgehoben.")
            room.objectInRoom = None  # Entfernt den Gegenstand aus dem Raum