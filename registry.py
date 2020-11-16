#regstry.py: is able to show the state of the rocket at all times
class registry:
   def __init__(self):
      self.actuatePressureRelease = actuatePressureRelease
      self.actuatePressureRelease = False
      self.pressureSensorReading = pressureSensorReading
      self.pressureSensorReading = 250    
         
   def viewReadings(self):
      print "Pressure released yet: " + actuatePressureRelease
      if self.pressureSensorReading > 460  or self.pressureSensorReading < 50:
         print "The sensor reading is " + pressureSensorReading + " and everything is fine!"
      else:
         print "The sensor reading is " + pressureSensorReading + " and it is in a critical state."

      
      
      
      
      
      
        