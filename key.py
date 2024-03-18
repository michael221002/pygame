class Key:
    def __init__(self, value):
        self.itemName = 'Key'
        self.value = value

    def __str__(self):
        return f"Schlüssel mit Wert {self.value}"
