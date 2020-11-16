#sensor_task.py read and actuate commands
#when command is recieved, valve is opened, actuate becomes true
class PseudoValve():
    def __init__(self, actuate):
        self.actuate = actuate
    def valveState(self):
        if self.actuate==True:
            print("valve is venting")
        else:
            print("valve is shut")