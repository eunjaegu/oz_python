# birds.py
class Eagle:
    def __init__(self, name, species):
        self.name = name
        self.species  = species

    def get_info(self):
        return f"이름: {self.name}, 종: {self.species}"    
