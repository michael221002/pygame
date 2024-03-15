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