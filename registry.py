#regstry.py: is able to show the state of the rocket at all times
class registry:
   
   def __init__(self, actuatePressureRelease, pressureSensorReading):
      self.actuatePressureRelease = actuatePressureRelease
      self.pressureSensorReading = pressureSensorReading  
         
   def viewReadings(self):
      print("Valve State: " + self.actuatePressureRelease)
      if self.pressureSensorReading > 460  or self.pressureSensorReading < 50:
         print("The sensor reading is " + str(self.pressureSensorReading) + " and it is in a critical state.")
      else:
         print("The sensor reading is " + str(self.pressureSensorReading) + " Readings are NORMINAL")

      
      
      
      
      
      
        
