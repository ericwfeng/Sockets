class PseudoValve:
    def __init__(self):
        self.state = 'closed'
    
    def flip(self):
        if self.state == 'closed':
            self.state = 'open'
        else:
            self.state = 'closed'