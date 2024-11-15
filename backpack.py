class Backpack:
    def __init__(self, name, colour, max_size = 5):
        self.name = name
        self.colour = colour
        self.max_size = max_size
        self.contents = []

    def __str__(self):
        return f"{self.name}'s backpack coloured {self.colour} and contains {self.contents}."

    def __eq__(self, other):
        return self.name == other.self.name and self.colour == other.self.colour and self.max_size == other.self.capacity

    def put(self, item):
        if len(self.contents) >= self.max_size:
            print("No Room!")
            return
        self.contents.append(item)

    def dump(self):
        self.contents = []


