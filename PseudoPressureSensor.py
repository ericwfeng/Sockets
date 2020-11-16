from random import randint

class PseudoPressureSensor:
    def __init__(self, min, max):
        """
        min = minimum pressure value
        max = maximum pressure value
        """
        self.state = randint(min, max)
        self.min = min
        self.max = max
    
    def measure(self):
        """
        Generate new pressure measurement / warning.
        """
        self.state = randint(self.min, self.max)
        return self.state