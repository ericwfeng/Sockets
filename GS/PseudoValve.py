class PseudoValve:
    def __init__(self):
        self.state = 'off'
    
    def flip(self):
        if self.state == 'off':
            self.state = 'on'
        else:
            self.state = 'off'