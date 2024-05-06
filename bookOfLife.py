class BookOfLife:
    def __init__(self, value):
        self.itemName = 'BookOfLife'
        self.value = value

    def __str__(self):
        return f"Buch des Lebens mit Wert {self.value}"