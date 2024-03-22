class Potion:
    def __init__(self, value):
        self.itemName = 'Potion'
        self.value = value

    def __str__(self):
        return f"Potion mit Wert {self.value}"
